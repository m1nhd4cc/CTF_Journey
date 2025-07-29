# server.py
import hashlib
import os
from typing import Dict, Set

class HashCollisionServer:
    def __init__(self):
        self.required_successes = 64
        self.success_count = 0
        self.used_tokens = set()
        self.secret_key = os.urandom(16)  # Random key cho mỗi session
        self.flag = "flag{C0ngr4ts_0n_f1nd1ng_Th1s_H4sh_c0ll1s10ns_N0w_G0_h4v3_4_D0ubl3_Ch33s3_Burg3r}"
        
    def generate_token(self, message: str) -> str:
        """Tạo token cho message bằng cách hash với secret key"""
        data = message.encode() + self.secret_key
        return hashlib.sha256(data).hexdigest()[:16]
    
    def check_message(self, message: str, token: str) -> tuple[bool, str]:
        """Kiểm tra message và token"""
        expected_token = self.generate_token(message)
        
        if token in self.used_tokens:
            return False, "Token already used!"
            
        if token != expected_token:
            return False, f"Invalid token! Expected token: {expected_token}"
            
        self.used_tokens.add(token)
        self.success_count += 1
        return True, f"Success! {self.success_count}/64 valid tokens verified"
    
    def is_complete(self) -> bool:
        return self.success_count >= self.required_successes

def main():
    server = HashCollisionServer()
    print("Welcome to Hash Collision Challenge!")
    print("Find 64 valid tokens to get the flag")
    print("Example: 48656c6c6f 1234567890abcdef")
    print()
    
    attempt = 1
    while not server.is_complete():
        print(f"Attempt: {attempt}/128")
        try:
            user_input = input("Enter your message and token: ").strip()
            if not user_input:
                continue
                
            try:
                message, token = user_input.split()
            except ValueError:
                print("Invalid format! Use: <message> <token>")
                continue
            
            success, response = server.check_message(message, token)
            print(response)
            
            if server.is_complete():
                print("\nĐã thu thập đủ 64 token!")
                print("Congratulations! You beat the challenge!")
                print(server.flag)
                break
                
            attempt += 1
            if attempt > 128:
                print("Too many attempts! Challenge failed.")
                break
                
        except KeyboardInterrupt:
            print("\nChallenge aborted!")
            break
            
if __name__ == "__main__":
    main()
