"""Module with functions."""


def largest_sum(numbers: list[int]) -> tuple[int, int]:
    """Encontra e retorna os dois números que somados dão o maior valor."""
    numbers.sort()
    if len(numbers) <= 1:
        print(None)
    else: 
        print(numbers)    
        primeiro = numbers[-2]  # o primeiro número da soma
        segundo = numbers[-1]  # o segundo número da soma
        return primeiro, segundo
