from rsa import generate_keys

def message_interface(public_key, private_key):
    """Yksinkertainen konsolipohjainen käyttöliittymä, jossa käyttäjä voi lähettää ja vastaanottaa RSA:lla salattuja viestejä.
    """

    print("Interface started\n")
    
    N, e = public_key
    _, d = private_key

    messages = []

    print("Your private key:", d)
    print("Press enter to continue once you've copied your private key.")
    input()

    while True:
        print("Enter 's' to send a message, 'r' to receive the last message from the queue or 'q' to quit:")
        mode = input().strip().lower()

        if (mode != 's' and mode != 'r' and mode != 'q'):
            print(mode)
            print("Enter 's', 'r' or 'q'.\n")
            continue

        elif (mode == 's'):
            print("Enter a message:")
            message = int.from_bytes(input().strip().encode())
            encrypted_message = pow(message, e, N)
            messages.append(encrypted_message)
            print("\nEncrypted message:", encrypted_message, "appended to queue.\n")
        
        elif (mode == 'r'):
            print("Enter your private key:")
            pk = int(input().strip())
            if (pk != d):
                print("Wrong private key.\n")
                continue
            
            if len(messages) != 0:
                encrypted_message = messages.pop()
                decrypted_message_in_ints = pow(encrypted_message, d, N)
                bytes_len = decrypted_message_in_ints.bit_length() + 7 // 8
                decrypted_message = decrypted_message_in_ints.to_bytes(bytes_len).decode()
                print("\nDecrypted message:", decrypted_message, "\n")
            else:
                print("No messages in queue.")
            continue
    
        elif (mode == 'q'):
            return

if __name__ == "__main__":
    public_key, private_key = generate_keys()
    message_interface(public_key, private_key)