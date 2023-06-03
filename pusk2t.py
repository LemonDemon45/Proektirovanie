#Создайте функцию, которая выводит слово, имеющее максимальную длину или список слов, если таковых
#несколько
def max_length_word(a):
    with open(a, 'r') as f:
        d = f.read().split()

    max_len = max(len(word) for word in d)
    max_d = [word for word in d if len(word) == max_len]
    if len(max_d) == 1:
        return max_d[0]
    else:
        return max_d


print(max_length_word('functions.txt'))


