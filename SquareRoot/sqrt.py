from decimal import Decimal
import cmath
from mpmath import mp


def square_root(x, precision=None):
    """
    Функция для вычисления арифметического квадратного корня числа с заданной точностью
    Функция поддерживает длинные числа, аналитические, корни из нуля.
    
    Параметры:
    x (float): Число, из которого требуется извлечь квадратный корень
    precision (int): Количество знаков после запятой. По умолчанию None
    
    Возвращает:
    float: Квадратный корень из числа x с заданной точностью
    """
    try:
        if precision:
            if str(precision).count('.'):
                a = 1/0
            number = Decimal(float(x))
            root = number.sqrt()
            return round(Decimal(root), int(precision))
        else:
            return Decimal(float(x)).sqrt()
    except:
        return "Некорректный ввод данных."


def complex_square_root(real_part, imaginary_part, precision=None):
    """
    Функция для вычисления квадратного корня комплексного числа с заданной точностью
    Функция поддерживает длинные числа, аналитические, корни из нуля.
    
    Параметры:
    real_part (float): Действительная часть числа, из которого требуется извлечь квадратный корень
    imaginary_part  (float): Мнимая часть числа, из которого требуется извлечь квадратный корень
    precision (int): Количество знаков после запятой. По умолчанию None
    
    Возвращает:
    float: Квадратный корень из комплексного числа с действительной частью real_part и мнимой частью imaginary_part
    """
    try:
        if precision:
            if str(precision).count('.'):
                a = 1/0
            mp.dps = int(precision) + 2
            x = complex(float(real_part), float(imaginary_part))
            root = cmath.sqrt(x)
            return complex(round(root.real, int(precision)), round(root.imag, int(precision)))
        else:
            x = complex(float(real_part), float(imaginary_part))
            return cmath.sqrt(x)
    except:
        return "Некорректный ввод данных."
    

'''
# Тесты
    
# Кейс 1. Арифметическое число, из которого извлекается квадрат.
print(square_root(4))

# Кейс 2. Извлечения корня из нуля.
print(square_root(0))

# Кейс 3. Арифметическое число, из которого квадрат извлекается не как целое число.
print(square_root(3))

# Кейс 4. Извлечения квадрата с заданной точностью.
print(square_root(3, 1))

# Кейс 5. Извлечения корня из длинного числа
print(square_root(1099511627776))

# Кейс 6. Извлечения корня из комплексного числа.
print(complex_square_root(4, 4))

# Кейс 7. Извлечения корня из комплесного числа с заданной точностью.
print(complex_square_root(3, 3, 3))

# Кейс 8. Действительная часть - длинная, комплексная - арифметическое
print(complex_square_root(1099511627776, 2))

# Кейс 9. Действительная часть - арифметическая, комплексная - длинная
print(complex_square_root(2, 1099511627776))

# Кейс 10. Все части - длинные
print(complex_square_root(30495002083984, 4284415280148025))

# Кейс 11. Все части - длинные, c заданной точностью.
print(complex_square_root(30495002083984, 4284415280148025, 4))

# Кейс 12. Все части - нули.
print(complex_square_root(0, 0))

# Кейс 13. Отправка букв.
print(square_root("eqrwrwer"))
print(complex_square_root("sdadasd", "asdadqw"))

# Кейс 14. Числа с плавающей точкой.
print(square_root(4.0))

# Кейс 15. Числа с плавающей точкой с заданной точностью.
print(square_root(3.56, 3))

# Кейс 16. Комплексные числа с плавающей точкой.
print(complex_square_root(45.2342, 2.2))

# Кейс 17. Одно число - с плавающей точкой, другое нет.
print(complex_square_root(32.2411, 2))
print(complex_square_root(213, 12.312))

# Кейс 18. Комплексные числа с плавающей точкой с заданной точностью
print(complex_square_root(323.23, 23.45, 2))


'''