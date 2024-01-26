def main():
    try:
        n = int(input())
    except ValueError:
        return

    answers = []
    for i in range(n):
        guesses = input()
        streak = 0
        score = 0
        for guess in guesses:
            if guess == "O":
                streak += 1
            else:
                streak = 0
            score += streak
        #        print(score)
        answers.append(score)

    for answer in answers:
        print(answer)


while True:
    try:
        main()
    except EOFError:
        break
