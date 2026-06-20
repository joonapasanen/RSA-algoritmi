import unittest
from unittest.mock import patch
from io import StringIO
from rsa import generate_keys
from main import message_interface

class TestMessageInterface(unittest.TestCase):
    def setUp(self):
        self.public_key, self.private_key = generate_keys()

    def test_end_to_end(self):
        plain_message = "This is a test message"
        
        d = self.private_key[1]

        inputs = ["", "s", plain_message, "r", str(d), "q"]

        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=StringIO) as output:
            message_interface(self.public_key, self.private_key)

        # output tallentaa kaiken stdout:iin tulostetun tekstin, joten käytetään assertIn, eikä assertEqual
        self.assertIn(plain_message, output.getvalue())
