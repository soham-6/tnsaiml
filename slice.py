data = "PmYaTsHtOeNr"

print(data[0::2])

print(data[1::2])

print(data[0:12:2], data[1:12:2])

d1 = data[0:12:2]
d2 = data[1:12:2]
print(d2[::-1], d1[::-1])
