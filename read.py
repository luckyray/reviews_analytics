data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        # if count % 1000 == 0:
        print(len(data))
print('file is read, total', len(data), 'data')
print(data[0])



sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print(sum_len)
print('Average line length is', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('There are total', len(new), 'items which length less than 100')
print(new[0])
print(len(new[0]))

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('total', len(good), 'item/s')
print(good[0])


wc = {} # word count dict
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # new key input to dict

for word in wc:
    if wc[word] >= 10000:
        print(word, wc[word])

#print(len(wc))
#print(wc['Raymond'])

while True:
    word = input('Please enter the word you want to look up: ')
    if word == 'q':
        break
    if word in wc:
        print(word, 'have appeared', wc[word], 'times')
    else:
        print('this word does not appeared')

print('Thanks for using this look up function.')
