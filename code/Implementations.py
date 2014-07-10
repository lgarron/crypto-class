from SPCS import E, D, h, toHex, fromHex, newRandomKey, split, xor, b, num_to_block, block_to_num

"""
This file was written entirely during live coding
sessions in a crypto class for high school students.
( http://spcs.stanford.edu/ )

Apart from day breaks, nothing has been added or removed,
so excuse the organization. The crypto should hopefully be
correct, though.

You can also definitely see traces of July 4th
and the World Cup in this file. :-)

"""


print "Hello, World!"

# AES : {0,1}^128 x {0, 1}^128 -> {0, 1}^128
# 8 bits in a byte => 16 bytes

# key = "HAPPY FOURTH USA"
# print h(key)
key = newRandomKey()
# print h(key)
# print ""
# print h(E(key, "AMERICA==FREEDOM"))
# print h(E(key, "GOD BLESS MURICA"))
# print h(E(key, "AMERICA==FREEDOM"))

# ECB (BAD) (NEVER USE) (FORGET ABOUT IT AFTER THIS CLASS)
def AES_ECB_E(key, msg):
  # split our message into 16-byte block
  return "".join([E(key, block) for block in split(msg)])

def AES_ECB_D(key, msg):
  # split our message into 16-byte block
  return "".join([D(key, block) for block in split(msg)])

msg = "AMERICA==FREEDOM" + "PIZZAPIZZAPIZZA_" + "AMERICA==FREEDOM"
# c = AES_ECB_E(key, msg)
# decrypted = AES_ECB_D(key, c)
# print h(c)
# print decrypted

def AES_DET_CTR_E(key, msg):
  blocks = split(msg)
  counter = 0
  output = ""
  for block in blocks:
    mask = E(key, num_to_block(counter))
    encrypted_block = xor(mask, block)
    output += encrypted_block
    counter += 1
  return output


# Notes about CTR Mode:
# - Stream Cipher
#   - Malleable (until Monday: MACs signatures)
# - Unlike OTP:
#   - key is short
#   - don't have perfect secrecy (|K| > |M|)
#   - can encrypt arbitrary-length message using the same short key
# - Like OTP:
# - Can use the key only once for DETERMINISTIC CTR
#   - ecnrypting two messages m_0, m_1 using same key: xor(m_0, m_1)

AES_DET_CTR_D = AES_DET_CTR_E

# key = newRandomKey()
# msg = "AMERICA==FREEDOM" + "PIZZAPIZZAPIZZA_" + "AMERICA==FREEDOM"
# print h(AES_ECB_E(key, msg))
# print h(AES_DET_CTR_E(key, msg))
# print AES_DET_CTR_D(key, AES_DET_CTR_E(key, msg))




###### Day Break




def AES_RANDOMIZED_CTR_E(key, msg):
  blocks = split(msg)
  iv =  block_to_num(newRandomKey()) # IVs = keys = {0, 1}^128
  counter = iv
  output = ""
  for block in blocks:
    mask = E(key, num_to_block(counter))
    encrypted_block = xor(mask, block)
    output += encrypted_block
    counter += 1
  return (iv, output)


# key = newRandomKey()
# msg = "AMERICA==FREEDOM" + "PIZZAPIZZAPIZZA_" + "AMERICA==FREEDOM"
# print h(AES_ECB_E(key, msg))
# print h(AES_DET_CTR_E(key, msg))
# print h(AES_DET_CTR_E(key, msg))
# iv, ct = AES_RANDOMIZED_CTR_E(key, msg)

# print iv
# print h(ct)
# iv, ct = AES_RANDOMIZED_CTR_E(key, msg)

# print iv
# print h(ct)
# iv, ct = AES_RANDOMIZED_CTR_E(key, msg)

# print iv
# print h(ct)


## PRF

# key = newRandomKey()
# print h(AES_DET_CTR_E(key, num_to_block(0)))
# print h(AES_DET_CTR_E(key, num_to_block(1)))
# print h(AES_DET_CTR_E(key, num_to_block(0)))
# print h(AES_DET_CTR_E(key, num_to_block(2)))

##### Day Break


# CBC with CBC-MAC

# AES: {0, 1}^128 x {0, 1}^128 -> {0, 1}^128

def AES_CBC_ENC(key, msg):
  startIV = newRandomKey() # random key = random block = random IV
  currentIV = startIV
  c = ""
  for block in split(msg):
    currentIV = E(key, xor(currentIV, block))
    c += currentIV
  return (startIV, c)

def AES_CBC_DEC(key, startIV, c):
  m = ""
  currentIV = startIV
  for block in split(c):
    m += xor(currentIV, D(key, block))
    currentIV = block
  return m

key = newRandomKey()
msg = "GERMANYVSBRAZIL!PIZZAPIZZAPIZZA_GERMANYVSBRAZIL!"

IV, c = AES_CBC_ENC(key, msg)
# print h(IV)
# print h(c)

# print AES_CBC_DEC(key, IV, c)

def AES_CBC_MAC(k1, k2, x):
  # CBC Encryption Part
  currentIV = num_to_block(0)
  for block in split(x):
    currentIV = E(k1, xor(currentIV, block))
  # Finalization
  return E(k2, currentIV)

# k1 = newRandomKey()
# k2 = newRandomKey()
# x = "GERMANYVSBRAZIL!PIZZAPIZZAPIZZA_GERMANYVSBRAZIL!"
# s = AES_CBC_MAC(k1, k2, x)
# print h(s)

def AES_VERIFY_CBC_MAC(k1, k2, s, x):
  return AES_CBC_MAC(k1, k2, x) == s

# x = "GERMANYVSBRAZIL!PIZZAPIZZAPIZZA_GERMANYVSBRAZIL!"
# print AES_VERIFY_CBC_MAC(k1, k2, s, x)



##### Day Break




def AES_AE_CBC_WITH_CBC_MAC(kE, k1, k2, m):
  IV, c = AES_CBC_ENC(kE, m)
  s = AES_CBC_MAC(k1, k2, IV + c) # Need to include IV
  return (IV, c, s)


def AES_AE_CBC_WITH_CBC_MAC_DECRYPT(kE, k1, k2, IV, c, s):
  if not AES_VERIFY_CBC_MAC(k1, k2, s, IV + c):
    assert False, "ERROR DETECTED"
  return AES_CBC_DEC(kE, IV, c)


# IV = xor(IV, num_to_block(7))

# print h(IV)
# print h(c)
# print h(s)

def AES_AE_ONE_KEY(k, m):
  kE = E(k, num_to_block(0))
  k1 = E(k, num_to_block(1))
  k2 = E(k, num_to_block(2))
  return AES_AE_CBC_WITH_CBC_MAC(kE, k1, k2, m)

def AES_AE_ONE_KEY_DECRYPT(k, IV, c, s):
  kE = E(k, num_to_block(0))
  k1 = E(k, num_to_block(1))
  k2 = E(k, num_to_block(2))
  return AES_AE_CBC_WITH_CBC_MAC_DECRYPT(kE, k1, k2, IV, c, s)


key = newRandomKey()

motd = "REDWHITEBLUEFLAGREDWHITEBLUEFLAG"
IV, c, s = AES_AE_ONE_KEY(key, motd)

# print h(IV)
# print h(c)
# print h(s)

# print AES_AE_ONE_KEY_DECRYPT(key, IV, c, s)

# IV, c, s = AES_AE_CBC_WITH_CBC_MAC(kE, k1, k2, motd)

f = open("cube_heart.png", "r")
msg = f.read()
f.close()

import binascii
key = binascii.unhexlify("bba1951b279bfa3267fd726106f994a7")
print h(key)

IV, c, s = AES_AE_ONE_KEY(key, msg)

out_file = open("cube_heart.png.encrypted", "w")
out_file.write(s + IV + c)
out_file.close()

########

with open("cube_heart.png.encrypted", "r") as input_file:
  concatenated = input_file.read()

s = split(concatenated)[0]
IV = split(concatenated)[1]
c = "".join(split(concatenated)[2:])

decrypted = AES_AE_ONE_KEY_DECRYPT(key, IV, c, s)


with open("cube_heart.decrypted.png", "w") as output_file:
  output_file.write(decrypted)




# print AES_AE_CBC_WITH_CBC_MAC_DECRYPT(kE, k1, k2, IV, c, s)

