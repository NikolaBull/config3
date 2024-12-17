def parse_expression(expr):
    """
    Парсит и вычисляет префиксное выражение.
    """
    tokens = expr.split()[::-1]  # Разделяем строку и разворачиваем список
    stack = []

    while tokens:
        token = tokens.pop()

        if token == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif token == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        elif token == "abs":
            a = stack.pop()
            stack.append(abs(a))
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError(f"Невозможно преобразовать '{token}' в число.")

    if len(stack) != 1:
        raise ValueError(f"Некорректное выражение: '{expr}'")
    return stack[0]
