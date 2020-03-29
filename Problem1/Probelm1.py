import unittest

def TwoNumbersEqual(list, value):
  is_sum_exist = False
  for i in range(len(list)):
    for j in range(len(list)):
      if(list[i] + list[j] == value and i != j):
        is_sum_exist = True
  return is_sum_exist


class Test(unittest.TestCase):

    def test_return_true_if_sum_exists(self):
        result = TwoNumbersEqual([10, 15, 3, 7], 17)
        self.assertTrue(result)
    def test_return_false_if_sum_dont_exists(self):
        result = TwoNumbersEqual([10, 15, 3, 7], 19)
        self.assertFalse(result)
    def test_if_empty_array_handled(self):
        result = TwoNumbersEqual([], 19)
        self.assertFalse(result)
    


unittest.main(verbosity=2)