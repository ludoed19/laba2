import re
def num_to_words(digits):
    words = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь"]
    return " ".join(words[int(d)] for d in sorted(digits))
K = 3 
try:
    with open("input.txt", "r", encoding="utf-8") as f:
        data = f.read().strip()  
except FileNotFoundError:
    print("Ошибка: Файл 'input.txt' не найден.")
    input("Нажмите Enter для выхода...")
    exit()
matches = re.findall(r"\b[0-7]+\b", data)  # Ищем только восьмеричные числа
print("Найденные восьмеричные числа:", matches)  # Отладочный вывод
nums = [(int(m, 8), set(m)) for m in matches if len(set(m)) >= K]  # Преобразуем числа
nums = [(n, d) for n, d in nums if n <= 2047 and n % 2 == 1]  # Фильтруем
if nums:
    print("Числа:", [n[0] for n in nums])
    print("Количество:", len(nums))
    print("Используемые цифры:", num_to_words(set.union(*[n[1] for n in nums])))
else:
    print("Нет подходящих чисел.")
input()
