import unittest

from translator import englishToFrench,frenchToEnglish 

class TestEnglishToFrench (unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertEqual(englishToFrench('1'),'1')
        self.assertEqual(englishToFrench(''),'')
        self.assertEqual(englishToFrench(None),'')

class TestFrenchToEnglish (unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(frenchToEnglish('1'),'1')
        self.assertEqual(frenchToEnglish(''),'')
        self.assertEqual(frenchToEnglish(None),'')


unittest.main()


