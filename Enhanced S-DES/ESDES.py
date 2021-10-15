from SDES.encrypter import encryption
from SDES.key_generator import key_generation
from SDES.decrypter import decryption

# First process the Simple Columnar Transposition Technique with Multiple Rounds (SCTTMR)
# Then the output comes from SCTTMR will gain indergone Shift Rows Stage (sic)
# The plaintext message is first converted into the cipher text by using SCTTMR with min. 1 or 2 rounds
# The output from Shift row is then converted into a bit form because the S-DES applies its process on bit level as usual

def print_columns(columns):
    print()
    for index in range(3):
        print(columns[0][index], columns[1][index], columns[2][index])
        
def read_columns(columns):
    round_1_result = ""
    for num1 in range(3):
        for num2 in range(3):
            round_1_result += round_1_result.join((columns[num1][num2]))
    return round_1_result

def plaintext_into_columns(plaintext):
    # Creation of empty columns
    column_1 = []
    column_2 = []
    column_3 = []
    
    #Remove spaces from the plaintext input
    plaintext_spaceless = plaintext.replace(" ","")
    
    # Add the plaintext to the columns 
    # string[start:stop:step] start position. end position. the increment
    column_1 = [[letter] for letter in plaintext_spaceless[::3]]
    column_2 = [[letter] for letter in plaintext_spaceless[1::3]]
    column_3 = [[letter] for letter in plaintext_spaceless[2::3]]
    #print(column_1, column_2, column_3)
    
    # Add the columns into a list for ease of access when doing rounds
    columns = [column_1, column_2, column_3]
    print_columns(columns)
    return columns

def transposition(columns, round):
    # Perform the first column transposition round
    columns[0], columns[1], columns[2] = columns[round[0]-1], columns[round[1]-1], columns[round[2]-1]
    return columns

def simple_columnar_transposition(plaintext):
    # Random selection of columns for the rounds
    round_1 = [2, 3, 1]
    round_2 = [2, 3, 1]
    
    # Write the plaintext into the columns
    columns = plaintext_into_columns(plaintext)
    
    # Perform the first column transposition round
    columns = transposition(columns, round_1)
    
    # Read in columns
    round_1_result = read_columns(columns)
    print(f"Result of round 1 of SCTTMR: {round_1_result}")
    
    # Write the plaintext into the columns
    columns = plaintext_into_columns(round_1_result)
    
    # Perform the second column transposition round
    columns = transposition(columns, round_2)
    
    # Read in columns
    round_2_result = read_columns(columns)
    print(f"Result of round 2 of SCTTMR: {round_2_result}")
    
    columns = shift_row(columns)
    print_columns(columns)
    
    last_round_result = read_columns(columns)
    print(f"Result of round 2 of SCTTMR: {last_round_result}")
    
    return last_round_result

# Simple permutation
def shift_row(rows):
    # First row is not altered.
    # Second row is circular left shifted 1 byte
    rows[1][0], rows[1][1], rows[1][2] = rows[1][1], rows[1][2], rows[1][0]
    # Third row is circular left shifter 2 bytes
    rows[2][0], rows[2][1], rows[2][2] = rows[2][2], rows[2][0], rows[2][1]
    
    return rows

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


def main():
    print("************")
    input_plaintext = "DID YOU SEE"
    print(f"Plaintext: {input_plaintext}")
    SCT_result = simple_columnar_transposition(input_plaintext)
    print(f"SCTTMR result: {SCT_result}")
    
    # Encrypt using S-DES
    
    key = "0010010111"
    print(f"Key: {key}")
    key = key_generation(key)
    # Turn the each letter of the input into binary
    binary_input = "".join(format(ord(i), "08b") for i in SCT_result)
    binary_input_list = [binary_input[i:i+8] for i in range(0, len(binary_input), 8)]
    # Encrypt each letter
    print("************")
    print("Start Enhanced S-DES encryption process")
    cyphertext = ""
    for binary_letter in binary_input_list:
        cyphertext += encryption(binary_letter, key)
        print("Joining result with the rest of the cyphertext...")
    print("************")
    print("End of Enhanced S-DES encryption process")
    # Show the result as hex
    decimal_cypher = int(cyphertext, 2)
    hex_cypher = hex(decimal_cypher)
    print(f"Hex output of DES encryption: {hex_cypher}")
    
    # Decrypt using DES
    print("************")
    print("Start Enhanced S-DES decryption process")
    cyphertext_binary_list = [cyphertext[i:i+8] for i in range(0, len(cyphertext), 8)]
    binary_decryption = ""
    for cyphertext_fragment in cyphertext_binary_list:
        binary_decryption += decryption(cyphertext_fragment, key) + " "
        print("Joining result with the rest of the 'plaintext'...")
    print("************") 
    print("End of Enhanced S-DES decryption process")
    # Convert binary string to ascii string
    print(binary_decryption)
    plaintext_for_SCT = ""
    for binary_value in binary_decryption.split():
        an_int = int(binary_value, 2)
        ascii_char = chr(an_int)
        plaintext_for_SCT += ascii_char
    
    print(f"Plaintext for SCT: {plaintext_for_SCT}")
    
    # Start decryption of SCT
    
    columns = plaintext_into_columns(plaintext_for_SCT)
    print("I wonder", read_columns(columns))
    columns = inverse_shift_row(columns)
    print_columns(columns)
    input = read_columns(columns)
    print("end me:",input)
    simple_columnar_transposition(input)
    

if __name__ == "__main__":
    main()
