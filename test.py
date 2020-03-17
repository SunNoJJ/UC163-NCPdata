# conding：utf-8
import re
import csv

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
if __name__ == '__main__':
    reText()


