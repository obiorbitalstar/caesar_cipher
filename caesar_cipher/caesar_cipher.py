import nltk

def encrypt(text, key):
    """
    A method to encrypt some string ( takes in some text and applies the key on it )
    """
    text = text.upper()
    cipher = ""

    for letter in text:
        if letter.isalpha()==True:
            shifted = ord(letter) + key
            if shifted < 65:
                shifted += 26
            if shifted > 90:
                shifted -= 26
            cipher += chr(shifted)
        else:
           cipher+= " "
    return cipher

def decrypt(text,key):
    """ A method to decrypt if u know the key """
    return encrypt(text,-key)


print (encrypt("MOLLZY,ABC", 1))
print (decrypt("NPMMAZ BCD", 1))
#------------------- demo

nltk.download('words')
jomleh = 'this is an english sentence try it out'
print(jomleh)
list_of_sentences=[]
for i in range(1,27):

       list_of_sentences.append(encrypt(jomleh,i))


original_words_list = nltk.corpus.words.words()
words_list = [word.lower() for word in original_words_list]

# For any given sentence, how many english words are there?
def count_words(sentence):
    sentence_words = sentence.split()
    en_word_count = 0

    for word in sentence_words:
        if word.lower() in words_list:
            en_word_count += 1

    return en_word_count

def most_likely(sentences):
    _max = 0
    _max_sentence = ''

    for sentence in sentences:
        if count_words(sentence) > _max:
            _max_sentence = sentence
            _max = count_words(sentence)
    return _max_sentence

# Go over the list of sentences list and count the number of each correct english word inisde it
# theh one with the most english word in it is the one to be most likly a dycribted one (without the key)

for i in range(len(list_of_sentences)):
    print(count_words(list_of_sentences[i]))

print(most_likely(list_of_sentences))
