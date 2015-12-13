__author__ = 'Călin Sălăgean'

import unittest
from events.models.person_event import PersonEvent

class TestPersonEvent(unittest.TestCase):
    def test_instance(self):
        with self.assertRaises(ValueError):
            person_event = PersonEvent(1, 2)
            self.assertIsInstance(person_event, PersonEvent)

    def test_validation(self):
        with self.assertRaisesRegex(AttributeError, 'Please provide all fields'):
            person_event = PersonEvent()
            person_event = PersonEvent(person_id=1)
            person_event = PersonEvent(event_id=1)

        with self.assertRaisesRegex(ValueError, 'Invalid IDs! Please provide valid IDs'):
            person_event = PersonEvent(1, 1)

        person_event = PersonEvent(25, 25)

    def test_update(self):
        person_event = PersonEvent(25, 25)

        person_event.update(25,84)

        self.assertEqual(person_event.get_person_id(), 25)
        self.assertEqual(person_event.get_event_id(), 84)

    def test_get_serialization(self):
        person_event = PersonEvent(25, 25)

        serialization = person_event.get_serialization()

        self.assertEqual(serialization['person_id'], 25)
        self.assertEqual(serialization['event_id'], 25)