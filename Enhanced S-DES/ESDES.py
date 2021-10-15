from SDES.encrypter import encryption
from SDES.key_generator import key_generation
from SDES.decrypter import decryption
from encrypt_scttmr import simple_columnar_transposition
from decrypt_scttmr import decrypt_simple_columnar_transformation

# First process the Simple Columnar Transposition Technique with Multiple Rounds (SCTTMR)
# Then the output comes from SCTTMR will gain indergone Shift Rows Stage (sic)
# The plaintext message is first converted into the cipher text by using SCTTMR with min. 1 or 2 rounds
# The output from Shift row is then converted into a bit form because the S-DES applies its process on bit level as usual

def text_into_binary(text):
    # Turn the each letter of the input into binary
    binary_input = "".join(format(ord(i), "08b") for i in text)
    binary_input_list = [binary_input[i:i+8] for i in range(0, len(binary_input), 8)]
    
    return binary_input_list

def binary_into_text(binary):
    result = ""
    for binary_value in binary.split():
        an_int = int(binary_value, 2)
        ascii_char = chr(an_int)
        result += ascii_char
    return result


def main():
    print("************")
    input_plaintext = "DID YOU SEE"
    print(f"Plaintext: {input_plaintext}")
    SCT_result = simple_columnar_transposition(input_plaintext)
    print(f"SCTTMR result: {SCT_result}")
    
    #
    # Encrypt using S-DES
    #
    
    key = "0010010111"
    print(f"Key: {key}")
    key = key_generation(key)
    
    # Encrypt each letter
    print("************")
    print("Start Enhanced S-DES encryption process")
    
    binary_input_list = text_into_binary(SCT_result)
    cyphertext = ""
    print(binary_input_list)
    for binary_letter in binary_input_list:
        cyphertext += encryption(binary_letter, key)
        print("Joining result with the rest of the cyphertext...")
    print("************")
    print("End of Enhanced S-DES encryption process")
    # Show the result as hex
    decimal_cypher = int(cyphertext, 2)
    hex_cypher = hex(decimal_cypher)
    print(f"Hex output of DES encryption: {hex_cypher}")
    
    #
    # Decrypt using DES
    #
    #
    #print("************")
    #print("Start Enhanced S-DES decryption process")
    #cyphertext_binary_list = text_into_binary(cyphertext)
    #
    #binary_decryption = ""
    #for cyphertext_fragment in cyphertext_binary_list:
    #    binary_decryption += decryption(cyphertext_fragment, key) + " "
    #    print("Joining result with the rest of the 'plaintext'...")
    #print("************") 
    #print("End of Enhanced S-DES decryption process")
    ## Convert binary string to ascii string
    #print(binary_decryption)
    #
    #plaintext_for_SCT = binary_into_text(binary_decryption)
    #
    #print(f"Plaintext for SCT: {plaintext_for_SCT}")
    #
    ## Start decryption of SCT
    #
    #decrypt_simple_columnar_transformation(plaintext_for_SCT)
    

if __name__ == "__main__":
    main()
