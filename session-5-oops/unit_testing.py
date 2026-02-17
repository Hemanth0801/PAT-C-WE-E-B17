# unit testing is a technique used for testing a block of code with different paramater.

# Arrange -> set up data set
# Act -> Execute peace of code with the prepared data set
# Assert -> comparing expected and actual result

# You developed one test case -> Login functionality -> Multiple combination of data

# get locator of url
# enter username -> combination of username-> valid/in value -> leng should not 20 charact ->
# enter password -> valid/invalid
# click on login


import unittest
def add(a,b):
    return a+b
class Testcase1(unittest.TestCase):
    def test1(self):
        self.assertEqual(add(1,2), 3)
    def test2(self):
        self.assertEqual(add(10,20), 30)
    def test3(self):
        self.assertEqual(add(10,30), 50)