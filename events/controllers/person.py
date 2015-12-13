__author__ = 'Călin Sălăgean'

from events.repositories.person_event import PersonEvent, PersonEventRepository
from events.repositories.person import PersonRepository
from events.repositories.event import EventRepository
from events.models.person_event import PersonEvent
import re

class PersonController():
    def __init__(self):
        '''
        PersonController constructor
        :return: object
        '''
        self.repository = PersonRepository()
        self.person_event_repository = PersonEventRepository()
        self.event_repository = EventRepository()

    def index(self):
        '''
        Return all persons
        :return: string
        '''

        output = ""

        for person in self.repository.get_all():
            output += str(person.get_id()) + "\t" + person.get_name() + "\t" + person.get_address() + "\n"
        return output

    def show(self, id):
        '''
        Return a found person
        :param id:
        :return: string
        '''
        try:
            id = int(id)
        except ValueError:
            return "Please enter an integer for ID"

        try:
            person = self.repository.get(id)
            return str(person.get_id()) + "\t" + person.get_name() + "\t" + person.get_address() + "\n"
        except (ValueError, AttributeError) as e:
            return e

    def insert(self, name = None, address = None, event = None):
        '''
        Insert a person
        :param date:
        :param time:
        :param description:
        :return: string
        '''
        try:
            person = Person(name, address, event)
            self.repository.insert(person)
        except (ValueError, AttributeError) as e:
            return e
        return "Inserted successfully"

    def update(self, id, first_name = None, last_name = None, address = None):
        '''
        Update an event
        :param id:
        :param date:
        :param time:
        :param description:
        :return: string
        '''
        try:
            id = int(id)
        except ValueError:
            return "Please insert a valid ID"

        try:
            person = self.repository.get(id)
        except ValueError as e:
            return e

        if first_name == '':
            first_name = None
        if last_name == '':
            last_name = None
        if address == '':
            address = None

        try:
            person.update(first_name, last_name, address)
            self.repository.update(person)
        except (ValueError, AttributeError) as e:
            return e

        return "Person updated successfully!"

    def delete(self, id):
        '''
        Delete an event from instances array
        :param id:
        :return: string
        '''
        try:
            id = int(id)
        except ValueError:
            return "Please enter an integer for ID"

        try:
            person = self.repository.get(id)
            self.repository.delete(person)
        except (ValueError, AttributeError) as e:
            return e

        return "Person was deleted successfully"

    def associate(self, person_id, event_id, data):
        '''
        Associate a person with an event
        :param person_id:
        :param event_id:
        :param data:
        :return: string
        '''
        try:
            person_id = int(person_id)
            event_id = int(event_id)
        except ValueError:
            return "Please enter an integer for ID"

        try:
            person_event = PersonEvent(person_id, event_id, data)
            self.person_event_repository.insert(person_event)
        except (ValueError, AttributeError) as e:
            return e

        return "Association created successfully"

    def search(self, term):
        '''
        Search people by term
        :param term:
        :return: string
        '''
        found_people = []

        for person in self.repository.get_all():
            person_criteria = person.get_name() + person.get_address()

            if (re.match(term.lower(), person_criteria.lower()) is not None):
                found_people.append(person)

        output = ""
        for person in found_people:
            output += str(person.get_id()) + "\t" + person.get_name() + "\t" + person.get_address() + "\n"
        return output

    def get_events(self, id):
        '''
        Return events that a person has participated in
        :param id:
        :return: string
        '''
        try:
            id = int(id)
        except ValueError:
            return "Please enter an integer for ID"

        output = ""

        try:
            relations = self.get_instantiated_relation(id)
        except:
            print("The id doesn't exist")

        relations.sort(key=lambda rel: (rel[0].get_description(), rel[0].get_date()))

        for relation in relations:
            event = relation[0]
            person = relation[1]
            date = relation[2]

            output += str(event.get_id()) + "\t" + event.get_description() + "\t Inscreire in data: " + str(date) + "\n"

        return output

    def get_top_persons(self):
        '''
        Return top people with most visits
        :return: string
        '''
        relations = self.get_instantiated_relation()

        occurences = self.determine_occurences(relations)

        relations.sort(
            key=lambda rel: PersonController.find_dict(occurences, rel[1].get_id())[rel[1].get_id()],
            reverse=True
        )

        # Unique relations
        unique_relations = []
        actual_person = -1

        for rel in relations:
            if rel[1].get_id() != actual_person:
                actual_person = rel[1].get_id()
                unique_relations.append(rel)

        output = ""

        for rel in unique_relations:
            number_events = PersonController.find_dict(occurences, rel[1].get_id())[rel[1].get_id()]
            output += rel[1].get_name() + "\tparticipa la\t" + str(number_events) + "\n"

        return output

    def get_instantiated_relation(self, person_id = None, event_id = None):
        '''
        Reinstantiate a relation between person and event from repository
        :param person_id:
        :param event_id:
        :return: string
        '''
        if person_id is None and event_id is None:
            person_events = self.person_event_repository.get_all()
        else:
            person_events = self.person_event_repository.get_by_id(person_id, event_id)

        result = []

        for relation in person_events:
            event = self.event_repository.get(relation.get_event_id())
            person = self.repository.get(relation.get_person_id())
            date = relation.get_date()

            if date is None:
                date = "Doesn't exist"

            result.append((event, person, date))

        return result

    @staticmethod
    def determine_occurences(relations):
        '''
        Find occurences in multiple tuples of realtions
        :param relations:
        :return: array
        '''
        occurences = []

        for relation in relations:
            person_id = relation[1].get_id()
            try:
                occurence = PersonController.find_dict(occurences, person_id)
            except:
                occurences.append({
                    person_id: 0
                })
                occurence = occurences[-1]
            finally:
                occurence[person_id] += 1

        return occurences

    @staticmethod
    def find_dict(array, id):
        '''
        Find dictionary with given id
        :param array:
        :param id:
        :return: dictionary
        :raise: ValueError if id is not found
        '''
        for elem in array:
            try:
                elem[id]
                return elem
            except KeyError:
                continue

        raise ValueError