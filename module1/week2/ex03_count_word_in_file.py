
def count_word_in_file(path):
    dictionary = {}
    file = open(path)
    lines = file.readlines()

    for line in lines:
        words = line.strip().split()
        for word in words:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1


    file.close()
    return dictionary

path = './module1/week2/P1_data.txt'
result = count_word_in_file(path)
assert result['who'] == 3
print(result['man'])