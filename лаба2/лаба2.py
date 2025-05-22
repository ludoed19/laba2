# Шестнадцатеричные четные числа, не превышающие 2047(10) и содержащие более 7 цифр. Вывести числа и их количество. Максимальное число вывести прописью 
import re
digit_names = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 
               'шесть', 'семь', 'восемь', 'девять', 'десять',
               'одиннадцать', 'двенадцать', 'тринадцать', 
               'четырнадцать', 'пятнадцать']
with open('input.txt') as f:
    content = f.read().lower()
    pattern = r'\b(0{8,}|0*[1-7][0-9a-f]{7,})\b'
    nums = [m.group() for m in re.finditer(pattern, content) 
            if int(m.group(), 16) % 2 == 0 and int(m.group(), 16) <= 2047]
if nums:
    print("Найденные числа:", *nums)
    print("Количество:", len(nums))
    max_num = max(nums, key=lambda x: int(x, 16))
    print("Максимальное число прописью:", 
          ' '.join(digit_names[int(d, 16)] for d in max_num))
else:
    print("Нет подходящих чисел")
