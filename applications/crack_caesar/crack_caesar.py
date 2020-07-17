# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open("ciphertext.txt") as f:
    words = f.read()
cache = {}
for r in words:
    if r.isspace() == False and r not in ['"',':',';',',','.','-','+','=','/','\\','|','[',']','{','}','(',')','*','^','&','\'', '_', '!', '?', '1']:
        if r in cache:
            cache[r] += 1
        else:
            cache[r] = 1
sort_orders = sorted( cache.items(), key = lambda x:x[1], reverse= True ) 
cipherProb = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z', '-']
l = 0
cipherCache = {}
for i in sort_orders:
    # print(i[0], '=>', cipherProb[l])
    cipherCache[i[0]] = cipherProb[l]
    l+=1
# print(cipherCache)

temp = ''
for s in words:
    if s in  cipherCache:
        temp += cipherCache[s]
    else: temp +=s
print(temp)

