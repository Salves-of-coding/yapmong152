def is_unique(word):
    word.strip()
    result = True
    for i in word:
        count = 0
        for l in word:
            if i == l:
                count += 1
        if count >= 2:
            result = False

    print(result)

is_unique('kroea')
is_unique('hello')
is_unique('sex')