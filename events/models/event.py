__author__ = 'Călin Sălăgean'

from datetime import datetime
import re

class Event():
    __id_class = 0

    def __init__(self, date = None, time = None, description = None, id = None):
        '''
        Event class contructor
        :param date:
        :param time:
        :param description:
        :return: Instance variable
        '''
        self.validate(date, time, description)
        self.__date, self.__time, self.__description, self.__id = date, time, description, self.__set_id(id)

    def validate(self, date, time, description):
        '''
        Raise exceptions if parameters doesn't have right format
        :param date:
        :param time:
        :param description:
        :return: None
        '''
        if not date or not time or not description:
            raise AttributeError("Please provide all fields")

        try:
            datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Date doesn't have the right format")

        time = re.sub('\W', '', time)
        if (len(time) != 4 and len(time) != 2) or not time.isdigit():
            raise ValueError("Time doesn't have the right format")

    def __set_id(self, id):
        '''
        Increments class _id attribute
        :return: None
        '''
        if id is None:
            instance_id = Event.__id_class
        else:
            instance_id = id

        Event.__id_class += 1
        return instance_id

    def get_id(self):
        '''
        Returns event id
        :return: id
        '''
        return self.__id

    def get_date(self):
        '''
        Returns event date
        :return: date
        '''
        return self.__date

    def get_time(self):
        '''
        Returns event time
        :return: time
        '''
        return self.__time

    def get_description(self):
        '''
        Returns event description
        :return: description
        '''
        return self.__description

    def update(self, date = None, time = None, description = None):
        '''
        Updates event instance
        :param date:
        :param time:
        :param description:
        :return:
        '''
        if date is None:
            date = self.__date
        if time is None:
            time = self.__time
        if description is None:
            description = self.__description

        self.validate(date, time, description)
        self.__date, self.__time, self.__description = date, time, description

    def get_serialization(self):
        '''
        Returns JSON object
        :return: json
        '''
        dict = {
            'id': self.get_id(),
            'date': self.get_date(),
            'time': self.get_time(),
            'description': self.get_description()
        }

        return dict

    @staticmethod
    def set_class_id(id):
        '''
        Sets class id
        :param id:
        :return:
        '''
        Event.__id_class = id