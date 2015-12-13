__author__ = 'Călin Sălăgean'

from utils.IO import IO
from events.models.person_event import PersonEvent

class PersonEventRepository():
    def __init__(self, filename = None):
        self.__defaultfile = filename or 'person_event.json'

    def insert(self, person_event):
        operation = IO(self.__defaultfile)

        try:
            person_events = operation.get()
        except ValueError:
            person_events = []

        person_events.append(person_event.get_serialization())
        operation.set(person_events)

    def get_all(self):
        operation = IO(self.__defaultfile)

        person_events = []

        for person_event in operation.get():
            person_events.append(PersonEvent(person_event['person_id'], person_event['event_id'], person_event['date']))

        return person_events

    def get_by_id(self, person_id = None, event_id = None):
        operation = IO(self.__defaultfile)

        person_events = []

        for person_event in operation.get():
            if person_id is not None and event_id is not None:
                if person_event['person_id'] == person_id and person_event['event_id'] == event_id:
                    return [PersonEvent(person_id, event_id, person_event['date'])]
            elif person_id is None:
                if person_event['event_id'] == event_id:
                    person_events.append(PersonEvent(person_event['person_id'], event_id, person_event['date']))
            else:
                if person_event['person_id'] == person_id:
                    person_events.append(PersonEvent(person_id, person_event['event_id'], person_event['date']))

        return person_events