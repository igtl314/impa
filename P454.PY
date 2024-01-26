def get_sorted_phrase(phrase):
    # Remove spaces and sort the characters in the phrase
    return "".join(sorted(phrase.replace(" ", "")))


def find_anagrams(phrases):
    anagrams = {}

    for phrase in phrases:
        sorted_phrase = get_sorted_phrase(phrase)

        if sorted_phrase in anagrams:
            anagrams[sorted_phrase].append(phrase)
        else:
            anagrams[sorted_phrase] = [phrase]

    return anagrams


def print_anagrams(anagrams):
    for key, value in anagrams.items():
        if len(value) > 1:
            # Sort the phrases lexicographically
            value.sort()
            for i in range(len(value)):
                for j in range(i + 1, len(value)):
                    print(value[i] + " = " + value[j])


def main():
    test_cases = int(input().strip())
    input()  # Skip the blank line after the number of test cases

    for _ in range(test_cases):
        phrases = []
        line = input().strip()

        while line:
            phrases.append(line)
            line = input().strip()

        anagrams = find_anagrams(phrases)
        print_anagrams(anagrams)

        if _ < test_cases - 1:
            print()  # Separate consecutive output cases with a single blank line


while True:
    try:
        main()
    except EOFError:
        break
