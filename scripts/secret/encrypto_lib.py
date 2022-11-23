#!/usr/bin/python3

def encrypto(plaintext,bias):
    plaintext_list=list(plaintext)
    plainnumber_list=[ord(char) for char in plaintext_list]
    plainnumber_bias_list=[num+bias for num in plainnumber_list]
    ciphertext_list=[chr(num) for num in plainnumber_bias_list]
    ciphertext=''.join(ciphertext_list)
    return ciphertext
def unencrypto(ciphertext,bias):
    ciphertext_list=list(ciphertext)
    ciphernumber_list=[ord(char) for char in ciphertext_list]
    ciphernumber_bias_list=[num-bias for num in ciphernumber_list]
    plaintext_list=[chr(num) for num in ciphernumber_bias_list]
    plaintext=''.join(plaintext_list)
    return plaintext
if __name__=='__main__':
    print('加密模块正在运行\n')
else:
    print('加密模块被导入\n')

