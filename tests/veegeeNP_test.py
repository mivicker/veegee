import unittest
import sys
import numpy as np
sys.path.append('../')
import veegee.veegeeNP as veegeeNP

class TestSVGToNp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):

        with open('test_case.svg', 'r', encoding='utf-8') as f:
            self.test_file = f.read()

        with open('pathtest.txt', 'r', encoding='utf-8') as f:
            self.test_pathA = f.read().strip()

        with open('path1test.txt', 'r', encoding='utf-8') as f:
            self.test_pathB = f.read().strip()

        self.test_commands = ['m', 'c', 'C']
        self.test_points = ['90.714276,176.04758', '0,0', '-30.994041,-6.80357', '-32.505944,-31.74999', '56.696426,119.35116', '209.39879,148.8333', '168.57736,58.874994', '127.75594,-31.083336', '52.916665,25.613092', '52.916665,25.613092']

    def test_list_elements(self):
        out_list = veegeeNP.list_elements(self.test_file)
        for ele, ment in zip(out_list, [self.test_pathA, self.test_pathB]):
            self.assertEqual(ele, ment)

    def test_extract_dstring(self):
        dstring = veegeeNP.extract_dstring(self.test_pathB)
        test_dstring = "m 9.8273803,98.184493 c 0,0 9.8273787,-40.821406 47.6249987,-46.869023 37.797604,-6.047618 58.208321,28.726172 37.797604,32.505932 -20.410698,3.779757 -74.083319,27.970228 -58.96427,56.696418 15.119045,28.72619 47.624999,49.13691 47.624999,49.13691"
        self.assertEqual(test_dstring, dstring)

    def test_split_commands_points(self):
        commands, points = veegeeNP.split_commands_points(self.test_pathA)
        self.assertEqual(commands, self.test_commands)
        self.assertEqual(points, self.test_points)

    def test_points_to_numpy(self):
        array = veegeeNP.points_to_numpy(self.test_points)
        test_array = np.array([[90.714276,176.04758],
                               [0,0],
                               [-30.994041,-6.80357],
                               [-32.505944,-31.74999],
                               [56.696426,119.35116],
                               [209.39879,148.8333],
                               [168.57736,58.874994],
                               [127.75594,-31.083336],
                               [52.916665,25.613092],
                               [52.916665,25.613092]])
        self.assertTrue(np.array_equal(array, test_array))

if __name__ == '__main__':
    unittest.main()
