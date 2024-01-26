# import sys


def main():
    testcases = int(input())
    input()
    #    sys.stdout = open("output.txt", "w")
    for testcase in range(testcases):
        wordlist = []
        while True:
            word = input()
            if word == "":
                break
            wordlist.append(word)
        wordlist.sort()
        if wordlist == []:
            break
        for i in range(len(wordlist)):
            for j in range(i + 1, len(wordlist)):
                if sorted(wordlist[i].replace(" ", "").lower()) == sorted(
                    wordlist[j].replace(" ", "").lower()
                ):
                    print(wordlist[i] + " = " + wordlist[j])
        print()


# sys.stdout.close()


while True:
    try:
        main()
    except EOFError:
        break
