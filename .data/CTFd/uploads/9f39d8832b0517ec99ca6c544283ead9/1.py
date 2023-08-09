import gmpy2
from secret import flag

a = 17
b = 197
output = [(a * ord(i)) % b for i in flag]
print(output)

# [32, 93, 32, 188, 154, 121, 25, 28, 114, 171, 39, 127, 96, 147, 192, 39, 59, 182, 39, 59, 80, 131, 28, 2, 96, 97, 2, 155]