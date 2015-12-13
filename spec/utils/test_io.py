__author__ = 'Călin Sălăgean'

from utils.IO import IO
import unittest, os

class TestIO(unittest.TestCase):
    def test_instance(self):
        io = IO('person.json')
        self.assertIsInstance(io, IO)

    def test_validation(self):
        if os.path.exists(IO.filepath('test.json')):
            os.remove(IO.filepath('test.json'))

        with self.assertRaisesRegex(AttributeError, 'Please provide a valid file name!'):
            io = IO()

        io = IO('test.json')

        self.assertTrue(os.path.exists(IO.filepath('test.json')))

        os.remove(IO.filepath('test.json'))

    def test_read(self):
        file = open(IO.filepath('test.json'), 'w')
        file.write('1,2,3,,5')
        file.close()

        io = IO('test.json')
        with self.assertRaisesRegex(ValueError, 'The content of test.json is not valid!'):
            io.get()

        file = open(IO.filepath('test.json'), 'w')
        file.write('invalid json')
        file.close()

        io = IO('test.json')
        with self.assertRaisesRegex(ValueError, 'The content of test.json is not valid!'):
            io.get()

        file = open(IO.filepath('test.json'), 'w')
        file.write('[]')
        file.close()

        self.assertEqual(io.get(), [])

        os.remove(IO.filepath('test.json'))

    def test_set(self):
        file = open(IO.filepath('test.json'), 'w')
        file.close()

        io = IO('test.json')
        io.set('{"data":[{"a":1}]}')
        self.assertEqual(io.get(), '{"data":[{"a":1}]}')

        io.set(1)
        self.assertEqual(io.get(), 1)