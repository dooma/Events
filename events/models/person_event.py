__author__ = 'Călin Sălăgean'

from events.repositories.event import EventRepository
from events.repositories.person import PersonRepository
from datetime import datetime

class PersonEvent():
    def __init__(self, person_id = None, event_id = None, date = None):
        '''
        PersonEvent constructor
        :param person_id:
        :param event_id:
        :param date:
        :return: object
        '''
        self.validate(person_id, event_id, date)
        self.__person_id, self.__event_id, self.__date = person_id, event_id, date

    @staticmethod
    def validate(person_id, event_id, date):
        '''
        Validates PersonEvent params
        :param person_id:
        :param event_id:
        :param date:
        :return: None
        :raise AttributeError:
        :raise ValueError:
        '''
        if person_id is None or event_id is None:
            raise AttributeError('Please provide all fields')

        event_repository = EventRepository()
        person_repository = PersonRepository()

        try:
            event = event_repository.get(event_id)
            person = person_repository.get(person_id)
        except ValueError:
            raise ValueError('Invalid IDs! Please provide valid IDs')

        if date is not None:
            try:
                datetime.strptime(date, '%d/%m/%Y')
            except ValueError:
                raise ValueError("Date doesn't have the right format")

    def update(self, person_id = None, event_id = None, date = None):
        '''
        Updates realation between person and event
        :param person_id:
        :param event_id:
        :param date:
        :return: None
        '''
        if person_id is None:
            person_id = self.__person_id
        if event_id is None:
            event_id = self.__event_id
        if date is None:
            date = self.__date

        self.validate(person_id, event_id, date)

        self.__person_id, self.__event_id, self.__date = person_id, event_id, date

    def get_person_id(self):
        '''
        Returns person ID
        :return person_id:
        '''
        return self.__person_id

    def get_event_id(self):
        '''
        Returns event ID
        :return event_id:
        '''
        return self.__event_id

    def get_date(self):
        '''
        Returns date when relation was instantiated
        :return date:
        '''
        return self.__date

    def get_serialization(self):
        '''
        Returns a JSON serialization
        :return: JSON Object
        '''
        dict = {
            'person_id': self.__person_id,
            'event_id': self.__event_id,
            'date': self.__date
        }

        return dict