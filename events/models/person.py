__author__ = 'Călin Sălăgean'

class Person():
    __id_class = 0

    def __init__(self, first_name = None, last_name = None, address = None, id = None):
        '''
        Person class constructor

        :param name:
        :param address:
        :param event:
        :return: Class instance
        '''
        self.validate(first_name, last_name, address)
        self.__first_name, self.__last_name, self.__address = first_name, last_name, address
        self.__id = self.__set_id(id)

    @staticmethod
    def validate(first_name, last_name, address):
        '''
        Validation method for Person class

        :param name:
        :param address:
        :param event:
        :return: None
        :raise AttributeError:
        '''
        if not first_name or not last_name:
            raise AttributeError("Please provide full name")
        if not address:
            raise AttributeError("Please provide an address")

        # TODO: Implement validating existing events

    def __set_id(self, id):
        '''
        Increments the class _id attribute
        :param id:
        :return: None
        '''
        if id is None:
            instance_id = Person.__id_class
        else:
            instance_id = id
        Person.__id_class += 1
        return instance_id

    def get_id(self):
        '''
        Returns person ID
        :return id:
        '''
        return self.__id

    def get_name(self):
        '''
        Returns person name
        :return name:
        '''
        return self.__first_name + ' ' + self.__last_name

    def get_address(self):
        '''
        Returns person address
        :return address:
        '''
        return self.__address

    def update(self, first_name = None, last_name = None, address = None):
        '''
        Update person instance attributes
        :param first_name:
        :param last_name:
        :param address:
        :return: None
        '''
        if first_name is None:
            first_name = self.__first_name
        if last_name is None:
            last_name = self.__last_name
        if address is None:
            address = self.__address

        self.validate(first_name, last_name, address)
        self.__first_name, self.__last_name, self.__address = first_name, last_name, address

    def get_serialization(self):
        '''
        Return JSON serialization
        :return: JSON Object
        '''
        dict = {
            'id': self.__id,
            'first_name': self.__first_name,
            'last_name': self.__last_name,
            'address': self.__address,
        }

        return dict

    @staticmethod
    def set_class_id(id):
        '''
        Set class _id attribute
        :param id:
        :return: None
        '''
        Person.__id_class = id