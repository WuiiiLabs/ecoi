from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Literal
from bson import ObjectId
from datetime import date, datetime
from ...config import DB as db

class User(BaseModel):
    _id: str
    name: str
    gmail: EmailStr
    gender: Literal['Male', 'Female', 'Others']
    birthday: date
    location: str
    group_id: str

    lvl: int = 1
    blocked: list = []
    active: datetime = datetime.now()

    model_config = ConfigDict(extra='allow')

    _persist: bool = True
    _update_query: dict = {}

    def model_post_init(self, __context):
        if self._persist:
            self.save()

    def update(self, **kwargs):
        filtered = {k: v for k, v in kwargs.items() if v is not None}
        for k, v in filtered.items():
            setattr(self, k, v)
        self._update_query.setdefault('$set', {}).update(filtered)

    def upgrade(self):
        self.lvl += 1
        self._update_query.setdefault('$inc', {})['lvl'] = 1

    def active(self):
        self.active = datetime.now()
        self._update_query.setdefault('$set', {})['active'] = self.active

    def save(self):
        if not self._update_query:
            return
        db['users'].update_one(
            {"_id": ObjectId(self._id)},
            self._update_query,
            upsert=True
        )
        self._update_query.clear()

    def report(self, user_id: str, reason: str):
        pass

    def block(self, user_id: str, reason: str):
        self.blocked.append(user_id)
        self._update_query.setdefault('$addToSet', {}).setdefault('blocked', []).append(user_id)

    def unblock(self, user_id: str, reason: str):
        if user_id in self.blocked:
            self.blocked.remove(user_id)
            self._update_query.setdefault('$pull', {})['blocked'] = user_id

    def delete(self):
        db['users'].delete_one({"_id": ObjectId(self._id)})

    

def getById(user_id: str) -> User | None:
    data = db['users'].find_one({"_id": ObjectId(user_id)})
    if data:
        data['_id'] = str(data['_id'])
        return User(**data, _persist=False)
    return None