# Exercise 2: String Utilities


def reverse_string(s: str) -> str :
    return s[::-1]

def count_vowels(s: str) -> int:
    vowels='aeiouAEIOU'
    return len([s for s in s if s in vowels])



def is_palindrome(s: str) -> bool:
        s = s.lower().replace(" ", "")  # Normaliser en minuscules et sans espaces
        return s == s[::-1]



def capitalize_words(s: str) -> str:
        return " ".join(word.capitalize() if word else "" for word in s.split(" "))


