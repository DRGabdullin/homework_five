# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str,
# ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа
# и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии


def premium(names: list[str], cash: list[int], percent: list[str]) -> dict[str:float]:
    return {name: money / 100 * perc
            for name, money, perc in zip(names, cash, (float(i[:-1]) for i in percent))}

