import math
import string

def establish_vocab(text1, text2):
    appended_string = text1 + " " + text2
    unique_words = set(appended_string.split())
    vocab_to_int = {word: ii for ii, word in enumerate(unique_words)}
    return vocab_to_int

def tokenize_string(vocab_to_int, text):
    token_array = [0] * len(vocab_to_int.keys())
    for word in text.split():
        token_array[vocab_to_int[word]] += 1
    return token_array

def dot_product(arr1, arr2):
    return sum(a*b for a,b in zip(arr1,arr2))

def cosine_simularity(arr1, arr2):
    dp = dot_product(arr1, arr2)
    return dp / (math.sqrt(sum([i*i for i in arr1])) * math.sqrt(sum([i*i for i in arr1])))


if __name__ == "__main__":

    try:
        fText1 = open('text1.txt', 'r')
        text1 = fText1.read()
    except:
        print("could not open the text1.txt, please be sure file still exists")
        quit()

    try:
        fText2 = open('text2.txt', 'r')
        text2 = fText2.read()
    except:
        print("Could not open text2.txt, please be sure file still exists")
        quit()

    exclude = set(string.punctuation)

    text1 = ''.join(pf for pf in text1 if pf not in exclude).lower()

    text2 = ''.join(pf for pf in text2 if pf not in exclude).lower()

    vocab_to_int = establish_vocab(text1, text2)

    tokenized_string = tokenize_string(vocab_to_int, text1)
    tokenized_string2 = tokenize_string(vocab_to_int, text2)

    final = cosine_simularity(tokenized_string, tokenized_string2)

    print("Text simularity score: {}".format(round(final, 3)))
    