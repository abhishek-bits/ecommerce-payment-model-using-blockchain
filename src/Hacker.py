def ModifyMessage(msg: bytes):
    _msg = msg[4:]
    return _msg


def ModifyDigitalSignature(digi_sign: bytes):
    # _digi_sign = digi_sign.decode('ASCII')
    _digi_sign = digi_sign[::2]
    return _digi_sign
