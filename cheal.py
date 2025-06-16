import random

def random_quote():
    quotes = [
        "Code is like humor. When you have to explain it, it’s bad.",
        "Experience is the name everyone gives to their mistakes.",
        "In order to be irreplaceable, one must always be different.",
        "Java is to JavaScript what car is to Carpet.",
        "Knowledge is power."
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print("Random Programming Quote:")
    print(random_quote())