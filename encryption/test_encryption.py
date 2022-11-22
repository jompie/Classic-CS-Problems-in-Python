import unittest
import encryption

class TestEncryption(unittest.TestCase):
    def test_encryption(self):
        key1, key2 = encryption.encrypt("Top Secret!")
        self.assertNotEqual(key1, "Top Secret!")
        self.assertNotEqual(key2, "Top Secret!")
        self.assertEqual(encryption.decrypt(key1, key2), "Top Secret!")


if __name__ == "__main__":
    unittest.main()
