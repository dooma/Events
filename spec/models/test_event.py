__author__ = 'Călin Sălăgean'

import unittest
from events.models.event import Event

class TestEvent(unittest.TestCase):
    def test_initialization(self):
        event = Event('14/01/2015', '14:00', 'Colectiv')
        self.assertIsInstance(event, Event)

    def test_date_input_validation(self):
        with self.assertRaises(AttributeError):
            event = Event(time = '14:00', description = 'Colectiv')

    def test_time_input_validation(self):
        with self.assertRaises(AttributeError):
            event = Event(date = '14/01/2015', description = 'Colectiv')

    def test_valid_properties(self):
        event = Event('14/01/2015', '14:00', 'Colectiv')
        self.assertEqual(event.date, '14/01/2015')
        self.assertEqual(event.time, '14:00')
        self.assertEqual(event.description, 'Colectiv')

    def test_date_format_validation(self):
        with self.assertRaisesRegexp(ValueError, "Date doesn't have the right format"):
            event = Event('14012015', '14:00', 'Colectiv')

    def test_time_format_validation(self):
        with self.assertRaisesRegex(ValueError, "Time doesn't have the right format"):
            event = Event('14/01/2015', '1400', 'Colectiv')