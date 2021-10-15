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

def decrypt_simple_columnar_transformation(cyphertext):
    # Random selection of columns for the rounds
    round_1 = [2, 3, 1]
    round_2 = [2, 3, 1]
    
    # Write the plaintext into the columns
    columns = plaintext_into_columns(cyphertext)
    print_columns(columns)
    
    # Perform inverse row shift
    columns = inverse_shift_row(columns)
    print("Inverse shift row: ")
    print_columns(columns)
    shifted = read_columns(columns)
    print(shifted)
    
    columns = plaintext_into_columns(shifted)
    print_columns(columns)
    columns = transposition(columns, round_1)
    print_columns(columns)
    round_1_result = read_columns(columns)
    columns = plaintext_into_columns(round_1_result)
    print_columns(columns)
    print(read_columns(columns))