import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-email-check" in j:
            exec("".join(i['source']))


class testCases(unittest.TestCase):

    def testBadEmail(self):
      test1 = not emailCheck("stump_truck@gmail.com")
      test2 = not emailCheck("7tumptruck@aalto.fi")
      test3 = not emailCheck("stumptruckhappy2.org")
      test4 = not emailCheck("stumptruck@happy2org")

      self.assertTrue(test1 & test2 & test3 & test4, "Your code failed to detect all of the bad email addresses tested.")

    def testGoodEmail(self):
      test1 = emailCheck("stumptruck@gmail.com")
      test2 = emailCheck("7tumptruck@wsu.edu")
      test3 = emailCheck("stumptruck@happy2.org")

      self.assertTrue(test1 & test2 & test3, "Your code failed to validate all of the good emails tested.")