# load contents from file, put each element into a list, seperate by line-breaks
with open("puzzle2.txt") as f:
    reports = [list(map(int, line.split())) for line in f]


def is_valid_report(report):
    def is_sorted_and_valid(report):
        ascending = all(
            report[i] <= report[i + 1] and 1 <= report[i + 1] - report[i] <= 3
            for i in range(len(report) - 1)
        )
        descending = all(
            report[i] >= report[i + 1] and 1 <= report[i] - report[i + 1] <= 3
            for i in range(len(report) - 1)
        )
        return ascending or descending

    if is_sorted_and_valid(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if is_sorted_and_valid(modified_report):
            return True

    return False


valid_reports = 0

for report in reports:
    if is_valid_report(report):
        valid_reports += 1

print(valid_reports)
