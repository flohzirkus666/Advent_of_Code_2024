# load contents from file, put each element into a list, seperate by line-breaks
with open("puzzle2.txt") as f:
    reports = [list(map(int, line.split())) for line in f]

safe_reports = 0

for report in reports:
    if report == sorted(report) or report == sorted(report, reverse=True):
        if all(
            abs(report[i] - report[i + 1]) in [1, 2, 3] for i in range(len(report) - 1)
        ):
            safe_reports += 1

print(safe_reports)
