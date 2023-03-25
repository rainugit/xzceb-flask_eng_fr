import unittest

from machinetranslation import translator

class testTranslator(unittest.TestCase):
    
    def test_frenchToEnglish(self):
        with self.assertRaises(ValueError):
            translator.french_to_english(None)

    def test_englishToFrench(self):
        with self.assertRaises(ValueError):
            translator.english_to_french(None)

    def test_TranslatetoEnglish(self):
        self.assertEqual(translator.french_to_english("Bonjour"),"Hello")

    def test_TranslatetoFrench(self):
        self.assertEqual(translator.english_to_french("Hello"),"Bonjour")

if __name__ == "__main__":
    unittest.main()