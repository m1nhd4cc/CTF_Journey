#!/usr/local/bin/python3

import os
import time
import hashlib
import random
import sys
import math
import sympy
from Crypto.Util.number import getPrime
from Crypto.Hash import SHAKE256

sys.set_int_max_str_digits(10000)

FLAG = os.getenv("FLAG", "DDC{FAKE_FLAG_FAKE_FLAG}")

p = getPrime(1024)
q = getPrime(1024)
N = p * q
L_BITS = 256

POKEMON_PRICE = 2**8
FLAG_PRICE = 2**256

POKEMON_LIST = [
    "Pikachu", "Charizard", "Blastoise", "Venusaur", "Gengar", 
    "Dragonite", "Mewtwo", "Alakazam", "Machamp", "Golem"
]

class PokeShop:
    def __init__(self):
        self.coins = 0
        self.pokemon_owned = []
        self.challenges_solved = 0
        
    def show_shop(self):
        print("Welcome to the PokeShop!")
        print("=" * 40)
        
        print("1. View Status")
        print("2. Earn coins")
        print("3. Buy Pokemon (Random) - 2^8 coins")
        print("4. Buy FLAG - 2^256 coins")
        print("5. Show Menu")
        print("6. Exit")
        print("=" * 40)

    def buy_pokemon(self):
        if self.coins < POKEMON_PRICE:
            print(f"Not enough coins! You need {POKEMON_PRICE} coins.")
            print(f"You have: {self.coins} coins")
            return False
            
        available_pokemon = [p for p in POKEMON_LIST if p not in self.pokemon_owned]
        if not available_pokemon:
            print("You already own all Pokemon!")
            return False
            
        pokemon = random.choice(available_pokemon)
        self.coins -= POKEMON_PRICE
        self.pokemon_owned.append(pokemon)
        
        print(f"Congratulations! You caught {pokemon}!")
        print(f"Remaining coins: {self.coins}")
        return True
        
    def buy_flag(self):
        if self.coins < FLAG_PRICE:
            print(f"Not enough coins! You need {FLAG_PRICE} coins.")
            print(f"You have: {self.coins} coins")
            return False
            
        self.coins -= FLAG_PRICE
        print("FLAG PURCHASED!")
        print(f"Flag: {FLAG}")
        return True
        
    def view_collection(self):
        print(f"Your coins: {self.coins}")
        print(f"Pokemon owned: {len(self.pokemon_owned)}")
        print()
        if not self.pokemon_owned:
            print("No Pokemon in your collection yet!")
        else:
            print("Your Pokemon Collection:")
            for i, pokemon in enumerate(self.pokemon_owned, 1):
                print(f"  {i}. {pokemon}")
        print()

def hash_to_prime(data, bits=256):
    counter = 0
    while True:
        hash_input = counter.to_bytes(4, 'big') + data
        digest = hashlib.sha256(hash_input).digest()
        candidate = int.from_bytes(digest, 'big')
        
        candidate = candidate % (2**bits)
        if candidate < 2**(bits-1):
            candidate += 2**(bits-1)
        
        if candidate % 2 == 0:
            candidate += 1
        
        if sympy.isprime(candidate):
            return candidate
        
        counter += 1



def hash_to_group(m, N):
    ctr = 0
    while True:
        hash_input = ctr.to_bytes(4, 'big') + m
        shake = SHAKE256.new(hash_input)
        digest = shake.read(256)
        y = int.from_bytes(digest, 'big') % N
        
        if math.gcd(y, N) == 1:
            return y
        
        ctr += 1

def timestamp_to_x(N, timestamp):
    timestamp_data = timestamp.to_bytes(8, 'big')
    x = hash_to_group(timestamp_data, N)
    return x

def verify_proof(N, T, x, y, pi, ell):
    try:
        r = pow(2, T, ell)
        left = (pow(pi, ell, N) * pow(x, r, N)) % N
        right = y % N
        return left == right
    except:
        return False

def crypto_challenge(shop):
    print("How many coins do you want to earn?")
    try:
        T = int(input("Enter reward amount: "))
    except:
        print("Invalid reward amount!")
        return
    
    if T <= 0:
        print("Reward amount must be positive!")
        return
    
    current_time = int(time.time())
    x = timestamp_to_x(N, current_time)
    
    print(f"Challenge Parameters:")
    print(f"   N = {N}")
    print(f"   T = {T}")
    print(f"   x = {x}")
    print()
    print("Step 1: Compute y = x^(2^T) mod N")
    
    try:
        y = int(input("y = "))
        
        data = x.to_bytes(256, 'big') + y.to_bytes(256, 'big')
        ell = hash_to_prime(data, L_BITS)
        print(f"ell = {ell}")
        print()
        
        print("Step 2: Compute pi = x^(2^T // ell) mod N")
        pi = int(input("pi = "))
    except:
        print("Invalid input format!")
        return
    
    if verify_proof(N, T, x, y, pi, ell):
        shop.coins += T
        shop.challenges_solved += 1
        
        print("Proof Verified!")
        print(f"Earned {T} coins")
        print(f"Total coins: {shop.coins}")
    else:
        print("Invalid proof!")
    
    print()

def main():
    shop = PokeShop()
    
    shop.show_shop()
    while True:
        try:
            choice = input("Choose option (1-6): ").strip()
            
            if choice == "1":
                shop.view_collection()
            elif choice == "2":
                crypto_challenge(shop)
            elif choice == "3":
                shop.buy_pokemon()
            elif choice == "4":
                if shop.buy_flag():
                    break
            elif choice == "5":
                shop.show_shop()
            elif choice == "6":
                print("Thanks for visiting PokeShop! Come back soon!")
                break
            else:
                print("Invalid option! Choose 1-6.")
            
            print()
            
        except (EOFError, KeyboardInterrupt):
            print("\nThanks for playing! Goodbye!")
            break
        except Exception as e:
            print(f"System error: {e}")

if __name__ == "__main__":
    main()