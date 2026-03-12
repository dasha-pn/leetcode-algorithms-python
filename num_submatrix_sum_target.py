"""exercise from LeetCode"""

from collections import defaultdict

def num_submatrix_sum_target(matrix, target):
    """..."""

    rows = len(matrix)
    cols = len(matrix[0])

    result = 0

    # Перебираємо всі можливі пари рядків: top..bottom
    for top in range(rows):
        # col_sums[c] буде сумою елементів у стовпці c від рядка top до bottom
        col_sums = [0] * cols

        for bottom in range(top, rows):
            # Оновлюємо вертикальні суми для поточного bottom
            for c in range(cols):
                col_sums[c] += matrix[bottom][c]

            # Тепер задача: скільки підмасивів у col_sums дають суму target?
            # Використаємо префіксні суми + hashmap
            prefix_count = defaultdict(int)
            prefix_count[0] = 1  # порожній префікс

            current_sum = 0
            for val in col_sums:
                current_sum += val

                # скільки префіксів було з сумою current_sum - target?
                need = current_sum - target
                if need in prefix_count:
                    result += prefix_count[need]

                # зафіксувати, що префікс із сумою current_sum тепер існує
                prefix_count[current_sum] += 1

    return result

print(num_submatrix_sum_target([[0,1,0],[1,1,1],[0,1,0]], 0)) #4

# Крок 3. Повний алгоритм
# Нехай rows = len(matrix), cols = len(matrix[0]).
# Для кожної пари рядків top і bottom (top ≤ bottom):
# створюємо масив col_sums довжини cols, спочатку всі нулі
# для кожного стовпця c, додаємо matrix[bottom][c] до col_sums[c]
# (тобто ми поступово накопичуємо суму між top і поточним bottom)
# тепер в col_sums зберігається "сплющений" рядок для підматриць з рядками top..bottom
# на col_sums рахуємо кількість підмасивів із сумою target
# за допомогою prefix sums + hashmap
# додаємо це до глобального лічильника
# Повертаємо глобальний лічильник.
# Чому це працює:
# Ми перебираємо всі можливі верхні/нижні межі прямокутника,
# Для кожної такої "смуги" рахуємо всі варіанти лівої/правої межі.
