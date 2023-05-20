import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sent = [
    'I Dont know how',
    'This is IT',
    'The rhyme that I spit cant be fit inside!',
    'Nigga This aint my jam! Ridiculous'
]

# Initialize the Tokenizer
tokenizer = Tokenizer(num_words=50, oov_token='Illia') # 'num_word' define the maximum number of entries in the Dictionary i.e fro mthe entire data prick only first 100 common words.

# Generate indices for each word in the corpus or the data
tokenizer.fit_on_texts(sent)

# Get indices and prints it
word_idx = tokenizer.word_index

seq = tokenizer.texts_to_sequences(sent)
padded = pad_sequences(seq, padding='pre', truncating='pre')

print(word_idx)
print(seq)
print(padded)