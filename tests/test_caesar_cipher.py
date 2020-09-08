from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt,decrypt,count_words,most_likely

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
    actual = encrypt('MOLLZY ABC',1)
    expected = 'NPMMAZ BCD'
    assert expected == actual
def test_decrypte():
    actual = decrypt('NPMMAZ BCD',1)
    expected ='MOLLZY ABC'
    assert expected == actual

def test_upper_and_lower_case_encyption():
    actual = encrypt('AbC',1)
    expected = 'BCD'
    assert expected == actual
def test_encrypt_with_non_alpha():
    actual = encrypt('A B,C',1)
    expected = 'B C D'
    assert expected == actual

def test_decrypte_without_key():

    sentence = 'It was the best of times, it was the worst of times.'
    sentences_list=[]
    for i in range(1,27):
            sentences_list.append(encrypt(sentence, i))

    for i in range(len(sentences_list)):
            print(count_words(sentences_list[i]))

    assert most_likely(sentences_list)=="it was the best of times  it was the worst of times ".upper()
