import Crypto.Cipher.AES
import binascii
from Crypto import Random

"""
Convenience functions for live coding during a crypto class.
(This was mostly about Getting Stuff Done.
 I may rewrite some of this to be more elegant later.)
"""

def E(k, x):
  assert len(x) == 16
  return Crypto.Cipher.AES.new(k, Crypto.Cipher.AES.MODE_ECB).encrypt(x)

def D(k, x):
  assert len(x) == 16
  return Crypto.Cipher.AES.new(k, Crypto.Cipher.AES.MODE_ECB).decrypt(x)

def newRandomKey():
  # print("Generating random new key...")
  return Random.new().read(Crypto.Cipher.AES.block_size)

toHex = binascii.hexlify
h = toHex
fromHex = binascii.unhexlify

def split(m):
  return ["".join(a) for a in zip(*[m[i::16] for i in range(16)])]

def xor(a, b):     # xor two strings (trims the longer input)
  return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])


def b(s):
  a = "B{"
  for i in s:
    a += ("1" if (ord(i) & 0b10000000) else "0")
    a += ("1" if (ord(i) & 0b01000000) else "0")
    a += ("1" if (ord(i) & 0b00100000) else "0")
    a += ("1" if (ord(i) & 0b00010000) else "0")
    a += ("1" if (ord(i) & 0b00001000) else "0")
    a += ("1" if (ord(i) & 0b00000100) else "0")
    a += ("1" if (ord(i) & 0b00000010) else "0")
    a += ("1" if (ord(i) & 0b00000001) else "0")
  a += "}"
  return a

def block_to_num(block):
  l = len(block)
  a = 0
  for i in range(l):
    a *= 256
    a += ord(block[i])
  return a

def num_to_block(num):
  o = ""
  for i in range(16):
    o = chr(num % 256) + o
    num = num / 256
  return o

def increment(s):
  return num_to_block(block_to_num(s) + 1)

# print num_to_block(block_to_num("aaaaaaaaaaaaaaaa") + 1)


"""
from SPCS import AES, h, toHex, fromHex, newRandomKey
"""