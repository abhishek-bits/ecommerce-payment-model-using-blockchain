# Ref: https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class Customer:

    # to define attributes for this class
    def __init__(self, merchant_message: bytes, merchant_digital_signature: bytes):

        self._privateKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        self._publicKey = self._privateKey.public_key()

        self._msg = merchant_message
        self._dig_sign_1 = merchant_digital_signature
        self._dig_sign_2 = self._privateKey.sign(
            self._dig_sign_1,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

    # returns the message
    def get_message(self):
        return self._msg

    # returns the Digital Signature 1
    # this will be the Merchant's own signature
    def get_digital_signature_1(self):
        return self._dig_sign_1

    # returns the Digital Signature 2
    # this will be the Customer's signature over
    # the Merchant's signature.
    def get_digital_signature_2(self):
        return self._dig_sign_2

    # returns the public key
    def get_public_key(self):
        return self._publicKey

