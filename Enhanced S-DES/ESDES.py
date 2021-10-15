from SDES.encrypter import encryption
from SDES.key_generator import key_generation

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
    
    # Perform the first column transposition round
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
    rows[1][0], rows[1][1], rows[1][2] = rows[1][2], rows[1][0], rows[1][1]
    # Third row is circular left shifter 1 byte
    rows[2][0], rows[2][1], rows[2][2] = rows[2][1], rows[2][2], rows[2][0]


def main():
    input_plaintext = "DID YOU SEE"
    SCT_result = simple_columnar_transposition(input_plaintext)
    # Encrypt using S-DES
    key = key_generation("0010010111")
    # Turn the each letter of the input into binary
    binary_input = "".join(format(ord(i), "08b") for i in SCT_result)
    binary_input_list = [binary_input[i:i+8] for i in range(0, len(binary_input), 8)]
    # Encrypt each letter
    cyphertext = ""
    for binary_letter in binary_input_list:
        cyphertext += encryption(binary_letter, key)
    # Show the result as hex
    decimal_cypher = int(cyphertext, 2)
    hex_cypher = hex(decimal_cypher)
    print(hex_cypher.capitalize())

if __name__ == "__main__":
    main()
