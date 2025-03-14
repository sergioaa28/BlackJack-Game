import random
import time

def deal_card():
    """Return a random card from the deck."""
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def calculate_score(cards):
    """Calculate score and handle Blackjack and Ace adjustments."""
    score = sum(cards)
    
    if score == 21 and len(cards) == 2:
        return 0  # Blackjack
    
    if 11 in cards and score > 21:
        cards = [1 if card == 11 else card for card in cards]  # Convert Ace (11) to 1 if needed
        score = sum(cards)

    return score

def compare(user_score, computer_score):
    """Compare scores and determine the winner."""
    if user_score == computer_score:
        return "It's a draw! 🤝"
    elif computer_score == 0:
        return "💀 The dealer got Blackjack! You lose!"
    elif user_score == 0:
        return "🎉 You got Blackjack! You win!"
    elif user_score > 21:
        return "💥 You busted! You lose!"
    elif computer_score > 21:
        return "🔥 The dealer busted! You win!"
    elif user_score > computer_score:
        return "🎉 You win!"
    else:
        return "😭 You lose!"

def play_game():
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    
    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            answer = input("Would you like another card? (yes/no): ").lower()
            if answer == "yes":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    time.sleep(1)  # Small delay for suspense
    print("\n--- Final Results ---")
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

if __name__ == "__main__":
    while input("\nDo you want to play Blackjack? (yes/no): ").lower() == "yes":
        print("\n" * 20)  # Clear screen effect
        play_game()
