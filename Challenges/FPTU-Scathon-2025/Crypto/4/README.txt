# Confused RC4 Challenge

## Challenge Description
A suspicious cipher has been discovered. It looks like RC4, but something feels... off.
Can you recover the flag?

## Files
- `encrypt.py`: Script used to encrypt the flag using a modified version of RC4.
- `ciphertext.txt`: The encrypted flag.

## Objective
Write a script to reverse engineer the custom RC4 encryption and recover the flag.

## Hint
- The cipher stream is based on something similar to RC4.
- The initial permutation is not the usual 0-255.
- Key length is short and guessable.

## How to Run the Encrypt Script (Optional)
```bash
python3 encrypt.py
```
(This will regenerate the ciphertext.)

Good luck!
