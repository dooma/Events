__author__ = 'Călin Sălăgean'

from events.models.event import Event
from events.repositories.event import EventRepository
from events.repositories.person_event import PersonEventRepository
from events.repositories.person import PersonRepository

class EventController():
    def __init__(self):
        '''
        EventController constructor
        :return: object
        '''
        self.repository = EventRepository()
        self.person_event_repository = PersonEventRepository()
        self.person_repository = PersonRepository()

    def index(self):
        '''
        Return all events in one string ready to display
        :return: string
        '''
        events = self.repository.get_all()

        output = ""

        for event in events:
            output += str(event.get_id()) + "\t" + event.get_date() + "\t" + event.get_time() + "\t" + event.get_description() + "\n"

        return output

    def show(self, id):
        '''
        Return a found event ready to display
        :param id:
        :return: string
        '''
        try:
            id = int(id)
        except ValueError:
            return "Please enter an integer for ID"

        try:
            event = self.repository.get(id)
            return str(event.get_id()) + "\t" + event.get_date() + "\t" + event.get_time() + "\t" + event.get_description() + "\n"
        except (ValueError, AttributeError) as e:
            return e

    def insert(self, date = None, time = None, description = None):
        '''
        Insert an event
        :param date:
        :param time:
        :param description:
        :return: string
        '''
        try:
            event = Event(date, time, description)
        except (AttributeError, ValueError) as e:
            return e

        self.repository.insert(event)

        return "Event inserted successfully"

    def update(self, id, date = None, time = None, description = None):
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
            event = self.repository.get(id)
        except ValueError as e:
            return e

        if date == '':
            date = None
        if time == '':
            time = None
        if description == '':
            description = None

        try:
            event.update(date, time, description)
            self.repository.update(event)
        except (ValueError, AttributeError) as e:
            return e

        return "Event updated successfully!"

    def delete(self, id):
        '''
        Delete an event
        :param id:
        :return: string
        '''
        try:
            id = int(id)
        except ValueError:
            return "Please enter an integer for ID"

        try:
            event = self.repository.get(id)
            self.repository.delete(event)
        except (ValueError, AttributeError) as e:
            return e

        return "Event was deleted successfully"

    def get_top_events(self):
        '''
        Show top events with most visitors
        :return: string
        '''
        relations = self.get_instantiated_relation()

        occurences = self.determine_occurences(relations)

        relations.sort(
            key=lambda rel: EventController.find_dict2(occurences, rel[0].get_id())[rel[0].get_id()],
            reverse=True
        )

        # Unique relations
        unique_relations = []
        actual_event = -1

        for rel in relations:
            if rel[0].get_id() != actual_event:
                actual_event = rel[0].get_id()
                unique_relations.append(rel)

        output = ""

        for rel in unique_relations:
            number_events = EventController.find_dict2(occurences, rel[0].get_id())[rel[0].get_id()]
            output += str(rel[0].get_id()) + "\t" + rel[0].get_description() + "\tparticipa \t" + str(number_events) + " persoane\n"

        return output

    def get_instantiated_relation(self, person_id = None, event_id = None):
        '''
        Instantiate a Repository Many-to-Many relation
        :param person_id:
        :param event_id:
        :return: array
        '''
        if person_id is None and event_id is None:
            person_events = self.person_event_repository.get_all()
        else:
            person_events = self.person_event_repository.get_by_id(person_id, event_id)

        result = []

        for relation in person_events:
            person = self.person_repository.get(relation.get_person_id())
            event = self.repository.get(relation.get_event_id())
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
            event_id = relation[0].get_id()
            try:
                occurence = EventController.find_dict2(occurences, event_id)
            except:
                occurences.append({
                    event_id: 0
                })
                occurence = occurences[-1]
            finally:
                occurence[event_id] += 1

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

    @staticmethod
    def find_dict2(array, id):
        '''
        Find dictionary with given id
        :param array:
        :param id:
        :return: dictionary
        :raise: ValueError if id is not found
        '''

        if not len(array):
            raise ValueError

        try:
            array[0][id]
            return array[0]
        finally:
            return find_dict2(array[1:], id)