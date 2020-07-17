def no_dups(s):
    # Your code here

    temp = ''
    cache = ''
    i=0 
    for r in s:
        if r.isspace() or r == '':
            if len(temp):
                if temp not in cache:
                    if len(cache) > 0:
                        cache += ' '+temp
                    else:
                        cache += temp
                temp = ''
        else:
            temp += r.lower()
        i+=1
        if i == len(s):
            if len(temp):
                if temp not in cache:
                    cache += temp 
    return cache


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
