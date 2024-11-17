# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as file:          # TODO считать содержимое csv файла
        lines = [line for line in csv.DictReader(file)]



    with open(OUTPUT_FILENAME,'w') as file2:
        json_file = json.dump(lines, file2,indent=4, ensure_ascii=False)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
