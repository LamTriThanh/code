import googletrans
from googletrans import Translator

translator = Translator()
result = translator.translate(input(), src='vi', dest='en')

print(result.src)
print(result.dest)
print(result.text)