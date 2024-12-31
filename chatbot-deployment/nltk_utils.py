# this file consists of defined nltk methods 

'''from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer'''

import numpy as np
import nltk
import torch
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

# from spellchecker import SpellChecker

# spell = SpellChecker()

# def correct_spelling(sentence):
#     corrected_sentence = []
#     for word in sentence.split():
#         corrected_word = spell.correction(word)
#         corrected_sentence.append(corrected_word)
        
#     return ' '.join(corrected_sentence)

# # Example usage
#user_input = "Helo, hw are yu?"
#corrected_input = correct_spelling(user_input)
#print(corrected_input)  # Output: "Hello, how are you?"



def tokenize(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    
    return nltk.word_tokenize(sentence)


def stem(word):
    """
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())


# # Training Word2Vec model (for demonstration, use pre-trained embeddings for real projects)
# sentences = [tokenize(pattern) for pattern in all_patterns]  # All patterns from intents.json
# w2v_model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# def sentence_to_vector(sentence, model, size):
#     words = tokenize(sentence)
#     vec = np.zeros(size)
#     for word in words:
#         if word in model.wv:
#             vec += model.wv[word]
#     return vec / len(words)


def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1    #intialize word matching sentence to 1

    return bag


FILE = "data.pth"
data = torch.load(FILE)
'''
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tf=TfidfVectorizer()
tfidf=tf.fit_transform(all_words)
print(tfidf)
'''
