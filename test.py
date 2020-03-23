# conding：utf-8
import re
import csv
import matplotlib.pyplot as plt

def readCsv():
    with open('data.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        print(header)
        for row in reader:
            print(row)

def writeRelut():
    header = ['name', 'password', 'status']

    data = [
        ['abc', '123456', 'PASS'],
        ['张五', '123#456', 'PASS'],
        ['张#abc123', '123456', 'PASS'],
        ['666', '123456', 'PASS'],
        ['a b', '123456', 'PASS']
    ]

    with open('result.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
def reText():
    strs = r'primary-cell">广西壮族<br>自治区</div'
    # num = re.compile(r'\d+')  # 查找数字
    # print(num.findall(re.findall("(=.*span)",strs)[0]))

    print(re.findall(">.*<", 'span-gray">1235</span')[0].replace(">", "").replace("<", ""))

    # zh = re.compile(r'[\u4e00-\u9fa5]+')  # 查找中文
    # print(re.findall("([\u4e00-\u9fa5]*)?", strs))
    #
    # print(zh.findall( strs))
def rePlaceList():
    lis = ['HKN', 'TNN', '07:00', '07:35', '00:35', '', '有', '有', 'x', '', '', '', '', 'x', '18', '']
    str = ['', 'x']
    res = ["-" if x in str else x for x in lis]
    print(res)
    for i in range(len(lis)):
        if lis[i] in str:
            lis[i] = '-'
    print(lis)

    for index,name in enumerate(lis):
        lis[index] = name.replace("_uc.csv",'')
    print(lis)
    list3 = [name.replace("_uc.csv",'') for name in lis]
    print(list3,end="大幅度发")
def plotXY():
    x = range(5)
    y = [x1*x1 for x1 in x]
    plt.plot(x,y)
    plt.show()
    y = [x1 for x1 in x]
    plt.plot(x, y)
    plt.show()
if __name__ == '__main__':
    a = 2
    b = 1
    h = ""

    h = "变量1" if a > b else "变量2"

    print(h)


