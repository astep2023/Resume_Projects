file = [58,   88,    4,
 97,   49,  59,
 56,   22,   46,
 61,   67,   13,
 41,   69,   23,
  1,   30,   42,
 77,   72,   91]
values = [128,64,32,16,8,4,2,1]

binary_version = dict()

for x in file:
    value = ""
    temp_x = x
    for v in values:
        if temp_x >= v:
            value = value + "1"
            temp_x = x - v
        else:
            value = value + "0"
    binary_version[x] = value

print(binary_version)

