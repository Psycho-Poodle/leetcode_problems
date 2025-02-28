text = 'Pakistan'
freq = {}
for i in text:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)