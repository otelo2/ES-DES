# Functions used by the key generation process

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

# Picks out and permutes 8 of the 10 bits
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