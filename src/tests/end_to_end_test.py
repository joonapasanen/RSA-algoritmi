import unittest
from rsa import generate_keys, encrypt_message, decrypt_message


class TestEndToEnd(unittest.TestCase):
    def setUp(self):
        self.public_key, self.private_key = generate_keys()

    def test_short_message(self):
        message = "lyhyt viesti"
        message_ints = int.from_bytes(message.encode())
        encrypted = encrypt_message(message_ints, self.public_key)
        decrypted = decrypt_message(encrypted, self.private_key)
        bytes_len = (decrypted.bit_length() + 7) // 8
        result = decrypted.to_bytes(bytes_len).decode()
        self.assertEqual(message, result)

    def test_long_message(self):
        message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam hendrerit nisi sed sollicitudin pellentesque." \
        "Nunc posuere purus rhoncus pulvinar aliquam. Ut aliquet tristique nisl vitae volutpat. Nulla aliquet porttitor venenatis."
        message_ints = int.from_bytes(message.encode())
        encrypted = encrypt_message(message_ints, self.public_key)
        decrypted = decrypt_message(encrypted, self.private_key)
        bytes_len = (decrypted.bit_length() + 7) // 8
        result = decrypted.to_bytes(bytes_len).decode()
        self.assertEqual(message, result)

    def test_non_ascii(self):
        message = "ääkköset eli åäö"
        message_ints = int.from_bytes(message.encode())
        encrypted = encrypt_message(message_ints, self.public_key)
        decrypted = decrypt_message(encrypted, self.private_key)
        bytes_len = (decrypted.bit_length() + 7) // 8
        result = decrypted.to_bytes(bytes_len).decode()
        self.assertEqual(message, result)
