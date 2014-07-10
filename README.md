# High School Crypto Class Materials

Materials from teaching cryptography at a 3-week Stanford summer program for high school students (SPCS, formerly EPGY), with 14 days of instruction from June 23, 2014 to July 10, 2014. The students all just finished 9th or 10th grade.

Almost all of the course material is assembled together from scratch, with a slight focus on math, and a preference to work with actual constructions/numbers instead of full technical proofs (for example, see the mini PRPs in homeworks 11-13).

This sort of course is usually centered around number theory, but most of the advanced math is not of as much interest to practical cryptography. Thus, I focused on interesting/mathematical aspects of block ciphers on the second half of the course.

## Credits

Everything I learned about crypto, I learned from [Dan Boneh](https://crypto.stanford.edu/~dabo/) and the internet.

Almost all the material is based on:

- Dan's [CS255 crypto class at Stanford](https://crypto.stanford.edu/~dabo/cs255/) (which I took once and TAed twice).
- Dan's [Coursera crypto course](https://www.coursera.org/course/crypto) lecture slides.
- Topics discussed in relevant Wikipedia entries.

I also had access to preliminary notes and a syllabus from a previous iteration of the course, taught by [Nick Haber](http://math.stanford.edu/~nhaber/) and based on [`An Introduction to Mathematical Cryptography`](http://link.springer.com/book/10.1007%2F978-0-387-77993-5).

# In this Repository

## Live Code (from class)

- ElGamal Encryption in Mathematica
- [Block Ciphers](code/Implementations.py)
  - Deterministic CTR (deterministic and randomized),
  - CBC
  - CBC-MAC
  - Authenticated Encryption (CBC with CBC-MAC)
    - Simple key stretching for single-key AE.
 - Encrypting a file on the file system.

## Homeworks

I had to create most of these "from scratch". A few of them are taken from CS255.

## Lecture Notes

Not included right now. Everything I have is hand-written on index cards. (It's good for planning out material in board-sized chunks!)
