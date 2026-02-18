# Install nltk first if not installed
# pip install nltk

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download required tokenizer models
nltk.download('punkt')

# Extended Introduction Text
text = """My name is Muhammad Shahbaz. 
I am from Pakistan, and I am doing a master's in Big Data and Data Science at TSU. 
I am passionate about machine learning and natural language processing. 
I enjoy working with Python and data analytics tools."""

# Sentence Segmentation
sentences = sent_tokenize(text)

print("===== Sentence Segmentation =====\n")
for i, sentence in enumerate(sentences, 1):
    print(f"Sentence {i}: {sentence}")

# Word Tokenization
print("\n===== Word Tokenization =====\n")

for i, sentence in enumerate(sentences, 1):
    words = word_tokenize(sentence)
    print(f"Sentence {i} Tokens: {words}")
