import csv

with open("employee_writer.csv", mode="w") as employee_file:
    csv_writer = csv.writer(
        employee_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
    )

    # writing list of rows
    csv_writer.writerow(["John Smith", "IT", "Jan"])

    # using a Dictionary
    with open("employee_writer_dict.csv", mode="w") as employee_file_dict:
        dict_header = ["name", "dept", "birth_mon"]
        csv_writer_dict = csv.DictWriter(employee_file_dict, fieldnames=dict_header)

        # writing list of rows
        csv_writer_dict.writeheader()
        csv_writer_dict.writerow(
            {"name": "John Smith", "dept": "Accountant", "birth_mon": "Feb"}
        )
