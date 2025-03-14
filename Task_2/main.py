import re
from typing import Callable

#приймає рядок як аргумент і повертає генератор, що ітерує по всіх дійсних числах у тексті
def generator_numbers(word: str):
    pattern_number = r"[\d]+\.{0,1}[\d]+"
    match = re.search(pattern_number, word)
    if match:
        print(3, match.group())
        yield match.group()
    else:
        yield 0

#використовувує генератор для обчислення загальної суми чисел у вхідному рядку та приймає його як аргумент при виклику 
def sum_profit(text: str, func: Callable):
    #розбиває текст на окремі слова
    text = text.split()
    sum = 0
    #ітерує функцію по словам та підраховує по результатам загальну суму
    for word in text:
        gen_num = func(word)
        sum += float(next(gen_num))
    return sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
