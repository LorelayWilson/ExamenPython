import csv

def read_data(f1, f2):
    diccionario = {}
    with open(f1, 'r') as file1:
        with open(f2,'r') as file2:
            reader1 = csv.reader(file1)
            reader2 = csv.reader(file2)
            for row in reader2:
                print(row)  



if __name__ == "__main__":
    f1 = "stops.csv"
    f2 = "stops_data.csv"
    diccionario = read_data(f1,f2)
    