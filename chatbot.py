import random
from datetime import datetime

# ============================
# Basic Rule-Based Chatbot
# ============================

print("=" * 45)
print("🤖 Welcome to My Python Chatbot 🤖")
print("=" * 45)

# Ask user's name
name = input("What's your name? ")

# Time-based greeting
hour = datetime.now().hour

if hour < 12:
    greeting = "Good Morning"
elif hour < 18:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

print(f"\n{greeting}, {name}! 😊")
print("I'm your simple rule-based chatbot.")
print("Type 'help' to see the available commands.\n")


# Help Menu Function
def help_menu():
    print("\n========== HELP MENU ==========")
    print("hello          - Say hello")
    print("how are you    - Ask how I am")
    print("time           - Show current time")
    print("date           - Show today's date")
    print("joke           - Hear a joke")
    print("quote          - Get a motivational quote")
    print("thank you      - Thank the bot")
    print("who made you   - Know my creator")
    print("help           - Show this menu")
    print("bye            - Exit the chatbot")
    print("===============================\n")


# Main Chat Loop
while True:

    user = input("You: ").lower().strip()

    # Hello
    if user == "hello" or user == "hi":
        replies = [
            "Hi! 👋",
            "Hello! 😊",
            "Hey there! 😄",
            f"Hello, {name}! 👋"
        ]
        print("Bot:", random.choice(replies))

    # How are you
    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking. 😊")

    # Time
    elif user == "time":
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print("Bot: Current Time:", current_time)

    # Date
    elif user == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's Date:", current_date)

    # Joke
    elif user == "joke":
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
            "Why did the Python programmer wear glasses? Because they couldn't C! 🤓",
            "Why was the computer cold? It forgot to close Windows! 😂"
        ]
        print("Bot:", random.choice(jokes))

    # Quote
    elif user == "quote":
        quotes = [
            "Believe in yourself. 🌟",
            "Success starts with small steps. 💪",
            "Never stop learning. 📚",
            "Dream big and work hard. 🚀"
        ]
        print("Bot:", random.choice(quotes))

    # Thank You
    elif user == "thank you" or user == "thanks":
        print("Bot: You're welcome! 😊 Happy to help.")

    # Creator
    elif user == "who made you":
        print("Bot: I was created by a Python programmer as a college project. 🤖")

    # Help
    elif user == "help":
        help_menu()

    # Bye
    elif user == "bye":
        print(f"Bot: Goodbye, {name}! 👋")
        print("Have a wonderful day! 🌸")
        break

    # Unknown command
    else:
        print("Bot: Sorry, I don't understand that. 😅")
        print("Type 'help' to see the available commands.")