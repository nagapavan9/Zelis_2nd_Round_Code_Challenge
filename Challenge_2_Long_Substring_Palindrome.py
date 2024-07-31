# Python version: 3.11.4

def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""

    longest = ""

    # Helper function to expand around center
    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    for i in range(n):
        # Odd length palindromes
        palindrome_odd = expand_around_center(i, i)
        if len(palindrome_odd) > len(longest):
            longest = palindrome_odd

        # Even length palindromes
        palindrome_even = expand_around_center(i, i + 1)
        if len(palindrome_even) > len(longest):
            longest = palindrome_even

    return longest


def main():
    # Provided block of text
    input_text = ("Fourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceiv"
                  "edinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedi"
                  "nagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlo"
                  "ngendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionoft"
                  "hatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisalto"
                  "getherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotco"
                  "nsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveco"
                  "nsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongre"
                  "memberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobed"
                  "edicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedI"
                  "tisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonore"
                  "ddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevoti"
                  "onthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGod"
                  "shallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeoplesh"
                  "allnotperishfromtheearth")

    longest_palindrome = longest_palindromic_substring(input_text)
    print("The longest palindromic substring is:", longest_palindrome)


if __name__ == "__main__":
    main()
