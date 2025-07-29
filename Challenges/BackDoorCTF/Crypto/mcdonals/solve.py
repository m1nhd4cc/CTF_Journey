from pwn import *

r1 = remote("34.42.147.172", 8004)
r2 = remote("34.42.147.172", 8004)

payload = b"\x00"
for _ in range(64):
    r2.sendlineafter(
        b"Enter your message and token:", payload.hex().encode() + b" " + b"00"
    )
    token = r2.recvline().split(b" ")[-1]
    r1.sendlineafter(
        b"Enter your message and token:", payload.hex().encode() + b" " + token
    )
    payload += b"\x00"

r1.interactive()

r1.close()
r2.close()



#When I connect to server:

# [+] Opening connection to 34.45.235.239 on port 8004: Done
# Welcome to the Token Verification Challenge!
# ============================================
# Rules:
# 1. Submit message-token pairs
# 2. Each token must be valid for its message
# 3. You cannot reuse tokens
# 4. Get 64 valid tokens accepted to win!

# Format: <hex-encoded-message> <hex-encoded-token>
# Example: 48656c6c6f 1234567890abcdef

# Attempt 1/128
# Enter your message and token: 4d65737361676531 4d65737361676531
# Invalid token! Expected token: 7d22cfb3ee44aa2e

# Attempt 2/128
# Enter your message and token: 4d65737361676531 7d22cfb3ee44aa2e
# Success! 1/64 valid tokens verified

# Attempt 3/128
# Enter your message and token: 4d65737361676532 4d65737361676532
# Invalid token! Expected token: 03598635ba81a9a1

# Attempt 4/128
# Enter your message and token: 4d65737361676532 03598635ba81a9a1
# Success! 2/64 valid tokens verified

# Attempt 5/128
# Enter your message and token: 4d65737361676533 4d65737361676533
# Invalid token! Expected token: 6f83a92214846863

# Attempt 6/128
# Enter your message and token: 4d65737361676533 6f83a92214846863
# Success! 3/64 valid tokens verified

# Attempt 7/128
# Enter your message and token: 4d65737361676534 4d65737361676534
# Invalid token! Expected token: 28190f7ab77b49f0

# Attempt 8/128
# Enter your message and token: 4d65737361676534 28190f7ab77b49f0
# Success! 4/64 valid tokens verified

# Attempt 9/128
# Enter your message and token: 4d65737361676535 4d65737361676535
# Invalid token! Expected token: 964da26ca9244b6e

# Attempt 10/128
# Enter your message and token: 4d65737361676535 964da26ca9244b6e
# Success! 5/64 valid tokens verified

# Attempt 11/128
# Enter your message and token: 4d65737361676536 4d65737361676536
# Invalid token! Expected token: 258b5d9c0613b305

# Attempt 12/128
# Enter your message and token: 4d65737361676536 258b5d9c0613b305
# Success! 6/64 valid tokens verified

# Attempt 13/128
# Enter your message and token: 4d65737361676537 4d65737361676537
# Invalid token! Expected token: 8d60feba2da23feb

# Attempt 14/128
# Enter your message and token: 4d65737361676537 8d60feba2da23feb
# Success! 7/64 valid tokens verified

# Attempt 15/128
# Enter your message and token: 4d65737361676538 4d65737361676538
# Invalid token! Expected token: 7092805c3e741ca3

# Attempt 16/128
# Enter your message and token: 4d65737361676538 7092805c3e741ca3
# Success! 8/64 valid tokens verified

# Attempt 17/128
# Enter your message and token: 4d65737361676539 4d65737361676539
# Invalid token! Expected token: c70bc3946696df2b

# Attempt 18/128
# Enter your message and token: 4d65737361676539 c70bc3946696df2b
# Success! 9/64 valid tokens verified

# Attempt 19/128
# Enter your message and token: 4d6573736167653130 4d6573736167653130
# Invalid token! Expected token: bdded58b9060bfa0

# Attempt 20/128
# Enter your message and token: 4d6573736167653130 bdded58b9060bfa0
# Success! 10/64 valid tokens verified

# Attempt 21/128
# Enter your message and token: 4d6573736167653131 4d6573736167653131
# Invalid token! Expected token: fdcf6af332230479

# Attempt 22/128
# Enter your message and token: 4d6573736167653131 fdcf6af332230479
# Success! 11/64 valid tokens verified

# Attempt 23/128
# Enter your message and token: 4d6573736167653132 4d6573736167653132
# Invalid token! Expected token: 774007d8db29109d

# Attempt 24/128
# Enter your message and token: 4d6573736167653132 774007d8db29109d
# Success! 12/64 valid tokens verified

# Attempt 25/128
# Enter your message and token: 4d6573736167653133 4d6573736167653133
# Invalid token! Expected token: a40cc671b61754e4

# Attempt 26/128
# Enter your message and token: 4d6573736167653133 a40cc671b61754e4
# Success! 13/64 valid tokens verified

# Attempt 27/128
# Enter your message and token: 4d6573736167653134 4d6573736167653134
# Invalid token! Expected token: 33e7abce95c7825b

# Attempt 28/128
# Enter your message and token: 4d6573736167653134 33e7abce95c7825b
# Success! 14/64 valid tokens verified

# Attempt 29/128
# Enter your message and token: 4d6573736167653135 4d6573736167653135
# Invalid token! Expected token: 328127af2e11ac5f

# Attempt 30/128
# Enter your message and token: 4d6573736167653135 328127af2e11ac5f
# Success! 15/64 valid tokens verified

# Attempt 31/128
# Enter your message and token: 4d6573736167653136 4d6573736167653136
# Invalid token! Expected token: 653c8d3850ef3147

# Attempt 32/128
# Enter your message and token: 4d6573736167653136 653c8d3850ef3147
# Success! 16/64 valid tokens verified

# Attempt 33/128
# Enter your message and token: 4d6573736167653137 4d6573736167653137
# Invalid token! Expected token: 835f2f9d568a750a

# Attempt 34/128
# Enter your message and token: 4d6573736167653137 835f2f9d568a750a
# Success! 17/64 valid tokens verified

# Attempt 35/128
# Enter your message and token: 4d6573736167653138 4d6573736167653138
# Invalid token! Expected token: 2afd1ac52a0e10ed

# Attempt 36/128
# Enter your message and token: 4d6573736167653138 2afd1ac52a0e10ed
# Success! 18/64 valid tokens verified

# Attempt 37/128
# Enter your message and token: 4d6573736167653139 4d6573736167653139
# Invalid token! Expected token: c2dde2f1c825556d

# Attempt 38/128
# Enter your message and token: 4d6573736167653139 c2dde2f1c825556d
# Success! 19/64 valid tokens verified

# Attempt 39/128
# Enter your message and token: 4d6573736167653230 4d6573736167653230
# Invalid token! Expected token: 848b7d2b530ce8ba

# Attempt 40/128
# Enter your message and token: 4d6573736167653230 848b7d2b530ce8ba
# Success! 20/64 valid tokens verified

# Attempt 41/128
# Enter your message and token: 4d6573736167653231 4d6573736167653231
# Invalid token! Expected token: ff298356ee042dac

# Attempt 42/128
# Enter your message and token: 4d6573736167653231 ff298356ee042dac
# Success! 21/64 valid tokens verified

# Attempt 43/128
# Enter your message and token: 4d6573736167653232 4d6573736167653232
# Invalid token! Expected token: 7fa22818584a74f9

# Attempt 44/128
# Enter your message and token: 4d6573736167653232 7fa22818584a74f9
# Success! 22/64 valid tokens verified

# Attempt 45/128
# Enter your message and token: 4d6573736167653233 4d6573736167653233
# Invalid token! Expected token: 8910aaad21284b52

# Attempt 46/128
# Enter your message and token: 4d6573736167653233 8910aaad21284b52
# Success! 23/64 valid tokens verified

# Attempt 47/128
# Enter your message and token: 4d6573736167653234 4d6573736167653234
# Invalid token! Expected token: ae3b5b706ad2f098

# Attempt 48/128
# Enter your message and token: 4d6573736167653234 ae3b5b706ad2f098
# Success! 24/64 valid tokens verified

# Attempt 49/128
# Enter your message and token: 4d6573736167653235 4d6573736167653235
# Invalid token! Expected token: b91e6bdc8da7d85d

# Attempt 50/128
# Enter your message and token: 4d6573736167653235 b91e6bdc8da7d85d
# Success! 25/64 valid tokens verified

# Attempt 51/128
# Enter your message and token: 4d6573736167653236 4d6573736167653236
# Invalid token! Expected token: 37108175f90750cf

# Attempt 52/128
# Enter your message and token: 4d6573736167653236 37108175f90750cf
# Success! 26/64 valid tokens verified

# Attempt 53/128
# Enter your message and token: 4d6573736167653237 4d6573736167653237
# Invalid token! Expected token: 52acb9855e669cae

# Attempt 54/128
# Enter your message and token: 4d6573736167653237 52acb9855e669cae
# Success! 27/64 valid tokens verified

# Attempt 55/128
# Enter your message and token: 4d6573736167653238 4d6573736167653238
# Invalid token! Expected token: 00773f19c4ddc684

# Attempt 56/128
# Enter your message and token: 4d6573736167653238 00773f19c4ddc684
# Success! 28/64 valid tokens verified

# Attempt 57/128
# Enter your message and token: 4d6573736167653239 4d6573736167653239
# Invalid token! Expected token: 371ff9b18842d643

# Attempt 58/128
# Enter your message and token: 4d6573736167653239 371ff9b18842d643
# Success! 29/64 valid tokens verified

# Attempt 59/128
# Enter your message and token: 4d6573736167653330 4d6573736167653330
# Invalid token! Expected token: 4f833ceae7e18596

# Attempt 60/128
# Enter your message and token: 4d6573736167653330 4f833ceae7e18596
# Success! 30/64 valid tokens verified

# Attempt 61/128
# Enter your message and token: 4d6573736167653331 4d6573736167653331
# Invalid token! Expected token: 84d7ba09779024ba

# Attempt 62/128
# Enter your message and token: 4d6573736167653331 84d7ba09779024ba
# Success! 31/64 valid tokens verified

# Attempt 63/128
# Enter your message and token: 4d6573736167653332 4d6573736167653332
# Invalid token! Expected token: e53e6a43dfdbeedd

# Attempt 64/128
# Enter your message and token: 4d6573736167653332 e53e6a43dfdbeedd
# Success! 32/64 valid tokens verified

# Attempt 65/128
# Enter your message and token: 4d6573736167653333 4d6573736167653333
# Invalid token! Expected token: 93846f107cde214e

# Attempt 66/128
# Enter your message and token: 4d6573736167653333 93846f107cde214e
# Success! 33/64 valid tokens verified

# Attempt 67/128
# Enter your message and token: 4d6573736167653334 4d6573736167653334
# Invalid token! Expected token: 62211c993ede9ba8

# Attempt 68/128
# Enter your message and token: 4d6573736167653334 62211c993ede9ba8
# Success! 34/64 valid tokens verified

# Attempt 69/128
# Enter your message and token: 4d6573736167653335 4d6573736167653335
# Invalid token! Expected token: 60bb76db10c367a4

# Attempt 70/128
# Enter your message and token: 4d6573736167653335 60bb76db10c367a4
# Success! 35/64 valid tokens verified

# Attempt 71/128
# Enter your message and token: 4d6573736167653336 4d6573736167653336
# Invalid token! Expected token: 7619360cd6aa6db4

# Attempt 72/128
# Enter your message and token: 4d6573736167653336 7619360cd6aa6db4
# Success! 36/64 valid tokens verified

# Attempt 73/128
# Enter your message and token: 4d6573736167653337 4d6573736167653337
# Invalid token! Expected token: 34c50fd0238b6032

# Attempt 74/128
# Enter your message and token: 4d6573736167653337 34c50fd0238b6032
# Success! 37/64 valid tokens verified

# Attempt 75/128
# Enter your message and token: 4d6573736167653338 4d6573736167653338
# Invalid token! Expected token: 0bb97eabd8c4adb2

# Attempt 76/128
# Enter your message and token: 4d6573736167653338 0bb97eabd8c4adb2
# Success! 38/64 valid tokens verified

# Attempt 77/128
# Enter your message and token: 4d6573736167653339 4d6573736167653339
# Invalid token! Expected token: a9aa73546278bd49

# Attempt 78/128
# Enter your message and token: 4d6573736167653339 a9aa73546278bd49
# Success! 39/64 valid tokens verified

# Attempt 79/128
# Enter your message and token: 4d6573736167653430 4d6573736167653430
# Invalid token! Expected token: c10999e44e4c4437

# Attempt 80/128
# Enter your message and token: 4d6573736167653430 c10999e44e4c4437
# Success! 40/64 valid tokens verified

# Attempt 81/128
# Enter your message and token: 4d6573736167653431 4d6573736167653431
# Invalid token! Expected token: 8157ee6bd7141ae8

# Attempt 82/128
# Enter your message and token: 4d6573736167653431 8157ee6bd7141ae8
# Success! 41/64 valid tokens verified

# Attempt 83/128
# Enter your message and token: 4d6573736167653432 4d6573736167653432
# Invalid token! Expected token: b4eeae2c71057b3e

# Attempt 84/128
# Enter your message and token: 4d6573736167653432 b4eeae2c71057b3e
# Success! 42/64 valid tokens verified

# Attempt 85/128
# Enter your message and token: 4d6573736167653433 4d6573736167653433
# Invalid token! Expected token: f59e830b4213856c

# Attempt 86/128
# Enter your message and token: 4d6573736167653433 f59e830b4213856c
# Success! 43/64 valid tokens verified

# Attempt 87/128
# Enter your message and token: 4d6573736167653434 4d6573736167653434
# Invalid token! Expected token: 49e87f28a1300f42

# Attempt 88/128
# Enter your message and token: 4d6573736167653434 49e87f28a1300f42
# Success! 44/64 valid tokens verified

# Attempt 89/128
# Enter your message and token: 4d6573736167653435 4d6573736167653435
# Invalid token! Expected token: 4494758a32a5c614

# Attempt 90/128
# Enter your message and token: 4d6573736167653435 4494758a32a5c614
# Success! 45/64 valid tokens verified

# Attempt 91/128
# Enter your message and token: 4d6573736167653436 4d6573736167653436
# Invalid token! Expected token: 218018c00e4ba3e6

# Attempt 92/128
# Enter your message and token: 4d6573736167653436 218018c00e4ba3e6
# Success! 46/64 valid tokens verified

# Attempt 93/128
# Enter your message and token: 4d6573736167653437 4d6573736167653437
# Invalid token! Expected token: 0d0dca225454bab9

# Attempt 94/128
# Enter your message and token: 4d6573736167653437 0d0dca225454bab9
# Success! 47/64 valid tokens verified

# Attempt 95/128
# Enter your message and token: 4d6573736167653438 4d6573736167653438
# Invalid token! Expected token: 7a81462aedc00986

# Attempt 96/128
# Enter your message and token: 4d6573736167653438 7a81462aedc00986
# Success! 48/64 valid tokens verified

# Attempt 97/128
# Enter your message and token: 4d6573736167653439 4d6573736167653439
# Invalid token! Expected token: eb978e8f27d03f0d

# Attempt 98/128
# Enter your message and token: 4d6573736167653439 eb978e8f27d03f0d
# Success! 49/64 valid tokens verified

# Attempt 99/128
# Enter your message and token: 4d6573736167653530 4d6573736167653530
# Invalid token! Expected token: b38ae5515c3c49f7

# Attempt 100/128
# Enter your message and token: 4d6573736167653530 b38ae5515c3c49f7
# Success! 50/64 valid tokens verified

# Attempt 101/128
# Enter your message and token: 4d6573736167653531 4d6573736167653531
# Invalid token! Expected token: a5bfba36ea737ffe

# Attempt 102/128
# Enter your message and token: 4d6573736167653531 a5bfba36ea737ffe
# Success! 51/64 valid tokens verified

# Attempt 103/128
# Enter your message and token: 4d6573736167653532 4d6573736167653532
# Invalid token! Expected token: e4a145da35fbcfe9

# Attempt 104/128
# Enter your message and token: 4d6573736167653532 e4a145da35fbcfe9
# Success! 52/64 valid tokens verified

# Attempt 105/128
# Enter your message and token: 4d6573736167653533 4d6573736167653533
# Invalid token! Expected token: 17807a35f03d8a60

# Attempt 106/128
# Enter your message and token: 4d6573736167653533 17807a35f03d8a60
# Success! 53/64 valid tokens verified

# Attempt 107/128
# Enter your message and token: 4d6573736167653534 4d6573736167653534
# Invalid token! Expected token: 0f4e4cef6bb85972

# Attempt 108/128
# Enter your message and token: 4d6573736167653534 0f4e4cef6bb85972
# Success! 54/64 valid tokens verified

# Attempt 109/128
# Enter your message and token: 4d6573736167653535 4d6573736167653535
# Invalid token! Expected token: 5699f9c40cb987e5

# Attempt 110/128
# Enter your message and token: 4d6573736167653535 5699f9c40cb987e5
# Success! 55/64 valid tokens verified

# Attempt 111/128
# Enter your message and token: 4d6573736167653536 4d6573736167653536
# Invalid token! Expected token: b90fcf30ccad4020

# Attempt 112/128
# Enter your message and token: 4d6573736167653536 b90fcf30ccad4020
# Success! 56/64 valid tokens verified

# Attempt 113/128
# Enter your message and token: 4d6573736167653537 4d6573736167653537
# Invalid token! Expected token: 6c554007c9f71104

# Attempt 114/128
# Enter your message and token: 4d6573736167653537 6c554007c9f71104
# Success! 57/64 valid tokens verified

# Attempt 115/128
# Enter your message and token: 4d6573736167653538 4d6573736167653538
# Invalid token! Expected token: ef6961173c485fe8

# Attempt 116/128
# Enter your message and token: 4d6573736167653538 ef6961173c485fe8
# Success! 58/64 valid tokens verified

# Attempt 117/128
# Enter your message and token: 4d6573736167653539 4d6573736167653539
# Invalid token! Expected token: 1627bef065945ff1

# Attempt 118/128
# Enter your message and token: 4d6573736167653539 1627bef065945ff1
# Success! 59/64 valid tokens verified

# Attempt 119/128
# Enter your message and token: 4d6573736167653630 4d6573736167653630
# Invalid token! Expected token: 39930cbe27f22e6b

# Attempt 120/128
# Enter your message and token: 4d6573736167653630 39930cbe27f22e6b
# Success! 60/64 valid tokens verified

# Attempt 121/128
# Enter your message and token: 4d6573736167653631 4d6573736167653631
# Invalid token! Expected token: c489efaac72afa24

# Attempt 122/128
# Enter your message and token: 4d6573736167653631 c489efaac72afa24
# Success! 61/64 valid tokens verified

# Attempt 123/128
# Enter your message and token: 4d6573736167653632 4d6573736167653632
# Invalid token! Expected token: 16c5f54e40c49f01

# Attempt 124/128
# Enter your message and token: 4d6573736167653632 16c5f54e40c49f01
# Success! 62/64 valid tokens verified

# Attempt 125/128
# Enter your message and token: 4d6573736167653633 4d6573736167653633
# Invalid token! Expected token: f9760c6d89bd15ef

# Attempt 126/128
# Enter your message and token: 4d6573736167653633 f9760c6d89bd15ef
# Success! 63/64 valid tokens verified

# Attempt 127/128
# Enter your message and token: 4d6573736167653634 4d6573736167653634
# Invalid token! Expected token: 50d8fe86b977e7ff

# Attempt 128/128
# Enter your message and token: 4d6573736167653634 50d8fe86b977e7ff
# Success! 64/64 valid tokens verified

# Đã thu thập đủ 64 token!
# [+] Receiving all data: Done (124B)
# [*] Closed connection to 34.45.235.239 port 8004

# Congratulations! You beat the challenge!
# flag{C0ngr4ts_0n_f1nd1ng_Th1s_H4sh_c0ll1s10ns_N0w_G0_h4v3_4_D0ubl3_Ch33s3_Burg3r}