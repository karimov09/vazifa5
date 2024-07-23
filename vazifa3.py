import os
import csv
class LoadCsv:
    def __init__(self, name):
        self.name = name
        if not os.path.isfile(self.filename):
            raise FileNotFoundErro(f" {self.filename}")
    def reader(self):
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                for i in csv_reader:
                    print(i)
        except Exception as e:
            print(f"{e}")
name = 'user.csv'
n = LoadCsv(name)
n.reader()