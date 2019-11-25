def text_preanalyzer():
    with open("/Users/vladislavasan/Desktop/1 курс маги/text.txt", "r") as f:
        text = f.read()
        text_l = text.lower()
        tokens = text_l.strip(".«»,!?–()[]")
        words = tokens.split()
        print("Число токенов: ", len(words))
        return(words)

s = text_preanalyzer(words)
wordforms = []

def text_wordforms:
    for word in s:
        if word[0] != word[1]:

            continue
        else:

