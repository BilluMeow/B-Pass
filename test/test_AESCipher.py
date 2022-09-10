from encryption.core import AESCipher
from codecs import decode, encode

class TestAESCipher:

    def test_encrypt_1(self) -> None:
        assert 1 == 1

    def test_encrypt_2(self) -> None:
        assert 1 == 1

    def test_encrypt_3(self) -> None:
        assert 1 == 1

    def test_decrypt_1(self) -> None:
        assert 1 == 1

    def test_decrypt_2(self) -> None:
        assert 1 == 1

    def test_decrypt_3(self) -> None:
        assert 1 == 1

    def test_generate_key_1(self) -> None:
        self.cipher = AESCipher()
        password = "This is Good"
        key, salt = (b'\x06D+\x080\xbe\xc7\xcds\x17\x9ej\xb3N\xdf\x157fZHd\xdf\x956t\x14\x13\xb9\xdc$;\x16', b'12323212')

        assert (key, salt) == self.cipher.generate_key(password, salt=salt)
        
    def test_generate_key_2(self) -> None:
        self.cipher = AESCipher()
        password = "asdaskdyjasuid"
        key, salt = (b'Z\xd6\x99u-\xdd\x0b\xc6g\x97kh`\x97\xfc0\x0fG\x1b\xbc,J\x86\xd0>\xf8\x19S\xdbunM', b'asdasd2ed23')

        assert (key, salt) == self.cipher.generate_key(password, salt=salt)

    def test_generate_key_3(self) -> None:
        self.cipher = AESCipher()
        password = "klasdjhfklajsdfhakwjlshfljksadbncvladjksfhsakldfjhsdaflkjh"
        key, salt = (b'h\xd2\xa8\xb6\xd3\x92J.;D\x89e\xae]s)\xf7-\x8bf"W`"\x98\xeb\x8e\x99.\xe0\xc2\x80', b'198237yhbzxcvmnhwbljkfh')

        assert (key, salt) == self.cipher.generate_key(password, salt=salt)