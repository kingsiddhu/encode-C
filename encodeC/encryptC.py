#The Encryptor used in https://github.com/kingsiddhu/Encrypt
def Encrypt(phrase, NumOfTimes=1):
    """
    This Encrypts your phrase
    """
    before = r"""qwertyuiopasdfghjklzxcvbnm1234567890`-=]£;',./ QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()~_+{}|:"<>?"""
    afters = r"""ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+`1234567890-=ABCDEFGHIJKLMNOPQRSTUVWXYZ{}|:"<>? ,./;'[]"""
    encrypt = ''
    for en in phrase:
        if en == "\n":
            encrypt = encrypt + "\n"
        elif before.find(en) == -1:
            encrypt = encrypt + en
        else:
            encrypt = encrypt + afters[before.find(en)]
    return encrypt


#The Decryptor used in https://github.com/kingsiddhu/Encrypt
def Decrypt(phrase):
    """
    This Decrypts your phrase
    """
    before = r"""qwertyuiopasdfghjklzxcvbnm1234567890`-=]£;',./ QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()~_+{}|:"<>?"""
    afters = r"""ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+`1234567890-=ABCDEFGHIJKLMNOPQRSTUVWXYZ{}|:"<>? ,./;'[]"""
    encrypt = ""
    for en in phrase:
        if en == "\n":
            encrypt = encrypt + "\n"
        elif before.find(en) == -1:
            encrypt = encrypt + en
        else:
            encrypt = encrypt + before[afters.find(en)]
    return encrypt
