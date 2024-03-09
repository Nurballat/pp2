# ex 1
'''import re
txt = input()
def test1(txt):
    m = re.search("ab*",txt)
    print(m)

test1(txt)

# ex 2
import re
txt = input()
print(re.search("ab{2,3}",txt))

# ex 3
import re
txt = input()
print(re.search(r"[a-z]_[a-z]+", txt))

# ex 4
import re
txt = input()
print(re.search(r"[A-Z][a-z]+", txt))

# ex 5
import re
txt = input()
print(re.search(r"a.*b", txt))

#ex 6
import re
txt = input()
pattern = r'[ ,.]'
retext = re.sub(pattern,':',txt)
print(retext)

#ex 7
import re

def convert_to_camel(snake):
    camel = re.sub(r'_([a-z])', lambda match: match.group(1).upper(),snake)
    return camel

snake = "This_function_converts_snake_to_camel"
camel = convert_to_camel(snake)
print(camel)

# ex8
import re
txt = input()
print(re.findall(r"[A-Z][a-z]*", txt))

# ex 9
import re
string = "HelloMyNameIsAlikhan"
result = re.findall("[A-Z][a-z]*", string)
print(' '.join(result))
'''
# ex 10
import re
def convert_to_snake(camel):
    snake = re.sub(r'(?<!^)([A-Z])', r'_\1', camel).lower()
    return snake
camel = "ThisFunctionConvertsToSnake"
snake = convert_to_snake(camel)
print(snake)



