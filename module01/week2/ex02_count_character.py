
def count_character(word):
    dictionary = {}
    for character in word:
        if character not in dictionary:
            dictionary[character] = 1
        else:
            dictionary[character] += 1
    return dictionary

assert count_character("Baby") == {'B': 1 , 'a': 1 , 'b': 1 , 'y': 1}
print(count_character('smiles'))