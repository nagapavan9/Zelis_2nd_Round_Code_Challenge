# Python version: 3.11.4

def parse_number(words):
    number_words = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
        "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
        "hundred": 100, "thousand": 1000, "million": 1000000
    }

    negative = False
    if words[0] == "negative":
        negative = True
        words = words[1:]

    result = 0
    current_number = 0
    for word in words:
        if word in number_words:
            scale = number_words[word]
            if scale < 100:
                current_number += scale
            elif scale == 100:
                current_number *= scale
            else:  # for thousand and million
                current_number *= scale
                result += current_number
                current_number = 0
        else:
            raise ValueError(f"Unknown number word: {word}")

    result += current_number

    if negative:
        result = -result

    return result


def main():
    input_text = input("Enter numbers in words (separated by ', '): ").strip()
    number_strings = input_text.split(", ")

    results = []
    for number_string in number_strings:
        words = number_string.split()
        number = parse_number(words)
        results.append(str(number))

    print(", ".join(results))

if __name__ == "__main__":
    main()
