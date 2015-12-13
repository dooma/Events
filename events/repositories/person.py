__author__ = 'Călin Sălăgean'

from events.models.person import Person
from utils.IO import IO

class PersonRepository():

    def __init__(self, filename = 'person.json'):
        '''
        PersonRepository class constructor
        :param filename: Default value 'person.json'
        :return:
        '''
        self.__defaultfile = filename
        Person.set_class_id(self.get_max_id())

    def insert(self, person):
        '''
        Add a person object into disk storage
        :param event:
        :return: None
        '''
        operation = IO(self.__defaultfile)

        try:
            people = operation.get()
        except ValueError:
            people = []

        people.append(person.get_serialization())
        operation.set(people)

    def update(self, person):
        '''
        Updates a person into disk storage
        :param updated_event:
        :return:
        '''
        operation = IO(self.__defaultfile)
        people = operation.get()

        for per in people:
            if per['id'] == person.get_id():
                people[people.index(per)] = person.get_serialization()

        operation.set(people)

    def delete(self, person):
        '''
        Deletes a person from disk storage
        :param deleted_event:
        :return:
        '''
        operation = IO(self.__defaultfile)
        people = operation.get()

        for per in people:
            if per['id'] == person.get_id():
                people.remove(per)
        operation.set(people)

    def get(self, id):
        '''
        Returns a person with provided ID from disk storage
        :param id:
        :return: Event instance
        '''
        for per in self.get_all():
            if per.get_id() == id:
                return per

        raise ValueError('Person not found!')

    def get_all(self):
        '''
        Returns all persons from disk storage
        :return:
        '''
        operation = IO(self.__defaultfile)
        people = []

        for person in operation.get():
            person_instance = Person(person['first_name'], person['last_name'], person['address'], person['id'])
            people.append(person_instance)

        return people

    def get_max_id(self):
        '''
        Returns the maximum ID found on disk storage
        :return:
        '''
        people = self.get_all()
        max = -1

        for person in people:
            if max < person.get_id():
                max = person.get_id()

        return max + 1