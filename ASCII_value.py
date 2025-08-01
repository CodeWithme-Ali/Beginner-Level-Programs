# ASCII Value of a Character

char = input("Enter a character: ")
print(f"The ASCII value of '{char}' is {ord(char)}")




'''ASCII stands for American Standard Code for Information Interchange.

It is a character encoding system that assigns a unique numeric value (0–127) to characters like:

Alphabets (A–Z, a–z)

Digits (0–9)

Symbols (!, @, #, etc.)

Control characters (like Enter, Tab, etc.)

For example:

'A' → 65

'a' → 97

'0' → 48

In Python, we use:

ord('A') → gives 65 (character → number)

chr(65) → gives 'A' (number → character)'''