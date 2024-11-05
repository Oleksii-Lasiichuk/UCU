# original code
def analyze_student_scores(input_file, output_file):
    file = open(input_file, "w")
    results = []

    for line in file:
        name, scores = line.split(":")
        scores = scores.split(",")

        total = 0
        highest = 0
        failed = False
        for score in scores:
            total += score
            if score > highest:
                highest = score
            if score < 75:
                failed = True

        average = total / len(scores)

        results[name] = {"average": average, "highest": highest, "failed": failed}

    input_file.close()

    output_file = open(output_file, "w")

    output_file.write(results)

    output_file.close()

    return results


# our code

# 1. Read mode
# 2. "with open" instead of just open
# 3. results is dict
# 4. then new_results is list (from results)


def analyze_student_scores1(input_file: str, output_file: str) -> list:
    """
    Analize student scores gotten from text file.
    """

    new_results = []
    with open(input_file, "r", encoding="utf-8") as file:
        results = {}  # dictionary instead of list

        for line in file:
            name, scores = line.strip().split(":")
            scores = [
                int(score) for score in scores.split(",")
            ]  # int + str -> int(score)

            total = 0
            highest = 0
            failed = False
            for score in scores:
                total += score
                if score > highest:
                    highest = score
                if score < 75:
                    failed = True

            average = total / len(scores)

            results[name] = {"average": average, "highest": highest, "failed": failed}

    for name, value1 in results.items():  # dict to list
        options = []
        for _, value2 in value1.items():
            options.append(value2)
        new_results.append([name, options])

    with open(output_file, "w", encoding="utf-8") as s_file:  # formatting output
        for student in new_results:
            _ = s_file.write(
                f"{student[0]}: Average: {student[1][0]:.2f}\
, Highest: {student[1][1]}, Failed: {student[1][2]}\n"
            )


# Chat GPT
"""
Неправильний режим відкриття файлу для читання: Файл input_file відкривався в режимі запису "w", хоча його потрібно було відкрити в режимі читання "r". Це призводило до того, що файл очищався перед тим, як прочитати дані, що робило їх недоступними.

Невідповідний тип структури даних: results було ініціалізовано як список (results = []), але потім використовувалося як словник, що призводило до помилки типу при спробі додати дані за ключем (results[name] = {...}).

Тип даних оцінок: Значення оцінок було потрібно перетворити з рядкового типу в ціле число, інакше арифметичні операції (total += score, if score > highest) були б неможливими.

Закриття файлу: Було намагання закрити input_file, хоча цей файл ніколи не відкривався напряму. Насправді потрібно було закрити file.

Неправильний спосіб запису словника у файл: Функція write не може записати словник напряму. Запис output_file.write(results) виведе помилку, оскільки write очікує рядок, а не словник.
"""


def analyze_student_scores2(input_file, output_file):
    # Відкриваємо файл для читання
    file = open(input_file, "r")
    results = {}

    # Обробляємо кожен рядок у файлі
    for line in file:
        name, scores = line.strip().split(":")
        scores = [int(score) for score in scores.split(",")]

        total = sum(scores)
        highest = max(scores)
        failed = any(score < 75 for score in scores)

        average = total / len(scores)
        results[name] = {"average": average, "highest": highest, "failed": failed}

    # Закриваємо файл після читання
    file.close()

    # Записуємо результати у вихідний файл у звичайному текстовому форматі
    with open(output_file, "w") as output_file:
        for name, data in results.items():
            output_file.write(f"Student: {name}\n")
            output_file.write(f"  Average Score: {data['average']:.2f}\n")
            output_file.write(f"  Highest Score: {data['highest']}\n")
            output_file.write(f"  Failed: {'Yes' if data['failed'] else 'No'}\n")
            output_file.write("\n")

    return results


print(analyze_student_scores2("student_scores.txt", "new_file.txt"))
