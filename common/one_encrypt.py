from Crypto.Cipher import AES
# key = b'abcdefgh'

#加密内容需要长达16位字符，所以进行空格拼接
def pad(text):
    # str to byte
    text = str.encode(text)
    while len(text) % 16 != 0:
        text += b' '
    return text

#加密秘钥需要长达16位字符，所以进行空格拼接
def pad_key(key):
    # str to byte
    key = str.encode(key)
    while len(key) % 16 != 0:
        key += b' '
    return key

def encrypt(text, key):
    aes = AES.new(pad_key(key), AES.MODE_ECB)
    return aes.encrypt(pad(text))

def decrypt(text, key):
    aes = AES.new(pad_key(key), AES.MODE_ECB)
    return str(aes.decrypt(text),encoding='utf-8',errors="ignore")

if __name__ == "__main__":
    key = '123456'
    text = '<your private key>'
    result = encrypt(text, key)
    print(encrypt(text, key))
    print(decrypt(result, key))
