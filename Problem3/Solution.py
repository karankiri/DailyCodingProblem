import unittest
import re
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def serialize(node):
  if(node == None):
    return ""
  leftString = ""
  rightString = ""
  valString = "{val:"+ node.val
  if(node.left):
    leftString = ",left:" + serialize(node.left)
  if(node.right):
    rightString = ",right:" +serialize(node.right) 
  return valString + leftString + rightString + "}"

def deserialize(string):
  print(string)
  p = re.compile('{val:(.*)')
  print(p.match(string).groups())
  return string

class Test(unittest.TestCase):
  def test_return_true_if_multiplication(self):
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
   


unittest.main(verbosity=2)