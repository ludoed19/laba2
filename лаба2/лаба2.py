# Шестнадцатеричные четные числа, не превышающие 2047(10) и содержащие более 7 цифр. Вывести числа и их количество. Максимальное число вывести прописью 
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
