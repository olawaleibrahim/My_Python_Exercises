import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 20
        result = main.do_stuff(test_param)
        self.assertEqual(result, 25)


unittest.main()

print(main)