import re
def ntw(digits):
    words = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь"]
    return " ".join(words[int(d)] for d in sorted(digits)
K = 10
try:
    with open("input.txt", "r", encoding="utf-8") as f:
        data = f.read().strip()  
except FileNotFoundError:
    print("Ошибка: Файл 'input.txt' не найден.")
    input("Нажмите Enter для выхода...")
    exit()
allowed = []
for i in range(2048):
    o = oct(i)[2:]  
    if i % 2 == 1 and len(set(o)) >= K:
        allowed.append(o)
if not allowed:
    print("Нет подходящих чисел.")
    input()
    exit()
pattern = r'\b(?:' + '|'.join(map(re.escape, allowed)) + r')\b'
matches = re.findall(pattern, data)
print("Найденные восьмеричные числа:", matches)  
if matches:
    nums = [(int(m, 8), set(m)) for m in matches]
    print("Числа:", [n[0] for n in nums])
    print("Количество:", len(nums))
    print("Используемые цифры:", ntw(set.union(*[n[1] for n in nums])))
else:
    print("Нет подходящих чисел.")
input()
