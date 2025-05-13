# Шестнадцатеричные четные числа, не превышающие 2047(10) и содержащие более 7 цифр. Вывести числа и их количество. Максимальное число вывести прописью
import re
def number_to_words(n):
    return ' '.join('zero one two three four five six seven eight nine'.split()[int(d)] for d in str(n))
with open("input.txt") as f:
    text = f.read() 
matches = re.findall(r'\b(?:[0-9a-fA-F]{8,})(?<=[02468aAcCeE])\b', text)
valid = [(h.upper(), int(h, 16)) for h in matches if int(h, 16) <= 2047]
for h, d in valid: print(f"{h} (десятичное: {d})")
print(f"\nВсего найдено: {len(valid)}")
if valid: print("Максимальное число (в пропись):", number_to_words(max(valid, key=lambda x: x[1])[1]))
