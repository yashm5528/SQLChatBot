import csv
import os

def convert_to_csv(file):
    rows = []

    with open(file) as fh:
        for line in fh:
            split_data = list(line.strip().split(" ||| ", 2))
            rows.append(split_data)

    fields = ["HumanQuery", "SQLQuery"]
    file_name = os.path.basename(file)
    csv_file = os.path.join(r"C:\Users\anark\Desktop\Capstone\Implementation\Modulated_code\Testing", f"{file_name}.csv")

    with open(csv_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

convert_to_csv('Testing\geography.uw.test.txt')
convert_to_csv('Testing\geography.uw.train.txt')
convert_to_csv('Testing\geography.uw.dev.txt')