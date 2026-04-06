#1
import re

pattern = r'ab*'
text = input("Enter string: ")

if re.fullmatch(pattern, text):
    print("Match found")
else:
    print("No match")
#2
import re

pattern = r'ab{2,3}'
text = input("Enter string: ")

if re.fullmatch(pattern, text):
    print("Match found")
else:
    print("No match")
#3
import re

pattern = r'[a-z]+_[a-z]+'
text = input("Enter string: ")

matches = re.findall(pattern, text)
print(matches)
#4
import re

pattern = r'[A-Z][a-z]+'
text = input("Enter string: ")

matches = re.findall(pattern, text)
print(matches)
#5
import re

pattern = r'a.*b'
text = input("Enter string: ")

if re.fullmatch(pattern, text):
    print("Match found")
else:
    print("No match")
#6
import re

text = input("Enter string: ")

result = re.sub(r'[ ,.]', ':', text)
print(result)
#7
def snake_to_camel(text):
    words = text.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

text = input("Enter snake_case string: ")
print(snake_to_camel(text))
#8
import re

text = input("Enter string: ")

result = re.findall(r'[A-Z][^A-Z]*', text)
print(result)
#9
import re

text = input("Enter string: ")

result = re.sub(r'(?<!^)([A-Z])', r' \1', text)
print(result)
#10
import re

text = input("Enter camelCase string: ")

result = re.sub(r'([A-Z])', r'_\1', text).lower()
print(result)