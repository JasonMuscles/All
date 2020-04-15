import csv

file_name = "death_valley_2014.csv"

try:
    with open(file_name) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # for index, column_header in enumerate(header_row):
        #     print(index, column_header)
        highs = []
        for row in reader:
            highs.append(row[1])
        print(highs)

except FileNotFoundError:
    print("文件：'" + file_name + "' 不存在")
