import csv

with open("employeedata.txt") as csv_files:
    csv_reader = csv.reader(csv_files, delimiter=",")
    line_count = 0
    for rows in csv_reader:
        if line_count == 0:
            print(f'Columns Names are {", ".join(rows)}')
        else:
            print(f"\t {rows[0]} works in {rows[1]} and was born in {rows[2]}")
        line_count += 1
    print(f"{line_count} lines read")
