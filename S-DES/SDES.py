from key_generator import key_generation
from encrypter import encryption
from decrypter import decryption

def main():
    # 10-bit key
    key = "1010000010"
    print(f"Key: {key}")
    # 8-bit plaintext
    plaintext = "10010110"
    print(f"Plaintext: {plaintext}")
    # Generate subkeys from the key
    print("-------------")
    print("Start of key generation process")
    generated_key = key_generation(key)
    print("End of key generation process")
    print("-------------")
    
    # Encrypt the plaintext using the key
    print("-------------")
    print("Start of encryption process")
    cyphertext = encryption(plaintext, generated_key)
    print("End of encryption process")
    print("-------------")
    
    # Decrypt the plaintext using the key
    print("-------------")
    print("Start of decryption process")
    decrypted_plaintext = decryption(cyphertext, generated_key)
    print("End of decryption process")
    print("-------------")
    
    # Show final results
    print("------------")
    print(f"Key: {key}")
    print(f"Plaintext: {plaintext}")
    print(f"Cyphertext: {cyphertext}")
    print(f"Decrypted plaintext: {decrypted_plaintext}")

if __name__ == "__main__":
    main()