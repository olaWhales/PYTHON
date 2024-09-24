def forth_swapping(word):
    word_marging = []
    for count in word:
        if count == ',.':
            count.skip()
            word_marging.append(count)
        return word_marging


print(forth_swapping('ap.p,le'))
