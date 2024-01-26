# Description: What is the Card?
def main():
    try:
        testcases = int(input())
    except ValueError:
        return

    answers = []
    for i in range(testcases):
        Y = 0
        deck = []
        cardsInHand = []
        try:
            cardOrder = input().split()
        except EOFError:
            break
        if cardOrder == "" or len(cardOrder) != 52:
            break
        for card in cardOrder:
            if len(card) != 2:
                break
            deck.append(card)
        # Remove the top 25 cards
        for z in range(25):
            cardsInHand.append(deck.pop(51 - z))
        # Reverse to get in the right order as it was taken from top stright away all 25 cards
        cardsInHand.reverse()
        # The tree test cases
        for u in range(3):
            # if card deck is empty, break
            if len(deck) == 0:
                break
            card = deck.pop()
            try:
                X = int(card[0])
            except ValueError:
                X = 10
            if X > 10:
                X = 10
            Y += X
            for v in range(10 - X):
                #
                if len(deck) == 0:
                    break
                deck.pop()
        # Check if Y is out of bounds

        deck += cardsInHand
        if Y - 1 < 0 or (Y - 1) > len(deck):
            break
        answers.append("Case {}: {}".format(i + 1, deck[Y - 1]))
    for answer in answers:
        print(answer)


while True:
    try:
        main()
    except EOFError:
        break
