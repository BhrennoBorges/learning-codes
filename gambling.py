import random

def play():
    symbols = ['🍒', '🍇', '🍉', '7️⃣']
    
    # Get three random symbols
    results = random.choices(symbols, k=3)
    
    # Print results separated by |
    print(' | '.join(results))
    
    # Check if all symbols are '7️⃣'
    if results.count('7️⃣') == 3:
        print("Jackpot! 💰")
    else:
        print("Thanks for playing!")

# Main game loop
def main():
    while True:
        play()
        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (Y/N): ").strip().upper()
        if play_again != 'Y':
            print("Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    main()
