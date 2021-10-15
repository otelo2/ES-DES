from SDES.encrypter import IP, f_k, SW, IP_1

def decryption(cyphertext, key):
    k1, k2 = key
    initial_permutation = IP(cyphertext)
    
    left_input = initial_permutation[0:4]
    right_input = initial_permutation[4:8]
    
    # First round of f_k function
    left_input = f_k(left_input, right_input, k2)

    # Perform swap function
    print("Start of swap function")
    left_input, right_input = SW(left_input, right_input)
    print("-------------")
    print("End of swap function")
    
    # Now apply the function to the other half of the input
    left_input = f_k(left_input, right_input, k1)
    
    #Finally perform inverse initial permutation
    plaintext = IP_1(left_input + right_input)
    
    print(f"Plaintext: {plaintext}")
    
    return plaintext