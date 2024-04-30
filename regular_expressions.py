# REGEX -> regular expressions

# patterns -> interpretate de un compilator special de regexuri ( incorporat in fiecare limbaj ) -> gaseste pattern in text/obiect

import re

# Basic example

text = 'Sunt Andrei si studiez Python studiez.'

pattern = r'studiez'

gasit = re.findall(pattern, text)
print(gasit)


# Meta caractere
"""
. -> match any character (mai putin newline)
^ -> match the start of the string
$ -> match the end of the string
\\d -> match any digit # un singur backslash
\\w -> match any character # un singur backslash
\\s -> match any whitespace (spatii goale) # un singur backslash
"""

text2 = 'The cat sat sat on the large mat'
pattern2 = r"\b\w{3}\b"
gasit2 = re.findall(pattern2, text2)
print(gasit2)


# Groups and capturing

text3 = "John: 25, Jane: 30"
pattern3 = r"(\w+): (\d+)"
gasit3 = re.findall(pattern3, text3)
print(gasit3[1][0])



text4 = "Please contact me at user@example.com or admin@test.com for further information."
pattern4 = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
gasit4 = re.findall(pattern4, text4)
print(gasit4)