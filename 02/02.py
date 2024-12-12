def is_report_safe(report: list[int]) -> bool:
    last_change = None
    for i in range(len(report)):
        
        if i == len(report) - 1:
            return True
        else:

            if not (0 < abs(change:=report[i] - report[i+1]) <= 3):

                return False
            elif last_change == None or (last_change < 0 and change < 0) or (last_change > 0 and change > 0):
                last_change = change
                continue
            else:
                return False





def find_unsafe_reports(reports):
    return [report for report in reports if not is_report_safe(report)]


def try_to_fix_report(report):
    # print(report)
    for i in range(len(report)):
        patched_report = report[:i]+report[i+1:]
        # print(patched_report)
        if is_report_safe(patched_report):
            return True
        else:
            continue
    return False


with open("02/test-inp") as f:
    report_data = [list(map(int, report.split(" "))) for report in f.read().splitlines()]

print(sum([1 if is_report_safe(report) else 0 for report in report_data ]))
print(sum([1 if is_report_safe(report) else 0 for report in report_data ]) + sum([1 if try_to_fix_report(report) else 0 for report in find_unsafe_reports(report_data)]))


with open("02/input") as f:
    report_data = [list(map(int, report.split(" "))) for report in f.read().splitlines()]

print(sum([1 if is_report_safe(report) else 0 for report in report_data ]))
print(sum([1 if is_report_safe(report) else 0 for report in report_data ]) + sum([1 if try_to_fix_report(report) else 0 for report in find_unsafe_reports(report_data)]))


