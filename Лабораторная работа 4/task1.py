import json

INPUT_FILE ="input.json"


# TODO решите задачу
def task() -> float:
    answer = []
    with open(INPUT_FILE) as file:
        file_json = json.load(file)

    answer += [item["score"] * item["weight"] for item in file_json]
    return (f"{sum(answer):.3f}")


print(task())
