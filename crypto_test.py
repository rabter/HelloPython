from utils.crypto_utils import CryptoUtils


class TestCrypto:
    def test_encrypt(self):
        key = 'hellopythonsecretvalue'
        login_id = 'foobar'

        crypto_utils = CryptoUtils(key, initial_vector_random_value=False)
        encrypt_login_id = crypto_utils.encrypt_str(login_id)

        print(f'{encrypt_login_id}')

    def test_decrypt(self):
        key = 'hellopythonsecretvalue'
        login_id = 'aGVsbG9weXRob25zZWNyZcXZlqWh1OQNga8ZCb+9LTo='

        crypto_utils = CryptoUtils(key, initial_vector_random_value=False)
        decrypt_login_id = crypto_utils.decrypt_str(login_id)

        print(f'{decrypt_login_id}')
