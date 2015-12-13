__author__ = 'Călin Sălăgean'

from utils.IO import IO
from events.models.event import Event

class EventRepository():

    def __init__(self, filename = 'event.json'):
        '''
        EventRepository class constructor
        :param filename: Default value 'event.json'
        :return:
        '''
        self.__datafile = filename
        Event.set_class_id(self.get_max_id())

    def insert(self, event):
        '''
        Add an event object into disk storage
        :param event:
        :return: None
        '''
        operation = IO(self.__datafile)

        try:
            data = operation.get()
        except ValueError:
            data = []

        data.append(event.get_serialization())

        operation.set(data)

    def update(self, updated_event):
        '''
        Updates an event into disk storage
        :param updated_event:
        :return:
        '''
        operation = IO(self.__datafile)
        events = operation.get()
        for event in events:
            if event['id'] == updated_event.get_id():
                events[events.index(event)] = updated_event.get_serialization()
                break

        operation.set(events)

    def delete(self, deleted_event):
        '''
        Deletes an event from disk storage
        :param deleted_event:
        :return:
        '''
        operation = IO(self.__datafile)
        events = operation.get()
        for event in events:
            if event['id'] == deleted_event.get_id():
                events.remove(event)
                break

        operation.set(events)

    def get(self, id):
        '''
        Returns an event with provided ID from disk storage
        :param id:
        :return: Event instance
        '''
        operation = IO(self.__datafile)
        for event in operation.get():
            if event['id'] == id:
                return Event(event['date'], event['time'], event['description'], event['id'])

        raise ValueError('Event not found!')

    def get_all(self):
        '''
        Returns all events from disk storage
        :return:
        '''
        operation = IO(self.__datafile)
        events = []
        for event in operation.get():
            instance = Event(event['date'], event['time'], event['description'], event['id'])
            events.append(instance)

        return events

    def get_max_id(self):
        '''
        Returns the maximum ID found on disk storage
        :return:
        '''
        events = self.get_all()
        max = -1

        for event in events:
            if max < event.get_id():
                max = event.get_id()

        return max + 1