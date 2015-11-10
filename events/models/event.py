__author__ = 'Călin Sălăgean'

from datetime import datetime

class Event():

    def __init__(self, date = None, time = None, description = None):
        self.validate(date, time, description)
        self.date, self.time, self.description = date, time, description

    def validate(self, date, time, description):
        '''
        Raise exceptions if parameters doesn't have right format
        :param date:
        :param time:
        :param description:
        :return:
        '''
        if not date or not time or not description:
            raise AttributeError("Please provide all fields")

        try:
            datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Date doesn't have the right format")

        clock = time.split(':')

        try:
            hours = str(int(clock[0]))
            minutes = str(int(clock[1]))

            if len(minutes) < 2:
                minutes = '0'.join(minutes)
        except (ValueError, IndexError):
            raise ValueError("Time doesn't have the right format")

