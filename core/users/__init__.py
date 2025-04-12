from datetime import datetime as _datetime
from typing import Literal as _Literal

def createUser(
    id: str,                  # Unique identifier for the user
    name: str,                # Full name of the user
    gmail: str,               # Gmail address for the user
    gender: _Literal['Male', 'Female', 'Other'],  # Gender identity of the user
    birthday: _datetime,       # Birthdate of the user (in datetime format)
    location: str,            # Geographical location (city, country)
    group_id: str,            # Group the user belongs to, e.g., '123'
):
    """
    Create a new user.
    """

    pass

def update(
    name: str,               # Update the user's name
    gmail: str,              # Update the user's email
    location: str,           # Update location
    birthday: _datetime,      # Update birthday
    group_id: str,           # Update group membership
    **kwargs                 # Other optional fields like gender, profile picture
):
    """
    Update user information.
    """
    pass

def active():
    """
    Last active time of the user.
    """
    pass

def report(
    user_id: int,            # ID of the user to be reported
    reason: str              # Reason for reporting the user 
):
    """
    Report a user.
    """
    pass

def block(
    user_id: int,            # ID of the user to block
    reason: str              # Reason for blocking the user (e.g., 'spam')
):
    pass

def unblock(
    user_id: int,            # ID of the user to unblock
    reason: str              # Reason for unblocking the user (e.g., 'misunderstanding')
):
    pass

def delete():              # Delete the user's account permanently
    pass

class profile:
    def __init__(self, user_id: str):
        self.user_id = user_id

    def read(
        self, 
        format: _Literal['dict', 'bson'] = 'dict',
        print_console: _Literal[True, False] = False,
        filter: Dict = None,
        query_vars: List = None,
        limit: int = 10
    ):
        """
        Read the user's profile details with optional filtering.
        """
        pass

    def update(
        self,
        name: str = None,
        pfp: str = None,   # Profile picture URL or file path
        status: str = None,  # Status message
        bio: str = None,  # Short bio
        gender: _Literal['Male', 'Female', 'Other'] = None,
        location: str = None,
        birthday: _datetime = None,
        relationship: str = None,  # Relationship status
        orientation: str = None,  # Sexual orientation
        **kwargs
    ):
        """
        Update the user's profile details.
        """
        pass

    class personality:
        def read(self, ptype: str = None):
            """
            Read personality details based on a specific personality type.
            """
            pass

        def update(
            self,
            mbti: str = None,
            dom: str = None,   # Dominant personality trait
            moral: str = None,  # Moral alignment
            enneg: str = None,  # Enneagram type
            tempr: str = None,  # Temperament
            analytical: str = None,
            zodiac: str = None,
            mental_age: str = None,
            **kwargs
        ):
            """
            Update user's personality type details.
            """
            pass

    class academics:
        def read(self, filter: Dict):
            """
            Read academic data with filter conditions.
            """
            pass

        def update(
            self,
            certifications: List = None,
            projects: List = None,
            skills: List = None,
            education: List = None,
            workExp: List = None,
            **kwargs
        ):
            """
            Update the user's academic details.
            """
            pass

        class Projects:
            def read(self, filter: Dict):
                """
                Read academic projects with filters.
                """
                pass

            def add(
                self,
                name: str,
                link: str,
                description: str,
                since: _datetime,
                till: _datetime = None,
                **kwargs
            ):
                """
                Add a new academic project.
                """
                pass

            def update(
                self,
                name: str = None,
                link: str = None,
                description: str = None,
                since: _datetime = None,
                till: _datetime = None,
                **kwargs
            ):
                """
                Update an existing academic project.
                """
                pass

            def delete(self):
                """
                Delete a project from the user's profile.
                """
                pass

        class Skills:
            def read(self):
                """
                Read the user's skills.
                """
                pass

            def add(self, name: str, description: str, **kwargs):
                """
                Add a new skill.
                """
                pass

            def update(self, name: str = None, description: str = None, **kwargs):
                """
                Update an existing skill.
                """
                pass

            def delete(self):
                """
                Delete a skill from the profile.
                """
                pass

        class Certifications:
            def read(self, filter: Dict):
                """
                Read certifications based on filters.
                """
                pass

            def add(
                self,
                name: str,
                org: str,
                link: str,
                description: str,
                since: _datetime,
                till: _datetime = None,
                **kwargs
            ):
                """
                Add a new certification.
                """
                pass

            def update(
                self,
                name: str = None,
                org: str = None,
                link: str = None,
                description: str = None,
                since: _datetime = None,
                till: _datetime = None,
                **kwargs
            ):
                """
                Update an existing certification.
                """
                pass

            def delete(self):
                """
                Delete a certification.
                """
                pass

        class Education:
            def read(self, filter: Dict, query_vars: List = None, limit: int = 10):
                """
                Read education details.
                """
                pass

            def add(
                self,
                name: str,
                degree: str,
                field: str,
                link: str,
                org: str,
                since: _datetime,
                till: _datetime = None,
            ):
                """
                Add education details.
                """
                pass

            def update(
                self,
                name: str = None,
                degree: str = None,
                field: str = None,
                link: str = None,
                org: str = None,
                since: _datetime = None,
                till: _datetime = None,
                **kwargs
            ):
                """
                Update education details.
                """
                pass

            def delete(self):
                """
                Delete an education record.
                """
                pass

    class workExperience:
        def read(self):
            """
            Read work experience details.
            """
            pass

        def add(
            self,
            position: str,
            company: str,
            start_date: _datetime,
            end_date: _datetime = None,
            description: str = '',
        ):
            """
            Add work experience details.
            """
            pass

        def update(
            self,
            work_id: str,
            position: str = None,
            company: str = None,
            start_date: _datetime = None,
            end_date: _datetime = None,
            description: str = None,
        ):
            """
            Update work experience details.
            """
            pass

        def delete(self, work_id: str):
            """
            Delete a work experience record.
            """
            pass

    class interests:
        def read(self, filter: Dict = None, query_vars: List = None, limit: int = 10):
            """
            Read user interests.
            """
            pass

        def add(self, name: str, description: str, since: _datetime, till: _datetime = None):
            """
            Add an interest.
            """
            pass

        def update(
            self,
            name: str = None,
            description: str = None,
            since: _datetime = None,
            till: _datetime = None,
        ):
            """
            Update an interest.
            """
            pass

        def delete(self):
            """
            Delete an interest.
            """
            pass

    class hobbies:
        def read(self, filter: Dict = None, query_vars: List = None, limit: int = 10):
            """
            Read user hobbies.
            """
            pass

        def add(self, name: str, description: str, since: _datetime, till: _datetime = None):
            """
            Add a hobby.
            """
            pass

        def update(
            self,
            name: str = None,
            description: str = None,
            since: _datetime = None,
            till: _datetime = None,
        ):
            """
            Update a hobby.
            """
            pass

        def delete(self):
            """
            Delete a hobby.
            """
            pass
