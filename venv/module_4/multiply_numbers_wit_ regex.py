import re

text = 'I am 20 years old and you 40'

def my_function(text, multiplier=250):
  i = int(text.group())
  return str(i * multiplier)

print(re.sub(r'\d+', my_function, text))
