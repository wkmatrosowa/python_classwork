import string

def text_reader(text):
    with open("file.txt", "r") as f:
        text = f.read()

def tokenizer(text):
    words = text.strip()
    words = words.lower()
    punct_digits = []
    for sym in words:
        if sym in string.punctuation:
            punct_digits.append(sym)
        elif sym in string.digits:
            punct_digits.append(sym)
    return words

print(words)

# def make_tsv_file(words):
#     with open ("our_words.tsv", "w") as tsvfile:
#         newfile = tsvfile.write()


