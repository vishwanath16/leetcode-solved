# Example: Converting binary to integer
# -------------------------------------
# To convert a binary string to an integer, use int(binary_string, 2)
binary_string = "1010"
decimal_value = int(binary_string, 2)  # Converts "1010" (binary) to 10 (decimal)
print(f"Binary: {binary_string} -> Decimal: {decimal_value}")  # Output: 10

# Example: Formatting a number as a 32-bit binary and reversing it
# ---------------------------------------------------------------
# Use f-string with :032b to format the number as a 32-bit binary with leading zeros
n = 0b00000010100101000001111010011100  # Example 32-bit binary number
formatted_binary = f'{n:032b}'  # Converts the number to a 32-bit binary string
print(f"32-bit Binary: {formatted_binary}")  # Output: 00000010100101000001111010011100

# Reversing the 32-bit binary string
reversed_binary = formatted_binary[::-1]  # Reverses the binary string
print(f"Reversed Binary: {reversed_binary}")  # Output: 00111001011110000010100101000000

# If you want the reversed binary as an integer, convert it back to decimal
reversed_decimal = int(reversed_binary, 2)
print(f"Reversed Binary (as Decimal): {reversed_decimal}")
