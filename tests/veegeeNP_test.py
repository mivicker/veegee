import unittest
import sys
sys.path.append('../')
import veegee.veegeeNP as veegeeNP

class TestSVGToNp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Test class was setup.")

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):

        with open('test_case.svg', 'r', encoding='utf-8') as f:
            self.test_file = f.read()

        with open('pathtest.txt', 'r', encoding='utf-8') as f:
            self.test_pathA = f.read()

        with open('path1test.txt', 'r', encoding='utf-8') as f:
            self.test_pathB = f.read()

    def test_list_elements(self):
        out_list = veegeeNP.list_elements(self.test_file)
        self.assertEqual(out_list, [self.test_pathA, self.test_pathB])


if __name__ == '__main__':
    unittest.main()
