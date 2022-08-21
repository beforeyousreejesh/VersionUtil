import unittest
import main.version_util as util

class VersionTestCase(unittest.TestCase):
    def test_compare_when_version1_is_greater_than_version2_return_one_1(self):
        result=util.compare('1.1','0.1')
        self.assertEqual(1,result)

    def test_compare_when_version1_is_less_than_version2_return_minue_one_1(self):
        result=util.compare('1.1','1.2')
        self.assertEqual(-1,result)

    def test_compare_when_version1_is_greater_than_version2_return_one_2(self):
        result=util.compare('1.2.9.9.9.9','1.2')
        self.assertEqual(1,result)

    def test_compare_when_version1_is_less_than_version2_return_minue_one_2(self):
        result=util.compare('1.2.9.9.9.9','1.3')
        self.assertEqual(-1,result)

    def test_compare_when_version1_is_greater_than_version2_return_one_3(self):
        result=util.compare('1.3.4','1.3')
        self.assertEqual(1,result)

    def test_compare_when_version1_is_less_than_version2_return_minue_one_3(self):
        result=util.compare('1.3.4','1.10')
        self.assertEqual(-1,result)

    def test_compare_when_version1_is_equal_to_version2_return_zero(self):
        result=util.compare('4.3.2','4.3.2')
        self.assertEqual(0,result)