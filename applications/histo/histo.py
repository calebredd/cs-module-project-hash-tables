# Your code here
with open("robin.txt") as f:
    words = f.read()
temp = ''
longest = 0
cache = {}
i=0 
for r in words:
    if r.isspace() or r == '':
        if len(temp):
            if temp in cache:
                cache[temp] += 1
            else:
                cache[temp] = 1
            if longest < len(temp):
                longest = len(temp)
            temp = ''
    # Statement to ignor special symbols
    elif r not in ['"',':',';',',','.','-','+','=','/','\\','|','[',']','{','}','(',')','*','^','&']:
        temp += r.lower()
    i+=1
    if i == len(words):
        if len(temp):
            if temp in cache:
                cache[temp] += 1
            else:
                cache[temp] = 1
            if longest < len(temp):
                longest = len(temp)
sort_orders = sorted(cache.items(), key = lambda x:(-x[1], x[0]) ) 

for i in sort_orders:
    print(i[0], end="") 
    b = 0
    c = 0
    while c + len(i[0]) < longest + 2:
        print(' ', end='')
        c+=1
    while b < i[1]:
        print('*', end='')
        b+=1
    print()

