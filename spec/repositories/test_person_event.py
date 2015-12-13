__author__ = 'Călin Sălăgean'

import unittest
from events.repositories.person_event import PersonEventRepository, PersonEvent
from utils.IO import IO

class TestPersonEventRepository(unittest.TestCase):
    def test_insert(self):
        repo = PersonEventRepository()

        person_event = PersonEvent(25, 61)
        repo.insert(person_event)

        person_events = repo.get_by_id(25, 61)
        self.assertEqual(len(person_events), 1)

        # Remove last appended object
        io = IO('person_event.json')
        updated_person_events = io.get()
        updated_person_events.pop()
        io.set(updated_person_events)

    def test_get_all(self):
        repo = PersonEventRepository()

        person_events = repo.get_all()

        self.assertEqual(len(person_events), 15)

    def test_get_by_id(self):
        repo = PersonEventRepository()

        person_events = repo.get_by_id(person_id=25)
        self.assertEqual(len(person_events), 3)

        person_events = repo.get_by_id(event_id=79)
        self.assertEqual(len(person_events), 4)

        person_events = repo.get_by_id(25, 84)
        self.assertEqual(len(person_events), 1)