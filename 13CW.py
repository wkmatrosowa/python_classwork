s = 'кошка'
consonants = 'бвгджзйклмнпрстфхцчшщ'
vowels = 'ауоыиэяюёе'
no_sounds = 'ьъ'

def write_sym(string, sym):
    return string + sym

def opened(string, sym):
    return string + sym + "-"

def passing(string, sym):
    return string

def event(ind, s):
    if s[ind-1] in consonants:
        return 'closed syllable'
    elif s[ind] in vowels and s[ind+1] in consonants:
        return 'closed syllable'
    elif

        if s[ind + 1] in consonants:
            return 'closed syllable'
        else:
            return 'opened syllable'
    else:
        return 'vowel'


table = {
    ('ON_SYLL', 'consonant'): ['IN_SYLL', write_sym],
    ('IN_SYLL', 'consonant'): ['IN_SYLL', passing],
    ('ON_SYLL', 'vowel'): ['IN_SYLL', write_sym],
    ('IN_SYLL', 'vowel'): ['IN_SYLL', passing],
    ('ON_SYLL', 'closed syllable'): ['IN_SYLL', opened],
    ('ON_SYLL', 'opened syllable'): ['IN_SYLL', opened],
    ('IN_SYLL', 'opened syllable'): ['IN_SYLL', passing],
    ('IN_SYLL', 'closed syllable'): ['IN_SYLL', passing]
}

state = 'ON_SYLL'
string = ''
for ind, sym in enumerate(s):
    state, action = table[state, event(ind, s)]
    string = action(string, sym)

print(string)
