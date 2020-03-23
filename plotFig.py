# coding:utf-8
import os
import csv
import matplotlib.pyplot as plt

## 获取文件名
file_names = os.listdir("./CsvData/UC/")
print(file_names)
## 文件名拼接路径
file_list = [os.path.join("./CsvData/UC/",file) for file in file_names]
print(file_list)
country = "湖北省"
def readCsv(list_f):
    now_confirms = [] ##现存确诊
    item_confirms = [] ##累计确诊1
    item_newconfirms = [] ##新增确诊4
    item_deads = [] ##累计死亡1
    item_heals = [] ##累计治愈1
    for csvF in list_f:
        with open(csvF, encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            header = next(reader)
            print(header)
            for row in reader:
                if row[0] == country:
                    now_confirms.append(int(0 if row[1]=="-" else row[1]))
                    item_confirms.append(int(0 if row[2]=="-" else row[2]))
                    item_newconfirms.append(int(0 if row[3]=="-" else row[3]))
                    item_deads.append(int(0 if row[4]=="-" else row[4]))
                    item_heals.append(int(0 if row[5]=="-" else row[5]))
    return now_confirms,item_confirms,item_newconfirms,item_deads,item_heals
def plotTrend(now_confirms,item_confirms,item_newconfirms,item_deads,item_heals):
    x = range(len(now_confirms))
    plt.plot(x,now_confirms,label='现存确诊')
    plt.plot(x,item_confirms,label='累计确诊')
    plt.plot(x,item_newconfirms,label='新增确诊')
    plt.plot(x,item_deads,label='累计治愈')
    plt.plot(x,item_heals,label='累计死亡')
    ## 参数配置
    plt.legend(loc='upper left')
    plt.title(country + " 单位：人")
    ## 将X轴显示为日期
    xTicLis = file_names
    plt.xticks(x, [name.replace("_uc.csv", '') for name in xTicLis], color='blue', rotation=15)
    plt.yticks([])
    plt.show()
def plotHist(now_confirms,item_confirms,item_newconfirms,item_deads,item_heals):
    x = range(len(now_confirms))
    plt.hist(x, now_confirms, label='现存确诊')
    plt.hist(x, item_confirms, label='累计确诊')
    plt.hist(x, item_newconfirms, label='新增确诊')
    plt.hist(x, item_deads, label='累计治愈')
    plt.hist(x, item_heals, label='累计死亡')
    plt.legend()
    plt.show()
def plotBar(now_confirms, item_confirms, item_newconfirms, item_deads, item_heals):
    x = range(len(now_confirms))
    plt.figure(figsize=(12,6))## 设置图片大小
    # plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)## 设置图片边距
    ## 画图
    plt_now_confirms = plt.bar(x, now_confirms, width=0.2,label='现存确诊',color= "red")
    plt_item_confirms = plt.bar([i + 0.2 for i in x], item_confirms, width=0.2,label='累计确诊')
    plt_item_newconfirms = plt.bar([i + 0.4 for i in x], item_newconfirms, width=0.2,label='新增确诊')
    plt_item_deads = plt.bar([i + 0.6 for i in x], item_deads,width=0.2,label='累计治愈',color= "green")
    plt_item_heals = plt.bar([i + 0.8 for i in x], item_heals, width=0.2, label='累计死亡',color= "black")

    ## 为每柱添加值
    for index,value in enumerate(plt_now_confirms):
        height_now_confirms = value.get_height()
        height_item_confirms = plt_item_confirms[index].get_height()
        height_item_newconfirms = plt_item_newconfirms[index].get_height()
        height_item_deads = plt_item_deads[index].get_height()
        height_item_heals = plt_item_heals[index].get_height()

        plt.text(value.get_x() + value.get_width() / 2, height_now_confirms + 1, str(height_now_confirms),
                 ha="center", va="bottom",rotation=-70)
        plt.text(plt_item_confirms[index].get_x() + plt_item_confirms[index].get_width() / 2, height_item_confirms + 1, str(height_item_confirms),
                 ha="center", va="bottom",rotation=-70)
        plt.text(plt_item_newconfirms[index].get_x() + plt_item_newconfirms[index].get_width() / 2, height_item_newconfirms + 1, str(height_item_newconfirms),
                 ha="center", va="bottom",rotation=-70)
        plt.text(plt_item_deads[index].get_x() + plt_item_deads[index].get_width() / 2, height_item_deads + 1, str(height_item_deads),
                 ha="center", va="bottom",rotation=-70)
        plt.text(plt_item_heals[index].get_x() + plt_item_heals[index].get_width() / 2, height_item_heals + 1, str(height_item_heals),
                 ha="center", va="bottom",rotation=-70)
    ## 参数配置
    plt.legend(loc='upper left')
    plt.title(country + " 单位：人")
    ## 将X轴显示为日期
    xTicLis = file_names
    plt.xticks(x, [name.replace("_uc.csv", '') for name in xTicLis], color='blue', rotation=15)
    plt.yticks([])
    ## 保存与展示
    plt.savefig("./img/"+country+".png")
    plt.show()


if __name__ == '__main__':
    now_confirms,item_confirms,item_newconfirms,item_deads,item_heals = readCsv(file_list)
    plotBar(now_confirms,item_confirms,item_newconfirms,item_deads,item_heals)


