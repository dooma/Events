__author__ = 'Călin Sălăgean'

import unittest, os
from utils.IO import IO
from events.repositories.event import EventRepository
from events.models.event import Event

class TestEventRepository(unittest.TestCase):
    def test_insert(self):
        io = IO('test.json')
        io.set([])

        event = Event('14/01/2015', '14:00', 'Colectiv')
        EventRepository('test.json').insert(event)

        content = io.get()
        self.assertIs(type(content), list)

        stored_event = content[0]

        self.assertEqual(stored_event['date'], '14/01/2015')
        self.assertEqual(stored_event['time'], '14:00')
        self.assertEqual(stored_event['description'], 'Colectiv')

    def test_get_all(self):
        io = IO('test.json')
        io.set([])
        repo = EventRepository('test.json')

        content = repo.get_all()

        self.assertEqual(content, [])

        event1 = Event('14/01/2015', '14:00', 'Colectiv')
        event2 = Event('14/01/2015', '14:00', 'Colectiv')
        repo.insert(event1)
        repo.insert(event2)

        content = repo.get_all()
        self.assertIs(type(content), list)
        self.assertEqual(len(content), 2)

        stored_event1 = content[0]
        stored_event2 = content[1]

        self.assertEqual(stored_event1.get_date(), '14/01/2015')
        self.assertEqual(stored_event1.get_time(), '14:00')
        self.assertEqual(stored_event1.get_description(), 'Colectiv')
        self.assertEqual(stored_event2.get_date(), '14/01/2015')
        self.assertEqual(stored_event2.get_time(), '14:00')
        self.assertEqual(stored_event2.get_description(), 'Colectiv')

    def test_get(self):
        Event.set_class_id(0)
        io = IO('test.json')
        io.set([])
        repo = EventRepository('test.json')

        event1 = Event('14/01/2015', '14:00', 'Colectiv')
        event2 = Event('14/01/2015', '14:00', 'Colectiv')
        repo.insert(event1)
        repo.insert(event2)

        content = repo.get(0)
        self.assertIs(type(content), Event)

        self.assertEqual(content.get_date(), '14/01/2015')
        self.assertEqual(content.get_time(), '14:00')
        self.assertEqual(content.get_description(), 'Colectiv')

        with self.assertRaisesRegex(ValueError, 'Event not found!'):
            content = repo.get(10)

    def test_update(self):
        Event.set_class_id(0)
        io = IO('test.json')
        io.set([])
        repo = EventRepository('test.json')

        event1 = Event('14/01/2015', '14:00', 'Colectiv')
        event2 = Event('14/01/2015', '14:00', 'Colectiv')
        repo.insert(event1)
        repo.insert(event2)

        event = repo.get(0)
        self.assertIs(type(event), Event)
        event.update('15/01/2015', '15:00', 'Untold festival')

        repo.update(event)

        updated_event = repo.get(0)

        self.assertEqual(updated_event.get_date(), '15/01/2015')
        self.assertEqual(updated_event.get_time(), '15:00')
        self.assertEqual(updated_event.get_description(), 'Untold festival')

    def test_get_max_id(self):
        Event.set_class_id(0)
        io = IO('test.json')
        io.set([])
        repo = EventRepository('test.json')
        self.assertEqual(repo.get_max_id(), 0)
        content = repo.get_all()
        self.assertEqual(content, [])

        event1 = Event('14/01/2015', '14:00', 'Colectiv')
        event2 = Event('14/01/2015', '14:00', 'Colectiv')
        repo.insert(event1)
        repo.insert(event2)

        content = repo.get_all()
        self.assertEqual(repo.get_max_id(), 2)

    def test_delete(self):
        Event.set_class_id(0)
        io = IO('test.json')
        io.set([])
        repo = EventRepository('test.json')

        event1 = Event('14/01/2015', '14:00', 'Colectiv')
        event2 = Event('14/01/2015', '14:00', 'Colectiv')
        repo.insert(event1)
        repo.insert(event2)

        event = repo.get(0)
        self.assertIs(type(event), Event)

        repo.delete(event)

        with self.assertRaisesRegex(ValueError, 'Event not found!'):
            updated_event = repo.get(0)