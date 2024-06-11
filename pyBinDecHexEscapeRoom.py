import random

def decimal_to_binary(decimal_number):
    return bin(decimal_number)[2:]

def decimal_to_hexadecimal(decimal_number):
    return hex(decimal_number)[2:].upper()

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def hexadecimal_to_decimal(hex_str):
    return int(hex_str, 16)

def escape_room():
    print("Welcome to the Binary, Decimal, and Hexadecimal Escape Room!")
    print("Solve the puzzles to escape. Good luck!")
    
    # Puzzle 1: Decimal to Binary
    decimal_number = random.randint(10, 100)
    correct_answer = decimal_to_binary(decimal_number)
    print(f"🧩 Puzzle 1: Convert the decimal number {decimal_number} to binary.")
    answer = input("Your answer: ")
    if answer == correct_answer:
        print("✅ Correct! You solved the first puzzle. 🎉")
    else:
        print(f"❌ Wrong! The correct answer was {correct_answer}. Try again.")
        return

    # Puzzle 2: Binary to Decimal
    binary_number = format(random.randint(10, 100), 'b')
    correct_answer = binary_to_decimal(binary_number)
    print(f"🧩 Puzzle 2: Convert the binary number {binary_number} to decimal.")
    answer = int(input("Your answer: "))
    if answer == correct_answer:
        print("✅ Correct! You solved the second puzzle. 🎉")
    else:
        print(f"❌ Wrong! The correct answer was {correct_answer}. Try again.")
        return

    # Puzzle 3: Decimal to Hexadecimal
    decimal_number = random.randint(10, 100)
    correct_answer = decimal_to_hexadecimal(decimal_number)
    print(f"🧩 Puzzle 3: Convert the decimal number {decimal_number} to hexadecimal.")
    answer = input("Your answer: ")
    if answer == correct_answer:
        print("✅ Correct! You solved the third puzzle. 🎉")
    else:
        print(f"❌ Wrong! The correct answer was {correct_answer}. Try again.")
        return

    # Puzzle 4: Hexadecimal to Decimal
    hex_number = format(random.randint(10, 100), 'X')
    correct_answer = hexadecimal_to_decimal(hex_number)
    print(f"🧩 Puzzle 4: Convert the hexadecimal number {hex_number} to decimal.")
    answer = int(input("Your answer: "))
    if answer == correct_answer:
        print("✅ Correct! You solved the fourth puzzle. 🎉")
    else:
        print(f"❌ Wrong! The correct answer was {correct_answer}. Try again.")
        return

    print("🎉 Congratulations! You have successfully escaped the room! 🎉")

if __name__ == "__main__":
    escape_room()
