from SPCS import E, D, h, toHex, fromHex, newRandomKey, split, xor, b, num_to_block, block_to_num



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


key = newRandomKey()
msg = "AMERICA==FREEDOM" + "PIZZAPIZZAPIZZA_" + "AMERICA==FREEDOM"
print h(AES_ECB_E(key, msg))
print h(AES_DET_CTR_E(key, msg))
print h(AES_DET_CTR_E(key, msg))
iv, ct = AES_RANDOMIZED_CTR_E(key, msg)

print iv
print h(ct)
iv, ct = AES_RANDOMIZED_CTR_E(key, msg)

print iv
print h(ct)
iv, ct = AES_RANDOMIZED_CTR_E(key, msg)

print iv
print h(ct)

