import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-favorite" in j:
            codelist = i['source']
            for k in range(len(codelist)):
                if ("input_string" in codelist[k]):
                    codelist[k] = 'input_string = "My favorite number is 12."\n'
                    exec("".join(codelist))
                else:
                    codelist = ['input_string = "My favorite number is 12."\n'] + codelist
                    exec("".join(codelist))



class testCases(unittest.TestCase):

    def testSingleDigit(self): 

      self.assertTrue(bool(hasNumber)==False, "There is a double digit number in this string, \nso the result of your regex should be False!")
