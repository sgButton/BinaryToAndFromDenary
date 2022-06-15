# Function converts binary numbers to denary
def bin_to_den(bin_num):
    denary = 0
    place_value = 128
    for i in bin_num:
        try:
            int_i = int(i)
        except ValueError:
            return "wrong value"
        denary_single = place_value * int_i
        denary += denary_single
        place_value //= 2
    return denary

# Function converts denary numbers to binary
def den_to_bin(den_num):
    try:
        den_int = int(den_num)
    except ValueError:
        return "wrong value"
    binary = ""
    place_value = 128
    for i in range(0, 8):
        if den_int >= place_value:
            binary += "1"
            den_int -= place_value
        else:
            binary += "0"
        place_value //= 2
    return binary

# Function for user decision
def decision():
    u_decision = input("Binary to Denary(BD) or Denary to Binary(DB)? ").upper()
    return u_decision


user_decision = decision()

if user_decision == "BD":
    acceptable_value = False

    while acceptable_value == False:
        binary_input = input("Please enter an 8 bit binary number: ")        
        d_conversion_function = bin_to_den(binary_input)

        if d_conversion_function == "wrong value":
            print("Please input a valid number!")
        else:
            print(f"{binary_input} is {d_conversion_function} in denary")
            acceptable_value = True

elif user_decision == "DB":
    acceptable_value = False
    
    while acceptable_value == False:
        denary_input = input("Please enter denary number under 256: ")
        b_conversion_function = den_to_bin(denary_input)

        if b_conversion_function == "wrong value":
            print("Please input a valid number!")
        else:
            print(f"{denary_input} is {b_conversion_function} in binary")
            acceptable_value = True

else:
    print("Please input either 'BD' or 'DB'!")