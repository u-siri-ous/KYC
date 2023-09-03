import csv

with open(f'data/datasets/fossil/fossil_ds.CSV', mode='r', encoding='latin-1') as file:
        # Create a CSV reader
        print(file)
        csv_reader = csv.reader(file)

        # Skip the header row
        next(csv_reader)

        # Perform the query
        for row in csv_reader:
            if row[0] == 'Psyduck':
               # p_details = row
                print(row)