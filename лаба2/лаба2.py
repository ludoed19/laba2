# Шестнадцатеричные четные числа, не превышающие 2047(10) и содержащие более 7 цифр. Вывести числа и их количество. Максимальное число вывести прописью 

import re
def ntw(n): return ' '.join({'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}[d] for d in str(n))
try: data = open("input.txt", encoding="utf-8").read()
except: input("Ошибка открытия файла\nEnter для выхода..."); exit()
pattern = r'\b[0-9a-fA-F]{8,}\b'
matches = re.findall(pattern, data)
nums = [int(m, 16) for m in matches if int(m, 16) <= 2047 and int(m, 16) % 2 == 0]
if nums:
    print(f"Найдено: {len(nums)}\nЧисла: {nums}\nМаксимум прописью: {ntw(max(nums))}")
else: print("Совпадений не найдено")
input()
12345678 000000FE ABCDEF00 000007DE 00000800
deadbeef 000007FF 000007FA facefeed 00000002

import re
def ntw(n): return ' '.join({'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}[d] for d in str(n))
try: data = open("input.txt", encoding="utf-8").read()
except: input("Ошибка открытия файла\nEnter для выхода..."); exit()
hex_even = [f"{i:X}" for i in range(0, 2048, 2) if len(f"{i:X}") > 7]  # только >7 символов и чётные
pattern = r'\b(?:' + '|'.join(hex_even) + r')\b'
matches = re.findall(pattern, data, re.IGNORECASE)
nums = [int(m, 16) for m in matches]
if nums:
    print(f"Найдено: {len(nums)}\nЧисла: {nums}\nМаксимум прописью: {ntw(max(nums))}")
else: print("Совпадений не найдено")
input()
