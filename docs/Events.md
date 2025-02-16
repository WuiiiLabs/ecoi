# Events
Events can be of many types and different structures. These properties and features should be addressed while making docs for the events:
- basic curd operations of events
- events with multiple stages
- events with multiple rounds
- participants dividing and merging
- filtering of events
- advertisements of events
- deadlines of rounds
- multiple events within event
- backward propogation for ranking
- groups allocation in event
- roles allocation
- permissions allocation
- sponsorships of event
- payments of event
- quizes, tests, and other activities of events
- bad participant blocking, consent forms, and other features
- gifts, rewards, and other incentives provided by event
- jurying process, voting process, and other decision making processes
- event site hosting and other processes

## Imports 
```py
from ecoi.core import events as evts
```

## CURD+ Operations
```py
event = evts.createEvent(...)
event_id = event.id

event.cancel(...)
event.update(...)

event.start(...)
event.block(...)
event.end(...)

event.sponsor(...)
event.advertise(...)
event.pay(...)
event.gift(...)
event.reward(...)

event.delete()
```

## Event Structure
```py
event.rounds()
event.addRounds(...)
event.removeRounds(...)
event.updateRounds(...)

round = event.rounds()[0]
round.filter(...)
round.addFilter(...)
round.removeFilter(...)
round.updateFilter(...)
round.filterInfo(...)

event.addSubEvent(...)
event.subEventInfo(...)
event.removeSubEvent(...)
event.updateSubEvent(...)
event.subEvents()
```

## Event Information
```py
event.getRound(...)
event.getRounds(...)
event.getParticipant(...)
event.getParticipantStatus(...)
event.getParticipants(...)
event.getGroup(...)
event.getGroups(...)
event.getRole(...)
event.getRoles(...)
event.getOrganizer(...)
event.getOrganizers(...)
event.getJury(...)
event.getJurys(...)
event.getSponsor(...)
event.getSponsors(...)
event.getAd(...)
event.getAds(...)
event.getPayment(...)
event.getPayments(...)
event.getGift(...)
event.getGifts(...)
event.getReward(...)
event.getRewards(...)
event.getFilter(...)
event.getFilters(...)
event.getSubEvent(...)
event.getSubEvents(...)
event.getPermission(...)
event.getPermissions(...)
event.getSite(...)
event.getContacts(...)

round.info(...)
round.filterInfo(...)
```

## Event Management
```py
event.participants()
event.addParticipants(...)
event.removeParticipants(...)
event.updateParticipants(...)
```
