import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
temp = ''
last = ''
cache = {}
i=0 
for r in words:
    if r.isspace() or r == '':
        if len(temp):
            if temp not in cache:
                if len(last): 
                    if last in cache:
                        cache[last].append(temp)
                    else:
                        cache[last] = [temp]
            last = temp
            temp = ''
    else:
        temp += r
    i+=1
    if i == len(words):
        if len(temp):
            if temp not in cache:
                if len(last):
                    if last in cache:
                        cache[last].append(temp)
                    else:
                        cache[last] = [temp]
# print(cache)
# exit()

# TODO: construct 5 random sentences
# Your code here
i=0
while i<5:
    l = random.randrange(1, len(cache)-1)
    findIndex = 0
    for word in cache:
        if findIndex != l:
            findIndex +=1
        elif  findIndex == l:
            findIndex +=1
            # quote = 0
            if word[0].isupper() or word[0] == '"' :
                print(word, end=" ")
                # if word[0] == '"':
                    # quote = 1
                if len(cache[word]) > 1:
                    y = random.randrange(0, len(cache[word])-1)
                else:
                    y = 0
                nexts = cache[word][y]
                while nexts in cache:
                    if nexts[-1] not in ('.', '"', '!'):
                        print(nexts, end=" ")
                        if len(cache[nexts]) > 1:
                            x = random.randrange(0, len(cache[nexts])-1)
                        else:
                            x = 0
                        nexts = cache[nexts][x]
                    else:
                        # if (quote == 1 and nexts[-1] == '"') or quote == 0:
                        print(nexts)
                        print()
                        nexts = None
                        i+=1
                        break
            break
