# coding:utf-8
import os
import csv
import matplotlib.pyplot as plt

## 获取文件名
file_names = os.listdir("./CsvData/")
print(file_names)
## 文件名拼接路径
file_list = [os.path.join("./CsvData/",file) for file in file_names]
print(file_list)

def readCsv(list_f):
    for csvF in list_f:
        with open(csvF, encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            header = next(reader)
            print(header)
            for row in reader:
                if row[0] == '法国':
                    print(row)

def plotPig():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    readCsv(file_list)
    plotPig()

