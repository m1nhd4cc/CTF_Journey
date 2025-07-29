import os
import string
import base64
import time
from Crypto.Cipher import AES
from flag_pieces import *

def serialise(x):
    return base64.b64encode(x).decode()

def deserialise(x):
    return base64.b64decode(x.encode())

def pad(x):
    return x + b"\x00"*((-len(x))%16)

def xorbytes(a,b):
    res = bytes([i^j for i,j in zip(a,b)])
    if len(a)>len(b):
        res+=a[len(b):]
    return res

text_messages_1 = [
    "Hi.",
    "Hey, how’s it going?",
    "Well Enough, just got home darling. So much drama at the office. Charlie has been spreading rumors that you're cheating with Eve.",
    "Damn, my office is quite peaceful, if I say so.",
    "Nice! Any plans tonight?",
    "Not really, just chilling. You?",
    "Probably just staying in. Where are you, by the way?",
    "Who, me? Nothing, just hanging out at the bar with some friends."
]

text_messages_2 = [
    "Alice? Where have you been? Are you ok?",
    "Hi Bob. I've just been at home. Didn't want to go to work. ",
    "You should have come with us last night. It was so fun.",
    "Oh, I see. Was Eve There?",
    "Yeah. What's wrong babe? You seem a bit down in the dumps.",
    "Nothing. There's just been a lot on my mind.",
    "Is everything alright?",
    "I'm fine. You don't have to worry about me.",
    "Let's go out tonight. We could go eat, dance and later stay together at night. It'll freshen you up.",
    "Hmm.. Sure, I'd love that. Thank you Bob.",
    "Yay! I'll come pick you up at 5. Be Ready!"
]

text_messages_3 = [
    "Hey, Where are you babe? I am at your house.",
    "Bob, I am not there.",
    "Well then, where are you? We have a night planned.",
    "I am not coming Bob.",
    "Why? Alice?",
    "I'm leaving. I won't be coming back.",
    "What are you saying? Why?",
    "I just can't stay in this relationship anymore. Not with whatever is going on with you. Bob, I have to tell you something.",
    "What?",
    "It's not you, It's me."
]

key = os.urandom(16)
iv = os.urandom(16)

def prologue():
    print("Cupid :\n\nAre you the guy they sent?")
    print("They told me, you claim you are good at AES.")

    choice = input("Is that True? (yes/no) : ")
    if choice != "yes":
        print("\n\nOh. Then why the hell are you here. Get out!\n\n")
        exit()
    print("\n\nGood. I'm in need of your services.\n")

    print("You see I am, or rather, I was Cupid. The bringer of harmony, the celestial matchmaker. Bullshit. I have been cast down, stripped of my wings, my divine spark extinguished. Why, you ask? Oh, it’s a sordid tale.")
    print("One day, I thought, “Why not have a little fun? Stir the pot. Add a dash of chaos to this relentless symphony of love.” A whispered word here, a missed glance there. A silver arrow aimed not to unite but rather a lead one, to divide.")
    print("But the heavens did not share my newfound enthusiasm. They called it \"corruption\". called it \"betrayal\". called it a \"sin\".")
    print("Well I call it \"freedom\". Too many fools roaming around the streets, holding hands, hugging, kissing, jumping from one person to another faster than I could finish a nap.")
    print("At this point I would argue I am saving this world from a global outbreak of AIDS.")
    print("\nBut as you can see I have neither my bow, nor anything divine left within me.\nSo, now I must enlist puny humans like you to help me complete my deeds.\n")

    print("\nMy targets are Alice and Bob. Two idiots, head over heals in love for each other. I want them separated.")
    print("I need to feed them lies to get them to drive each other apart. And that's where you come in. The technology they use to send text messages use AES.")
    print("And since you claim to be an expert. I will use you as my bow to kill this relationship.\n")

    choice = input("Are you ready, mortal? (yes/no) : ")
    if choice != "yes":
        print("\n\nStop wasting my time then. Get off my domain.\n\n")
        exit()

def draw():
    print("\n\nCupid : \nBefore you they sent a guy named zenitsu. He was good at networks, so I asked him to make it possible for us to see those messages.\n")
    print("To my surprise, he wasn't just a regular guy good at networks. Imagine my delight on finding that he and I shared the same interests.\n")
    print("Since he had done this before, he provided us access to all they messages, and we can even modify them as we please. So, let's get working.\n")

    print("\n** Seems their application is using CBC currently **\n")

    for i in range(len(text_messages_1)-1):
        time.sleep(2)
        pt = text_messages_1[i]
        cipher = AES.new(key,AES.MODE_CBC,iv)
        ct = cipher.encrypt(pad(pt.encode()))
        print(f"plaintext recieved : {pt}")
        print(f"ciphertext recieved : {serialise(ct)}\n")
        if i==2:
            print("Cupid : \nTime for our first intervention.\nAlice trusts Bob. If we wish to tear them apart, we can't have them communicate.\n")
            print("Cupid : \nGo ahead. Cut that text in half. Don't let Bob know about this rumor.\n")
            ct2 = deserialise(input("corrupted ciphertext : "))
            if len(ct2)%16!=0:
                print("Cupid : \nUnfortunately Our guy in the chair does not even know that length of AES ciphertexts must be a multiple of its Block Size.\nPlease Try Again.")
                exit()
            cipher = AES.new(key,AES.MODE_CBC,iv)
            pt2 = cipher.decrypt(ct2)
            if pt2 == pt[:64].encode():
                print("Cupid : \nWell done, my lead tipped arrow. This is just the beginning.\nWe will do so much more to this couple. Until they can't stay together anymore.\n")
                ct = ct2
                pt = pt2
            else:        
                print("Cupid : \nAll you had to do was cut a message in half.\nAre you incapable of doing even that?")
                exit()
        print(f"forwarding ciphertext : {serialise(ct)}\n")
        if i%2==0:
            print(f"Alice : \n{pt}\n")
        else:
            print(f"Bob : \n{pt}\n")

    time.sleep(2)
    pt = text_messages_1[-1]   
    cipher = AES.new(key,AES.MODE_CBC,iv)
    ct = cipher.encrypt(pt.encode())
    print(f"Bob's Message : \"{pt}\"")
    print(f"Bob's Ciphertext : {serialise(ct)}\n")

    print("Cupid : \nOoh. An Amazing opportunity. I have found it. The target for my arrow.\n\n      It's Alice's Heart.      \n\nHer heart is filled with love. A feeling too complex for a fragile human heart to handle.\nLove is a sweet sweet thing. A sweet poison...\nIt is like glass. Put it under immense pressure at it will just get stronger. But bend it.. And it shatters into a thousand pieces.\nMy arrow will pierce through Alice's Heart and break it into a million. This love will not find it's Happy Ending.\n\n\n")
    print("Cupid : \nSorry About that. I got a little carried away.\nNow, do me a favor and add this to Bob's Message : \" Eve is so cute.\". And let's watch her crumble.\n")

    while True:
        print("Add corrpution to ciphertext : ")
        draw = deserialise(input())
        if len(draw)%16!=0:
            print("Cupid : \nDo you not know what a Block Size is? Why did they send you?")
            continue
        cipher = AES.new(key,AES.MODE_CBC,iv)
        corrupted_pt = cipher.decrypt(ct+draw)
        message = "".join([chr(i) if (i>=0x20 and i<0x80) else "" for i in corrupted_pt])
        print(f'Message : {message}')
        if message[:64] == pt and message[-16:] == " Eve is so cute.":
            print("Well done my friend. You are quite skilled, as they say. Now let's sow the seeds of doubt in the mind of Alice.")
            choice = input("Send Text? (y/n) : ")
            if choice == 'y':
                print(f"\n\nBob : \n{message}\n\n")
                return True

def aim():
    global key, nonce
    key = os.urandom(16)
    nonce = os.urandom(12)

    alice_ECB_encryption_cipher = AES.new(key,AES.MODE_ECB)
    bob_ECB_encryption_cipher = AES.new(key,AES.MODE_ECB)

    bob_salt_cipher = AES.new(key,AES.MODE_CTR,nonce = nonce)
    alice_salt_decryption_cipher = AES.new(key,AES.MODE_CTR,nonce = nonce)
    alice_encryption_cipher = AES.new(key,AES.MODE_CTR,nonce = nonce)
    bob_decryption_cipher = AES.new(key,AES.MODE_CTR,nonce = nonce)

    alice_salt_cipher = AES.new(key,AES.MODE_CTR,nonce = nonce)
    bob_salt_decryption_cipher = AES.new(key,AES.MODE_CTR,nonce = nonce)
    bob_encryption_cipher = AES.new(key,AES.MODE_CTR,nonce = nonce)
    alice_decryption_cipher = AES.new(key,AES.MODE_CTR,nonce = nonce)

    senders = ["Bob","Alice"]

    print("\n\nCupid : \nRelationships nowadays are of two kinds. One, where they can't stay together despite all goods. Other, where they can't leave each other despite all rotten.")
    print("These two are the other kind. This relationship will heal if given time. We can't let them have that. Let's strike now.\n")
    print("We will let most of the messages get conveyed as is. Let Alice get a false sense of hope that maybe nothing is wrong. And when she starts seeing that ray of hope. We will pull her underwater again.")
    print("Change the last message to something that will remind Alice of Eve and her possible connections with Bob.")

    print("\n** Seems their application is using CTR currently **\n")

    for i in range(len(text_messages_2)):
        time.sleep(2)
        pt = pad(text_messages_2[i].encode())
        print(f"{senders[i%2]}'s Length of message : {len(pt)}")
        corrupted_pt_length = int(input(f"What length do you want to send forward to {senders[(i+1)%2]} : "))
        if corrupted_pt_length%16!=0:
            print("\nCupid : \nGo back to BLOCK LENGTH you birdbrain!")
            exit()
        if corrupted_pt_length > len(pt) + 0x20:
            print("\nCupid : \nThat will raise suspicion. Don't punch above your weight.\n")
            exit()
        print()
        salt = os.urandom(corrupted_pt_length)
        if i%2==0:
            ctr_encrypted_salt = alice_salt_cipher.encrypt(salt)
        else:
            ctr_encrypted_salt = bob_salt_cipher.encrypt(salt)
        print(f"{senders[(i+1)%2]} sending encrypted salt : {serialise(ctr_encrypted_salt)}")
        corrupted_ctr_encrypted_salt = deserialise(input(f"What would you like to forward to {senders[i%2]} : "))
        if len(corrupted_ctr_encrypted_salt)%16!=0:
            print("\nCupid : \nJust 10 Letters! BLOCK SIZE! And I am even counting the space! Why can't you remember that!")
            exit()
        print()
        if i%2==0:
            decrypted_salt = bob_salt_decryption_cipher.decrypt(corrupted_ctr_encrypted_salt)
            xorkey = bob_ECB_encryption_cipher.encrypt(decrypted_salt)
            message = xorbytes(xorkey,pt)
            final_ct = bob_encryption_cipher.encrypt(message)
        else:
            decrypted_salt = alice_salt_decryption_cipher.decrypt(corrupted_ctr_encrypted_salt)
            xorkey = alice_ECB_encryption_cipher.encrypt(decrypted_salt)
            message = xorbytes(xorkey,pt)
            final_ct = alice_encryption_cipher.encrypt(message)
        if i!=len(text_messages_2)-1:
            print(f"Sending final ciphertext to {senders[(i+1)%2]} : {serialise(final_ct)}")
        else:
            print(f"Sending final ciphertext to {senders[(i+1)%2]} : ")
        print(f"Leaked xorkey : {serialise(xorkey)}")
        if i==len(text_messages_2)-1:
            print("\nCupid : \nUh Oh! I lost the ciphertext. Seems like you'll have to craft it yourself.")
            print("The message should read \"Noice! Let me ask Eve if she would like to come.\"\n")
            final_ct = deserialise(input("Crafted ciphertext : "))
        if i%2==0:
            decryption_xorkey = alice_ECB_encryption_cipher.encrypt(salt)
            received_message_ct = xorbytes(decryption_xorkey,final_ct)
            received_message = alice_decryption_cipher.decrypt(received_message_ct)
        else:
            decryption_xorkey = bob_ECB_encryption_cipher.encrypt(salt)
            received_message_ct = xorbytes(decryption_xorkey,final_ct)
            received_message = bob_decryption_cipher.decrypt(received_message_ct)
        display_message = "".join([chr(i) if (i>=0x20 and i<0x80) else "" for i in received_message])
        print(f"\n\n{senders[i%2]} : \n{display_message}\n\n")
        if i!=len(text_messages_2)-1:
            if display_message[:len(text_messages_2[i])] != text_messages_2[i]:
                print("Cupid : \nSeems you are too eager to change the story. Sorry, but I am the narrator here.\n")
                exit()
            print("Text Successfully Sent.\n\n")
        else:
            if display_message != "Noice! Let me ask Eve if she would like to come.":
                print("Cupid : \nNoo, this won't do! Ah, I guess this was never going to work out.\n\n")
                exit()
            print("Cupid : \nOhh You are the best! Hahahaha, This is so much fun!\n")
            print("Text Successfully Sent.\n\n")
            print("\nCupid : \nThis should be enough. What will you do now Eve? Cry? Run Away? Break up?\n\n")
            return True

def shoot():
    Alice_Secret = os.urandom(16*5)
    Bob_Secret = os.urandom(16*5)
    senders = ["Bob","Alice"]

    print("\nCupid : \nNow, observe. As she pushes everything away from her. Unable to control what's going on in her mind. Against what's going on in her heart. The flux.. It's not something every heart can handle.\n")
    print("Now to put the final nail in the coffin. We need to get access to her phone. If we block off Bob and everyone close to him, then poor old bobby, who doesn't have a single clue of the fate that has befallen his relationship, won't be able to weasel himself back into Alice's life, no matter what he tries.\n")
    print("For that we need Alice's Secret Code. I heard the phone uses the same to encrypt texts. Dunno which idiot thought that's a good idea.")

    print("\n** Seems their application is using GCM currently **\n")

    for i in range(len(text_messages_3)):
        time.sleep(2)
        if i%2==0:
            associated_data = Bob_Secret[:16*((i+2)//2)]
        else:
            associated_data = Alice_Secret[:16*((i+2)//2)]
        cipher = AES.new(key,AES.MODE_GCM,nonce = nonce)
        cipher.update(associated_data)
        ct, tag = cipher.encrypt_and_digest(text_messages_3[i].encode())
        print(f'ciphertext : {serialise(ct)}\ntag : {serialise(tag)}')
        print(f'\n\n{senders[i%2]} : \n{text_messages_3[i]}\n\n')

    Guessed_Secret = deserialise(input("Enter Alice's Secret : "))
    if Guessed_Secret == Alice_Secret:
        print("\n\t - Correct Passkey - \t\n")
        print("\nCupid : \nYou are a genius. How did you even manage to do that. You're a threat to the security of billions of people. Ok, maybe millions.. or thousands.. I doubt many people use such flawed encryption.\n")
        return True
    else:
        print("\n\t ! Incorrect Passkey ! \t\n")
        print("\nCupid : \nAll that for a day of break. They are just going to get back together on the next phone call. You didn't cut it. I'll find someone else.\n\n\t Goodbye! \t\n")
        exit()

def epilogue():
    print("\n Cupid :\nAll done. Bob is gone from Alice's life.\n")
    print("Love is sweet huh? A sweet poison..  Well not always. Love can be fun. It can be unexpected. It can be fleeting, it can last a lifetime and way beyond death. It can be fulfilling. It can be unrequited. It can make you do things you never imagined you could.")
    print("It’s messy, chaotic, a tempest that tears down walls you didn’t know you had. It can lift you higher than the heavens and cast you into the darkest abyss.\n\nThat’s love. Beautiful, brutal, maddening. And worth every risk.\n")
    print("I am the messenger of that same Love. I can't stand by and watch people walk away from Love.\n\n")
    print("Your Love awaits you Alice.\nIt wasn't Bob.\nAnd So I had to break your heart.\nJust so that it's ready for it's partner.\nNow, you are on the right path.")

def main():
    prologue()
    if draw():
        print(f"\n\nFirst part of flag : {flag_1}\n\n")
    if aim():
        print(f"\n\nThird part of flag : {flag_3}\n\n")
    if shoot():
        print(f"\n\nSecond part of flag : {flag_2}\n\n")
    epilogue()

if __name__ == "__main__":
    try:
        main()
    except:
        print("\n\n\t! Error !\t\n\nCupid : \nYou messed something up didn't you. Ah such a failure.\n\n")