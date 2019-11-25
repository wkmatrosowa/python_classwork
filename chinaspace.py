import string
import re

def tokenizer():
    with open("chinaspace.txt", "r") as f:
        text = f.read()
    tokens = text.lower()
    words = tokens.split()
    for word in words:
        for sym in word:
            if sym in string.punctuation:


    print(words)

tokenizer()

# def find_chinese_ships:
#     chinese_reg = "^(.+?) $(кит.)"
