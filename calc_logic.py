"""
Модуль calc_logic.py
Содержит математические функции для калькулятора.
"""
import math

def add(a: float, b: float) -> float:
    """Складывает два числа."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Вычитает второе число из первого."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Умножает два числа."""
    return a * b

def divide(a: float, b: float) -> float:
    """
    Делит первое число на второе.
    Вызывает ValueError, если делитель равен 0.
    """
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a / b

def square_root(a: float) -> float:
    """Вычисляет квадратный корень неотрицательного числа.

    Args:
        a (float): Число, из которого извлекается корень.

    Returns:
        float: Квадратный корень числа a.

    Raises:
        ValueError: Если a меньше нуля.

    Examples:
        >>> square_root(9)
        3.0
    """
    if a < 0:
        raise ValueError(
            "Нельзя вычислить квадратный корень отрицательного числа."
        )

    return math.sqrt(a)

