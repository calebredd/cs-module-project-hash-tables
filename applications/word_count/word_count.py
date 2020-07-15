def word_count(s):
    # Your code here
    temp = ''
    cache = {}
    i=0 
    for r in s:
        if r.isspace() or r == '':
            if len(temp):
                if temp in cache:
                    cache[temp] += 1
                else:
                    cache[temp] = 1
                temp = ''
        # Statement to ignor special symbols
        elif r not in ['"',':',';',',','.','-','+','=','/','\\','|','[',']','{','}','(',')','*','^','&']:
            temp += r.lower()
        i+=1
        if i == len(s):
            if len(temp):
                if temp in cache:
                    cache[temp] += 1
                else:
                    cache[temp] = 1
    return cache



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
