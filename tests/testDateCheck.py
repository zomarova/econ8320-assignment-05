import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-date-check" in j:
            exec("".join(i['source']))


class testCases(unittest.TestCase):

    def testBadDates(self): 
      date1 = not dateCheck("32-01-2018")
      date2 = not dateCheck("31-13-2020")
      date3 = not dateCheck("01-01-2010a")

      self.assertTrue(date1 & date2 & date3, "Your code failed to detect all of the bad dates tested.")

    def testGoodDates(self):
      date1 = dateCheck("13-01-2018")
      date2 = dateCheck("31-12-2020")

      self.assertTrue(bool(date1) & bool(date2), "Your code failed to validate the good dates tested.")

    