# Ref: https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class Merchant:

    # to define attributes for this class
    def __init__(self, merchant_id, amount, transaction_time, transaction_id):

        self._privateKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        self._publicKey = self._privateKey.public_key()

        # convert string message to a byte object
        self._msg = (str(merchant_id) + str(amount) + str(transaction_time) + str(transaction_id)).encode('ASCII')

        # create digital signature
        self._signature = self._privateKey.sign(
            self._msg,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

    # returns the message
    def get_message(self):
        return self._msg

    # returns the digital signature
    def get_digital_signature(self):
        return self._signature

    # returns the public key
    def get_public_key(self):
        return self._publicKey
