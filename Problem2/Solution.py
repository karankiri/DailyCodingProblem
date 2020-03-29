import unittest

def ArrayMultiplication(list):
  resultList = []
  for i in range(len(list)):
    multiplication = 1
    for j in range(len(list)):
      if i!=j:
        multiplication = multiplication * list[j]
    resultList.append(multiplication)
  return resultList

class Test(unittest.TestCase):
    def test_return_true_if_multiplication(self):
        result = ArrayMultiplication([2, 3, 1])
        self.assertListEqual(result, [3, 2, 6])
    def test_return_true_if_multiplication_with_zero(self):
        result = ArrayMultiplication([2, 0, 5])
        self.assertListEqual(result, [0, 10, 0])

   


unittest.main(verbosity=2)