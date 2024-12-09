import csv
with open("F:\\Ostad\Mod 8\\business_Fdata.csv", "r") as csv_file:
    reader_variable = csv.reader(csv_file)
    #for row in reader_variable:
    #   print(row)
    for i, row in enumerate(reader_variable):
        if (i<10):
            print(row)
        else:
            break

with open("F:\Ostad\Mod 8\data.csv", mode= "w", newline='') as csv_file:
    writer_variable = csv.writer(csv_file)
    for i in range(5):
        writer_variable.writerow([1, 2, 3, 4])