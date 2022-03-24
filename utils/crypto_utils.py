import base64
import hashlib
from Cryptodome import Random
from Cryptodome.Cipher import AES


class CryptoUtils:
    def __init__(self, key, block_size=16, initial_vector_random_value=True):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.block_size = block_size
        self.pad = lambda s: s + (self.block_size - len(s.encode('utf-8')) % self.block_size) * chr(self.block_size - len(s.encode('utf-8')) % self.block_size)
        self.unpad = lambda s: s[0:-s[-1]]

        if initial_vector_random_value:
            self.initial_vector = Random.new().read(AES.block_size)
        else:
            self.initial_vector = bytes(key[:16], encoding='utf-8')

    def encrypt(self, plain) -> bytes:
        """

        Returns:
            object: 
        """
        raw = self.pad(plain)

        return base64.b64encode(self.initial_vector + AES.new(self.key, AES.MODE_CBC, self.initial_vector).encrypt(raw.encode('utf-8')))

    def encrypt_str(self, plain) -> str:

        return self.encrypt(plain).decode('utf-8')

    def decrypt(self, cipher):
        enc = base64.b64decode(cipher)
        initial_vector = enc[:16]

        return self.unpad(AES.new(self.key, AES.MODE_CBC, initial_vector).decrypt(enc[16:]))

    def decrypt_str(self, cipher) -> str:
        if isinstance(cipher, str):
            cipher = str.encode(cipher)

        return self.decrypt(cipher).decode('utf-8')
