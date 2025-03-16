import phrases
import time
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def main():
    clear_screen()
    animate_text("Uakea, your spark has been lost! It's up to you to find it.")
    time.sleep(1)

    while True:
        clear_screen()
        print("Choose an action:")
        print("1. Seek a compliment to reignite your spirit.")
        print("2. Listen to a funny joke to lift your mood.")
        print("3. Find funny encouragement to warm your heart.")
        print("4. Focus on your positive traits to find strength.")
        print("5. Exit the search.")

        choice = input("> ")

        if choice == "1":
            animate_text(phrases.get_random_phrase("compliments"))
            time.sleep(2)
        elif choice == "2":
            animate_text(phrases.get_random_phrase("dad_jokes"))
            time.sleep(2)
        elif choice == "3":
            animate_text(phrases.get_random_phrase("funny_encouragement"))
            time.sleep(2)
        elif choice == "4":
            animate_text(phrases.get_random_phrase("personal_traits"))
            time.sleep(2)
        elif choice == "5":
            animate_text("Your spark will return in time. Remember how loved you are.")
            break
        else:
            animate_text("Invalid choice.")
            time.sleep(1)

    animate_text("The end.")

if __name__ == "__main__":
    main()