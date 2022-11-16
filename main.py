# Blockchain based Payment Authentication System

from src.Blockchain import Blockchain
from src.Customer import Customer
from src.Hacker import ModifyMessage, ModifyDigitalSignature
from src.Merchant import Merchant


def main():

    # STEP 1:
    # Merchant signs the message
    # creates the digital signature 1

    merchant_id = 'bits'
    amount = 100
    transaction_time = '12:15 PM'
    transaction_id = '001'

    merchant = Merchant(merchant_id, amount, transaction_time, transaction_id)

    merchant_public_key = merchant.get_public_key()
    merchant_message = merchant.get_message()
    merchant_digital_signature = merchant.get_digital_signature()

    print('\nMerchant Details:-')
    print('Public Key = ', merchant_public_key)
    print('Message = ', merchant_message)
    print('Digital Signature = ', merchant_digital_signature)

    # ************* Hacker sits between Merchant and Customer ***************
    # hacker tampers the message
    # merchant_message = ModifyMessage(merchant_message)
    # hacker tampers the digital signature
    # merchant_digital_signature = ModifyDigitalSignature(merchant_digital_signature)
    # ************************************************************************

    # STEP 2:
    # Customer signs the digital signature 1
    # creates the digital signature 2

    customer = Customer(merchant_message, merchant_digital_signature)

    customer_public_key = customer.get_public_key()
    customer_message = customer.get_message()
    customer_digital_signature_1 = customer.get_digital_signature_1()
    customer_digital_signature_2 = customer.get_digital_signature_2()

    print('\nCustomer Details:-')
    print('Public Key = ', customer_public_key)
    print('Message = ', customer_message)
    print('Digital Signature 1 = ', customer_digital_signature_1)
    print('Digital Signature 2 = ', customer_digital_signature_2)

    # ********** Hacker sits between Customer and Blockchain System ***********
    # hacker tampers the message
    # customer_message = ModifyMessage(customer_message)
    # hacker tampers the digital signature 1
    # customer_digital_signature_1 = ModifyDigitalSignature(customer_digital_signature_1)
    # hacker tampers the digital signature 2
    # customer_digital_signature_2 = ModifyDigitalSignature(customer_digital_signature_2)
    # *************************************************************************

    # STEP 3:
    # Blockchain System verifies the transaction.
    blockchain = Blockchain(customer_message, customer_digital_signature_1, customer_digital_signature_2, merchant_public_key, customer_public_key)

    print('\nBlockchain Output:-')
    if blockchain.is_valid():
        print('VALID Blockchain')
    else:
        print('INVALID Blockchain')


if __name__ == '__main__':
    main()
