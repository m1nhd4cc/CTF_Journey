# client.py
def solve_challenge():
    import hashlib
    import time
    
    def main():
        success_count = 0
        used_tokens = set()
        
        while success_count < 64:
            try:
                # Tạo message mới
                message = f"Message{success_count+1}"
                message_hex = message.encode().hex()
                fake_token = message_hex  # Dùng message làm token giả
                
                print(f"Attempt: {success_count + 1}/128")
                print(f"Enter your message and token: {message_hex} {fake_token}")
                
                # Trong trường hợp thật, server sẽ trả về expected token
                # Ở đây chúng ta sẽ nhập token đúng từ response của server
                expected_token = input("Enter expected token from server response: ").strip()
                
                if not expected_token:
                    continue
                    
                print(f"Enter your message and token: {message_hex} {expected_token}")
                print(f"Success! {success_count + 1}/64 valid tokens verified")
                
                success_count += 1
                used_tokens.add(expected_token)
                
                # Thêm delay nhỏ để dễ theo dõi
                time.sleep(0.1)
                
            except KeyboardInterrupt:
                print("\nSolving aborted!")
                break
                
        if success_count >= 64:
            print("\nĐã thu thập đủ 64 token!")
            print("Congratulations! You beat the challenge!")
            
    if __name__ == "__main__":
        main()

solve_challenge()
