# Ref: https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/

import cryptography.exceptions
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey


class Blockchain:

    def __init__(self, message: bytes, digital_signature_1: bytes, digital_signature_2: bytes,
                 merchant_public_key: RSAPublicKey, customer_public_key: RSAPublicKey):

        self._blockchain_state = BlockchainState()

        # Message Verification Step 1
        # with Customer's Public Key verify that
        # Digital Signature 1 is Authentic

        try:
            customer_public_key.verify(
                digital_signature_2,  # signature
                digital_signature_1,  # message
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )

            self._blockchain_state.has_valid_digital_signature_1 = True

            # Message Verification Step 2
            # with Merchant's Public Key verify that
            # the Message is Authentic

            try:
                merchant_public_key.verify(
                    digital_signature_1,  # signature
                    message,  # message
                    padding.PSS(
                        mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH
                    ),
                    hashes.SHA256()
                )

                self._blockchain_state.has_valid_message = True

            except cryptography.exceptions.InvalidSignature as e:
                print('\nMerchant Message Verification Failure!')

        except cryptography.exceptions.InvalidSignature as e:
            print('\nCustomer Digital Signature Verification Failure!')

    def is_valid(self):
        if self._blockchain_state.has_valid_digital_signature_1 and self._blockchain_state.has_valid_message:
            return True
        return False


# a structure representing blockchain state
class BlockchainState:
    def __init__(self):
        self.has_valid_digital_signature_1 = False
        self.has_valid_message = False
