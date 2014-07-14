# Syllabus

Here is a listing of topics by day, as they were taught (in 2014). I would move some things around if I taught the course again.

Also, some minor topics are omitted, and the relationship/justification of some topics is not detailed.

## Day 1: Introduction (Monday)

- Symmetric Cryptography vs. Public-Key Cryptography, Signatures
- Secrecy (Confidentiality), Integrity (Authentication), and Identification
- Caesar Cipher, Substitution Ciphers (inc. Vigenère), One-Time Pad, Stream Cipher
- Sets
- Modular Arithmetic
- Divisibility, GCD, Euclidean Algorithm
- Solitaire Cipher (with deck of card)
- Keybase/PGP


## Day 2: Diffie-Hellman (Tuesday)

- Extended Euclidean Algorithm
  - Modular Inverses
- Diffie-Hellman Key Agreement
- Hardness Assumptions / Problems
  - Discrete Log Problem
  - (Computational) Diffie-Hellman Problem
- Repeated Squaring

## Day 3: RSA (Wednesday)

- Homomorphisms
- Group Theory
  - Group properties: identity, inverses, associativity, closure
  - commutativity
- Groups of integers mod p/n
  - Generators
  - phi(N)
- Fermat's Little Theorem
  - Euler's theorem
- RSA


## Day 4: ElGamal Encryption (Thursday)

- More RSA
- ElGamal Encryption
- Malleability


## Day 5: Chinese Remainder Theorem (Friday)

- Live Coding: ElGamal Encryption
- Chinese Remainder Theorem
  - Application to RSA (Montgomery multiplication)
- Factorization
  - Difference of Squares
- Primality Testing
  - FLT
  - (Didn't do Miller-Rabin. I think it would be worth doing if I teach this again.)
- On HW: Blind RSA Signatures (application of malleability)


## Day 6: Birthday Paradox (Monday)

- Birthday Paradox (exact and approximation)
- Baby Step-Giant Step DLP algorithm
- Malleability
  - RSA: E(m) -> E(m)^k
  - ElGamal Encryption: E(m) -> E(km), E(m) -> E(m)^k, E(m)*E(n) -> E(m*n)
- ElGamal Signatures

## Day 7: Perfect Secrecy (Tuesday)

- Perfect Secrecy
  - "ciphertext doesn't reveal anything about plaintext"
  - One-Time Pad
- XOR


## Day 8: More Perfect Secrecy (Wednesday)

- More Perfect Secrecy
  - #keys > #messages
- sets of functions
  - function F : X -> Y
  - permutations F : X -> X


## Day 9: Semantic Security / Advantage (Thursday)

- Semantic Security
  - Relation to perfect secrecy
  - cipher hides "meaning" of the message
- Advantage
  - Coin Toss Game


## Day 10: PRFs, PRPs, and Block Ciphers (Friday)

- CPA Security Game
- (Randomized) algorithm vs. (deterministic) function
- PRFs, PRPs
  - Security Games
  - Switching Lemma (using birthday paradox)
- Block Ciphers
  - AES
- Block Cipher Modes
  - CTR
  - CBC
  - OFB
- Initialization Vectors / Randomness
  - (Need for Semantic Security)
- Block Size Padding
- Live Coding: CTR Mode

## Day 11: More Block Ciphers, CBC-MAC (Monday)

- More/Review on Block Ciphers
  - CTR/CBC Security Theorems
- MACs
  - symmetric version of signatures
- CBC-MAC
- MAC Security Game (Forgery Game)
- Authenticated Encryption
  - Encrypt-then-MAC
- Live coding: CBC


## Day 12: More CBC-MAC (Tuesday)

- Discussion of CBC-MAC details
  - Bad: "random IV"
  - Bad: no finalization
  - Bad: finalization using same key
  - (Bad: reusing CBC encryption key for CBC-MAC)
- Modular One-Time MAC
- Live coding
  - CBC-MAC


## Day 13: Hash Functions (Wednesday)

- Key Stretching
- Live coding
  - Authenticated Encryption
  - AE with key stretching
- OWFs, OWPs, trapdoor permutations
- Hash Functions
  - Collision Resistance
  - Preimage Resistance
- Davies-Meyer Compression Function
  - Two Blocks -> One Block hash
  - Demonstrate several simple variants to be broken
- Merkle-Dåmgard Construction
  - SPCS-Hash: include length as extra block before message
- Password Hashing
  - slow
  - salting
- Application: Bitcoin


## Day 14: Final Day / Extra Topics (Thursday)

- TLS Handshake
  - Key Exchange
  - Cipher Spec
  - Wireshark demo
- Secret Sharing
  - Polynomials
- Course Wrap-Up / Bonus Topic
