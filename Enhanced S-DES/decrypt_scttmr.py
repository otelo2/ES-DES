from encrypt_scttmr import plaintext_into_columns, print_columns, read_columns, transposition


# Simple permutation
def inverse_shift_row(rows):
    # First row is not altered.
    # Second row is circular left shifted 2 bytes
    print_columns(rows)
    rows[0][1], rows[1][1], rows[2][1] = rows[2][1], rows[0][1], rows[1][1]
    # Third row is circular left shifter 1 byte
    rows[0][2], rows[1][2], rows[2][2] = rows[1][2], rows[2][2], rows[0][2]
    
    return rows

def read_rows(rows):
    round_1_result = ""
    for num1 in range(3):
        for num2 in range(3):
            round_1_result += round_1_result.join((rows[num2][num1]))
    return round_1_result

def decrypt_simple_columnar_transformation(ciphertext):
    # Random selection of columns for the rounds
    round_1 = [3, 1, 2]
    round_2 = [3, 1, 2]
    
    # Write the plaintext into the columns
    columns = plaintext_into_columns(ciphertext)
    print_columns(columns)
    
    # Perform inverse row shift
    columns = inverse_shift_row(columns)
    print("Inverse shift row: ")
    print_columns(columns)
    shifted = read_columns(columns)
    print(shifted)
    
    columns = plaintext_into_columns(shifted)
    
    # Perform first round of column transposition
    columns = transposition(columns, round_2)
    print("\nFirst round: ")
    print_columns(columns)
    result = read_columns(columns)
    print(result)
    
    columns = plaintext_into_columns(result)
    
    # Perform first round of column transposition
    columns = transposition(columns, round_2)
    print("\nSecond round: ")
    print_columns(columns)
    final = read_rows(columns)
    
    return final