
import sys

n =  48#sys.argv[1]
#if n.isdecimal():
print(bin(n))
offset = n.bit_length()
_n1 = n >> offset-1
_n2 = n << 1
print(bin(_n2))

mask = 0b011111

_n2 = _n2 & mask

result = _n1 | _n2

print(bin(n))
print(bin(_n1))
print(bin(_n2))
print(bin(mask))
print(result)