"""
Модуль calc_logic.py
Содержит математические функции для калькулятора.
"""

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
