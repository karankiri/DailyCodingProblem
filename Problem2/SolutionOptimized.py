import unittest

def ArrayMultiplication(list):
  multiplication = 1
  multiplicationWithoutZero = 1
  zeroCount = 0
  for item in list:
    if item == 0:
      zeroCount = zeroCount + 1
    else:
      multiplicationWithoutZero = item * multiplicationWithoutZero
    multiplication = item * multiplication
  if zeroCount > 1:
    return [0] * len(list)
  elif zeroCount == 1:
    for i in range(len(list)):
      if(list[i] == 0):
        list[i] = multiplicationWithoutZero
      else:
        list[i] = 0
  else:
    for i in range(len(list)):
      list[i] = multiplication / list[i]
  return list

class Test(unittest.TestCase):
    def test_return_true_if_multiplication(self):
        result = ArrayMultiplication([2, 3, 1])
        self.assertListEqual(result, [3, 2, 6])
    def test_return_true_if_multiplication_with_zero(self):
        result = ArrayMultiplication([2, 0, 5])
        self.assertListEqual(result, [0, 10, 0])
    def test_return_true_if_multiplication_with_multiple_zero(self):
        result = ArrayMultiplication([2, 0, 5, 0])
        self.assertListEqual(result, [0, 0, 0, 0])

   


unittest.main(verbosity=2)