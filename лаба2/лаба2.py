# Шестнадцатеричные четные числа, не превышающие 2047(10) и содержащие более 7 цифр. Вывести числа и их количество. Максимальное число вывести прописью 
import re
def ntw(d):
    return ' '.join(["ноль","один","два","три","четыре","пять","шесть","семь"][int(x)] for x in sorted(d))
K = 3
try:
    data = open("input.txt", encoding="utf-8").read()
except:
    input("Ошибка открытия файла\nEnter для выхода...")
    exit()
pattern = r'\b(?:' + '|'.join(
    oct(i)[2:] for i in range(1, 2048, 2) 
    if len(set(oct(i)[2:])) >= K
) + r')\b'
matches = re.findall(pattern, data)
if matches:
    digits = set().union(*matches)
    print(f"Найдено: {len(matches)}\nЧисла: {[int(m,8) for m in matches]}\nЦифры: {ntw(digits)}")
else:
    print("Совпадений не найдено")
input()
def ntw(n): return ' '.join({'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}[c] for c in str(n))
try: data = open("input.txt", encoding="utf-8").read()
except: input("Ошибка открытия файла\nEnter для выхода..."); exit()
nums = []
for tok in data.split():
    if len(tok) > 7 and all(c in '0123456789abcdefABCDEF' for c in tok):
        try:
            dec = int(tok, 16)
            if dec <= 2047 and dec % 2 == 0: nums.append(dec)
        except: pass
if nums:
    print(f"Найдено: {len(nums)}\nЧисла: {nums}\nМаксимум прописью: {ntw(max(nums))}")
else: print("Совпадений не найдено")
input()
