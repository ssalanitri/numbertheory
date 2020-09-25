
"""Tests for primesieve module."""

import primesieve
import unittest
import numbthy
import random
from nnumbers import Triangular

class Test_nnumbers(unittest.TestCase):

    # def assert_array_equal(have, want):
    #     """Convert array to list and compare to desired output."""
    #     assert list(have) == want

    def test_getTriangular(self):
        triang = Triangular()
        for testcase in ((3,6),(4,10),(5,15),(6,21)):
            self.assertEqual(testcase[1],Triangular.getTriangular(self,testcase[0]))
            
    def test_isTriangular(self):
        triang = Triangular()
        for testcase in (3,6,10,15,21):
            self.assertEqual(True,Triangular.isTriangular(self,testcasei98u))
  
  