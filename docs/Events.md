# **Events Management System**  

## **Imports**  
```py
from ecoi.core.events import Event
```

## **CRUD & Lifecycle Operations**  
```py
event = Event.createEvent(...)
event_id = event.id

event.update(...)
event.delete()
event.cancel()

event.start()
event.end()
event.block()
```


## **Sponsorship, Advertising & Financials**  
```py
event.sponsorships.add(...)
event.sponsorships.get(...)
event.sponsorships.remove(...)

event.ads.add(...)
event.ads.get(...)
event.ads.remove(...)

event.payments.add(...)
event.payments.get(...)
event.payments.remove(...)

event.gifts.add(...)
event.gifts.get(...)
event.gifts.remove(...)

event.rewards.add(...)
event.rewards.get(...)
event.rewards.remove(...)
```

## **Event Rounds & Stages**  
```py
event.rounds.add(...)
event.rounds.get(...)
event.rounds.remove(...)
event.rounds.update(...)

round = event.rounds.get()[0]
round.next()
round.info()
```


## **Participants & Jury**  
```py
event.participants.add(...)
event.participants.get(...)
event.participants.remove(...)
event.participants.update(...)
event.participants.block(...)
event.participants.consentForm(...)
```

### **Voting & Jury System**  
```py
round.participants.vote(...)       
round.participants.getVotes(...)  

round.jury.vote(participant_id)  
round.jury.getVotes(...)           
```

## **Groups & Roles**  
```py
event.groups.add(...)
event.groups.get(...)
event.groups.remove(...)
event.groups.update(...)

event.roles.add(...)
event.roles.get(...)
event.roles.remove(...)
event.roles.update(...)
```

## **Permissions & Access Control**  
```py
event.permissions.add(...)
event.permissions.get(...)
event.permissions.remove(...)
event.permissions.update(...)
```

## **Sub-Events (Nested Events)**  
```py
event.subEvents.add(...)
event.subEvents.get(...)
event.subEvents.remove(...)
event.subEvents.update(...)
```

## **Deadlines & Scheduling**  
```py
event.deadlines.add(...)
event.deadlines.get(...)
event.deadlines.remove(...)
event.deadlines.update(...)
```

## **Quizzes, Tests & Activities**  
```py
event.activities.add(...)
event.activities.get(...)
event.activities.remove(...)
event.activities.update(...)
```

## **Event Website & Contact Management**  
```py
event.site.get(...)
event.site.update(...)
event.site.remove(...)
event.contacts.get(...)
event.contacts.add(...)
event.contacts.remove(...)
event.contacts.update(...)
```