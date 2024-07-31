# Python version: 3.11.4

def find_six_letter_words(dictionary, pieces):
    # Create a set of pieces for fast lookup
    piece_set = set(pieces)

    results = []

    for word in dictionary:
        if len(word) == 6:
            # Try to split the word into two pieces
            for i in range(1, 6):
                part1 = word[:i]
                part2 = word[i:]
                attempt = f"{part1} + {part2}"
                if part1 in piece_set and part2 in piece_set:
                    results.append(word)
                    print(f"{attempt} = {word} (valid)")
                    break  # We found a valid split, no need to check further
                else:
                    print(f"{attempt} != {word} (invalid)")

    return results


def main():
    dictionary = ["albums", "barely", "befoul", "convex", "hereby", "jigsaw", "tailor", "weaver"]
    pieces = ["al", "bums", "bar", "ely", "be", "foul", "con", "vex", "here", "by", "jig", "saw", "tail", "or", "we",
              "aver"]

    six_letter_words = find_six_letter_words(dictionary, pieces)
    print("\nSix-letter words from the dictionary using the pieces:")
    for word in six_letter_words:
        print(word)


if __name__ == "__main__":
    main()
