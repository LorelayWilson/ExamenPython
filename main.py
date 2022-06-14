import csv

def read_data(f1, f2):
    dic = {}
    with open(f1, 'r') as file1:
        with open(f2,'r') as file2:
            reader1 = csv.reader(file1)
            reader2 = csv.reader(file2)
            for row in reader1:
                dic[row[0]] = {"description":row[3],
                                "id":"",
                                "lat":"",
                                "lon":"",
                                "name":row[2]}

            for row 
    
    print(dic)



if __name__ == "__main__":
    f1 = "stops.csv"
    f2 = "stops_data.csv"
    diccionario = read_data(f1,f2)
    