import unittest
import vigenereCipher

class TestVigenereCipher(unittest.TestCase):
    message = "you were able to decode this? nice work!"
    coded_message = "dfc aruw fsti gr vjtwhr wznj? vmph otis!"
    keyword = "friends"

    def test_vigenere_decoder(self):
        self.assertEqual(vigenereCipher.vigenere_decoder(self.coded_message, self.keyword), self.message)
    
    def test_vigenere_coder(self):
        self.assertEqual(vigenereCipher.vigenere_coder(self.message, self.keyword), self.coded_message)


# Run tests
unittest.main()