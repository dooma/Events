__author__ = 'Călin Sălăgean'

import os, json

class IO():
    def __init__(self, filename = None):
        '''
        IO Constructor
        :param filename: Default None
        :return: object
        '''
        self.validate(filename)

        self.__filename = filename

    def get(self):
        '''
        Returns parsed file content
        :return: dictionary
        :raise: ValueError if content is invalid
        '''
        file = open(IO.filepath(self.__filename))
        try:
            content = json.loads(file.read())
            return content
        except:
            raise ValueError('The content of ' + self.__filename + ' is not valid!')
        finally:
            file.close()

    def set(self, data):
        '''
        Writes data into file as JSON content
        :param data: dictionary (JSON format)
        :return: None
        '''
        temporary_file_prefix = 'tmp_'

        temporary_file = open(IO.filepath(temporary_file_prefix + self.__filename), 'w')
        json.dump(data, temporary_file)
        temporary_file.close()

        if temporary_file.closed:
            os.remove(IO.filepath(self.__filename))
            os.rename(temporary_file.name, IO.filepath(self.__filename))

    @staticmethod
    def filepath(filename):
        '''
        Static method that creates relative path for given filename
        :param filename:
        :return: string
        '''
        data_directory = 'data/'
        return os.path.abspath(data_directory + filename)

    @staticmethod
    def validate(filename):
        '''
        Validates filename. If file does not exist, it will create the file
        :param filename:
        :return:
        :raise: AttributeError if filename is invalid
        '''
        if filename == None or not len(str(filename)) or filename.split('.')[1] != 'json':
            raise AttributeError('Please provide a valid file name!')

        if not os.path.exists(IO.filepath(filename)):
            open(IO.filepath(filename), 'w')