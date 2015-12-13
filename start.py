__author__ = 'Călin Sălăgean'

from events.controllers.event import EventController
from events.controllers.person import PersonController

class Menu():

    text = """
        1. Adaugare persoana
        2. Afisare persoane
        3. Afisare persoana selectata
        4. Stergere persaoana
        5. Editare persoana
        6. Inscriere persoana la eveniment
        7. Adaugare eveniment
        8. Afisare evenimente
        9. Afisare eveniment selectat
        10. Sterge eveniment
        11. Editare eveniment

        12. Cautare persoane
        13. Cautare evenimente

        14. Lista de evenimente dupa persoana
        15. Lista de persoane inscrise la evenimente ordonate dupa numarul de evenimente
        16. Listeaza primele 20% evenimente importante

        (Alta tasta). Iesire
    """

    def __init__(self):
        self.menu_text = Menu.text
        self.person_controller = PersonController()
        self.event_controller = EventController()
        self.command_menu = {
            '1': self.add_person,
            '2': self.show_all_persons,
            '3': self.show_person,
            '4': self.delete_person,
            '5': self.edit_person,
            '6': self.associate_person,
            '7': self.add_event,
            '8': self.show_all_events,
            '9': self.show_event,
            '10': self.delete_event,
            '11': self.edit_event,
            '12': self.search_people,
            '13': self.search_events,
            '14': self.events_list_by_person,
            '15': self.people_most_events,
            '16': self.get_top_events
        }

    def print_menu(self):
        print(self.menu_text)

    def execute_command(self):
        self.print_menu()
        command = input("Introduceti comanda ")
        try:
            self.command_menu[command]()
            self.execute_command()
        except:
            print("Iesire")

    def add_person(self):
        first_name = input("Introduceti prenume ")
        last_name = input("Introduceti nume de familie ")
        address = input("Introduceti adresa ")
        print(self.person_controller.insert(first_name, last_name, address))

    def show_all_persons(self):
        print(self.person_controller.index())

    def show_person(self):
        id = input("Introduceti id-ul ")
        print(self.person_controller.show(id))

    def delete_person(self):
        id = input("Introduceti id-ul ")
        print(self.person_controller.delete(id))

    def edit_person(self):
        id = input("Introduceti id-ul ")

        first_name = input("Introduceti prenume ")
        last_name = input("Introduceti nume de familie ")
        address = input("Introduceti adresa ")

        print(self.person_controller.update(id, first_name, last_name, address))

    def associate_person(self):
        person_id = input("Introduceti ID persoana ")
        event_id = input("Introduceti ID event ")
        data = input("Introduceti data ")

        print(self.person_controller.associate(person_id, event_id, data))

    def add_event(self):
        date = input("Introduceti data ")
        time = input("Introduceti ora ")
        description = input("Introduceti descriere ")

        print(self.event_controller.insert(date, time, description))

    def show_event(self):
        id = input("Introduceti id-ul ")
        print(self.event_controller.show(id))

    def show_all_events(self):
        print(self.event_controller.index())

    def delete_event(self):
        id = input("Introduceti id-ul ")

        print(self.event_controller.delete(id))

    def edit_event(self):
        id = input("Introduceti id-ul ")

        date = input("Introduceti data ")
        time = input("Introduceti ora ")
        description = input("Introduceti descriere ")

        print(self.event_controller.update(id, date, time, description))

    def search_people(self):
        term = input("Introduceti termenul de cautare ")
        print(self.person_controller.search(term))

    def search_events(self):
        term = input("Introduceti termenul de cautare ")
        print(self.event_controller.search(term))

    def events_list_by_person(self):
        person_id = input("Introduceti ID ")
        print(self.person_controller.get_events(person_id))

    def people_most_events(self):
        print(self.person_controller.get_top_persons())

    def get_top_events(self):
        print(self.event_controller.get_top_events())

menu = Menu()
menu.execute_command()