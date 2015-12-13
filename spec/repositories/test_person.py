__author__ = 'Călin Sălăgean'

import unittest
from utils.IO import IO
from events.repositories.person import PersonRepository
from events.models.person import Person

class TestPersonRepository(unittest.TestCase):
    def test_initialization(self):
        io = IO('test.json')
        io.set([])

        repository = PersonRepository('test.json')
        self.assertIsInstance(repository, PersonRepository)

    def test_insert(self):
        io = IO('test.json')
        io.set([])

        Person.set_class_id(0)
        person = Person('Vasile', 'Pop', 'Str. Calea Floresti, nr. 24')
        repo = PersonRepository('test.json')
        repo.insert(person)

        people = io.get()
        person = people[0]

        self.assertEqual(len(people), 1)
        self.assertEqual(person['id'], 0)
        self.assertEqual(person['first_name'], 'Vasile')
        self.assertEqual(person['last_name'], 'Pop')
        self.assertEqual(person['address'], 'Str. Calea Floresti, nr. 24')

    def test_get_all(self):
        io = IO('test.json')
        io.set([])

        Person.set_class_id(0)
        person = Person('Vasile', 'Pop', 'Str. Calea Floresti, nr. 24')
        repo = PersonRepository('test.json')
        repo.insert(person)

        people = repo.get_all()

        self.assertEqual(len(people), 1)

        person = people[0]

        self.assertEqual(person.get_id(), 0)
        self.assertEqual(person.get_name(), 'Vasile Pop')
        self.assertEqual(person.get_address(), 'Str. Calea Floresti, nr. 24')

    def test_get(self):
        io = IO('test.json')
        io.set([])

        Person.set_class_id(10)
        person = Person('Vasile', 'Pop', 'Str. Calea Floresti, nr. 24')
        repo = PersonRepository('test.json')
        repo.insert(person)

        person = repo.get(10)

        self.assertEqual(person.get_id(), 10)
        self.assertEqual(person.get_name(), 'Vasile Pop')
        self.assertEqual(person.get_address(), 'Str. Calea Floresti, nr. 24')

        with self.assertRaisesRegex(ValueError, 'Person not found!'):
            person = repo.get(0)

    def test_update(self):
        io = IO('test.json')
        io.set([])

        Person.set_class_id(10)
        person = Person('Vasile', 'Pop', 'Str. Calea Floresti, nr. 24')
        repo = PersonRepository('test.json')
        repo.insert(person)

        person = repo.get(10)
        person.update('Dan', 'Popescu', 'Calea Dorobantilor')
        repo.update(person)

        updated_person = repo.get(10)

        self.assertEqual(person.get_id(), 10)
        self.assertEqual(person.get_name(), 'Dan Popescu')
        self.assertEqual(person.get_address(), 'Calea Dorobantilor')

    def test_delete(self):
        io = IO('test.json')
        io.set([])

        Person.set_class_id(10)
        person = Person('Vasile', 'Pop', 'Str. Calea Floresti, nr. 24')
        repo = PersonRepository('test.json')
        repo.insert(person)

        repo.delete(person)

        with self.assertRaisesRegex(ValueError, 'Person not found!'):
            person = repo.get(10)