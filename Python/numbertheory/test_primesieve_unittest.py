
"""Tests for primesieve module."""

import primesieve
import unittest
import numbthy
import random

class Test_primesieve(unittest.TestCase):

    # def assert_array_equal(have, want):
    #     """Convert array to list and compare to desired output."""
    #     assert list(have) == want


    """Test count_primes function."""
    def test_count_primes(self):
        for testcase1 in ((100,25),(10**6,78498),(10**10,455052511)):
             self.assertEqual(primesieve.count_primes(testcase1[0]),testcase1[1])

        for testcase2 in (((100, 10**6),78473),((10**9, 10**10),404204977)):
             self.assertEqual(primesieve.count_primes(testcase2[0][0],testcase2[0][1]),testcase2[1])
    
    def test_nth_prime(self):
        for testcase1 in ((25,97),(26,101),(10**8,2038074743)):
            self.assertEqual(primesieve.nth_prime(testcase1[0]),testcase1[1])
            
        for testcase2 in (((1, 100),101),((100, 1000000),1001311)):
            self.assertEqual(primesieve.nth_prime(testcase2[0][0],testcase2[0][1]),testcase2[1])
    
            
        
        
    # def test_nth_prime():
    #     """Test nth prime function."""
    #     assert primesieve.nth_prime(25) == 97
    #     assert primesieve.nth_prime(26) == 101
    #     assert primesieve.nth_prime(1, 100) == 101
    #     assert primesieve.nth_prime(100, 1000000) == 1001311
    #     assert primesieve.nth_prime(10**8) == 2038074743


    # def test_iterator():
    #     """Test iterator."""
    #     it = primesieve.Iterator()
    #     assert it.next_prime() == 2
    #     assert it.next_prime() == 3
    #     assert it.next_prime() == 5
    #     assert it.next_prime() == 7
    #     assert it.next_prime() == 11
    #     assert it.next_prime() == 13
    #     assert it.prev_prime() == 11
    #     assert it.prev_prime() == 7
    #     assert it.prev_prime() == 5
    #     assert it.prev_prime() == 3
    #     assert it.prev_prime() == 2
    #     assert it.prev_prime() == 0


    # def test_primes_array():
    #     """Test primes array output."""
    #     assert_array_equal(primesieve.primes(10), [2, 3, 5, 7])
    #     assert_array_equal(primesieve.primes(10, 20), [11, 13, 17, 19])


    # def test_n_primes_array():
    #     """Test n_primes array output."""
    #     assert_array_equal(primesieve.n_primes(7),
    #                     [2, 3, 5, 7, 11, 13, 17])
    #     assert_array_equal(primesieve.n_primes(5, 100), [101, 103, 107, 109, 113])