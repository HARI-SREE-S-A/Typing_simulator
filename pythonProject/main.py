import time
import keyboard

def simulate_typing_hindi(text):
    # Wait for 15 seconds before typing
    time.sleep(15)

    # Simulate typing each character with a small delay
    for char in text:
        keyboard.write(char)
        time.sleep(0.1)  # Adjust the delay as needed

if __name__ == "__main__":
    # Read input text from a file (input.txt) using utf-8 encoding
    try:
        with open("input.txt", "r", encoding="utf-8") as file:
            input_text = file.read()
    except FileNotFoundError:
        print("Error: input.txt not found.")
        exit()

    # Call the function to simulate typing in Hindi
    simulate_typing_hindi(input_text)
