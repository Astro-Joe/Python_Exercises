def letters(_input):
    """Define a function which counts vowels and
    consonant in a word."""
    _vowels = []
    _conson = []
    vowels = list('aeiou')
    consonant = list('bcdfghjklmnpqrstvwxyz')
    __input = list(_input.lower())
    for i in __input:
        if i in consonant:
            _conson.append(i)
    for i in __input:
        if i in vowels:
            _vowels.append(i)
    print('Count of vowel is = ' + str(len(_vowels)))
    print('Count of consonant is = ' + str(len(_conson)))


var = input('Enter a word: ')
letters(var)
