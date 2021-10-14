# Performs a circular left shift of one (1) position
def circular_left_shift_1(key):
    # Divide input into 5-bit pairs
    result_key = ""
    left_shift_guide = [1,2,3,4,0]
    for position in left_shift_guide:
        result_key += key[position]
    print(f"Output of circular left shift 1: {result_key}")
    return result_key

# Performs a circular left shift of two (2) positions
def circular_left_shift_2(key):
    # Divide input into 5-bit pairs
    result_key = ""
    left_shift_guide = [2,3,4,0,1]
    for position in left_shift_guide:
        result_key += key[position]
    print(f"Output of circular left shift 2: {result_key}")
    return result_key

# Permutation 10.
def P10(key):
    # Output
    permutated_key = ""
    # Permutation table = 3,5,2,7,4,10,1,9,8,6
    permutation_table = [3,5,2,7,4,10,1,9,8,6]
    for position in permutation_table:
        permutated_key += key[position-1]

    print(f"P10 output: {permutated_key}")
    return permutated_key

# Picks out and permutes 8 og the 10 bits
def P8(key):
    # Output
    permutated_key = ""
    # Permutation table = 6,3,7,4,8,5,10,9
    permutation_table = [6,3,7,4,8,5,10,9]
    for position in permutation_table:
        permutated_key += key[position-1]

    print(f"P8 output: {permutated_key}")
    return permutated_key

# Generate two 8-bit subkeys from the 10-bit input
def key_generation(key):
    # First permutate the key using P10
    p10_key = P10(key)
    # Next, perform a circular left shift (LS-1) on the first five bits and second five bits
    left_key = p10_key[0:5]
    right_key = p10_key[5:10]
    left_shifted_left_key = circular_left_shift_1(left_key)
    left_shifted_right_key = circular_left_shift_1(right_key)
    # Next we apply P8 which picks and permutes 8 of the 10 bits
    # The result is subkey 1
    joined_key = left_shifted_left_key + left_shifted_right_key
    k1 = P8(joined_key)
    print(f"Subkey 1: {k1}")
    # Go back to the pair of 5-bit strings produced by the two LS-1 functions
    # And perform a circular left shift of 2 bit positions on each string
    double_left_shifted_left_key = circular_left_shift_2(left_shifted_left_key)
    double_left_shifted_right_key = circular_left_shift_2(left_shifted_right_key)
    # Finally, P8 is applied again to produce k2
    joined_key = double_left_shifted_left_key + double_left_shifted_right_key
    k2 = P8(joined_key)
    print(f"Subkey 2: {k2}")
    
    return (k1, k2)

#Initial permutation
def IP(plaintext):
    # Output
    permutated_plaintext = ""
    # Permutation table = 2,6,3,1,4,8,5,7
    permutation_table = [2,6,3,1,4,8,5,7]
    for position in permutation_table:
        permutated_plaintext += plaintext[position-1]

    print(f"IP output: {permutated_plaintext}")
    return permutated_plaintext

# Inverse initial permutation
def IP_1(plaintext):
    # Output
    permutated_plaintext = ""
    # Permutation table = 4,1,3,5,7,2,8,6
    permutation_table = [4,1,3,5,7,2,8,6]
    for position in permutation_table:
        permutated_plaintext += plaintext[position-1]

    print(f"Inverse IP output: {permutated_plaintext}")
    return permutated_plaintext

# Combination of permutation and substitution functions
def f_k(left_input, right_input, subkey):
    a=1
    
# Mapping from 4-bit strings to 4-bit strings
# Input is a 4-bit number
def F(plaintext, subkey):
    # The first operation is an expansion/permutation operation
    # Output
    permutated_plaintext = ""
    # Permutation table = 4,1,2,3,2,3,4,1
    expansion_permutation_table = [4,1,2,3,2,3,4,1]
    for position in expansion_permutation_table:
        permutated_plaintext += plaintext[position-1]

    print(f"F function output: {permutated_plaintext}")
    
    # The 8-bit subkey k1 is added to this value using XOR
    P_string = ""
    for index, plaintext_bit in enumerate(permutated_plaintext):
        P_string += XOR(plaintext_bit, subkey[index])
        
    print(f"P string value: {P_string}")
    
    # The first 4 bits (first row of the P_string matrix)
    # are fed into the S-box s0 to produce a 2-bit output
    # The remaining 4 bits (second row) are def into S1 to produce another 2-bit output

def XOR(plaintext_bit, subkey_bit):
    # ^ is the bitwise XOR in python
    n = int(plaintext_bit)
    k = int(subkey_bit)
    #print(f"{n} XOR {k} = {n^k}")
    return str(n^k)

def encryption(plaintext, key):
    k1, k2 = key
    initial_permutation = IP(plaintext)
    left_input = initial_permutation[0:4]
    right_input = initial_permutation[4:8]
    
    F(right_input, k1)

def main():
    # 10-bit key
    key = "1010000010"
    # 8-bit plaintext
    plaintext = "10010110"
    # Generate subkeys from the key
    key = key_generation(key)
    
    #Encrypt the plaintext using the key
    encryption(plaintext, key)

if __name__ == "__main__":
    main()