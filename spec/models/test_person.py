__author__ = 'Călin Sălăgean'

import unittest

from events.models.person import Person

class TestPerson(unittest.TestCase):
    def test_initialization(self):
        person = Person('Vasile', 'Pop', 'Str. Calea Floresti, nr. 24')

        self.assertIsInstance(person, Person)

    def test_attributes_consistency(self):
        person = Person('Vasile', 'Pop', 'Str. Calea Floresti, nr. 24')

        self.assertEqual(person.get_name(), 'Vasile Pop')
        self.assertEqual(person.get_address(), 'Str. Calea Floresti, nr. 24')

    def test_validation_errors(self):
        with self.assertRaisesRegex(AttributeError, "Please provide full name"):
            person = Person(address = 'Str. Calea Floresti, nr. 24')

        with self.assertRaisesRegex(AttributeError, "Please provide full name"):
            person = Person()

        with self.assertRaisesRegex(AttributeError, "Please provide an address"):
            person = Person('Vasile', 'Pop')

        person = Person('Vasile', 'Pop', 'Str. Calea Floresti, nr. 24')

    def test_update(self):
        person = Person('Vasile', 'Pop', 'Str. Calea Floresti, nr. 24')
        person_id = person.get_id()

        person.update('Teodor')
        self.assertEqual(person.get_name(), 'Teodor Pop')
        self.assertEqual(person.get_address(), 'Str. Calea Floresti, nr. 24')
        self.assertEqual(person.get_id(), person_id)

        person.update('Teodor', 'Popescu')
        self.assertEqual(person.get_name(), 'Teodor Popescu')
        self.assertEqual(person.get_address(), 'Str. Calea Floresti, nr. 24')
        self.assertEqual(person.get_id(), person_id)

        person.update('Teodor', 'Popescu', 'Calea Dorobantilor, nr. 33')
        self.assertEqual(person.get_name(), 'Teodor Popescu')
        self.assertEqual(person.get_address(), 'Calea Dorobantilor, nr. 33')
        self.assertEqual(person.get_id(), person_id)

    def test_id_incrementation(self):
        Person.set_class_id(0)

        person1 = Person('Vasile', 'Pop', 'Str. Calea Floresti, nr. 24')
        person2 = Person('Vasile', 'Pop', 'Str. Calea Floresti, nr. 24')

        self.assertEqual(person1.get_id(), 0)
        self.assertEqual(person2.get_id(), 1)

    def test_set_class_id(self):
        Person.set_class_id(10)

        person = Person('Vasile', 'Pop', 'Str. Calea Floresti, nr. 24')
        self.assertEqual(person.get_id(), 10)

    def test_get_serialization(self):
        Person.set_class_id(0)
        person = Person('Vasile', 'Pop', 'Str. Calea Floresti, nr. 24')

        response = person.get_serialization()

        self.assertEqual(response['id'], 0)
        self.assertEqual(response['first_name'], 'Vasile')
        self.assertEqual(response['last_name'], 'Pop')
        self.assertEqual(response['address'], 'Str. Calea Floresti, nr. 24')