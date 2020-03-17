# coding: utf-8
from selenium import webdriver
import time
import re
import csv
import os
tt = 'https://user.qzone.qq.com/383817842/infocenter'

browser = webdriver.Firefox()

chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless') #增加无界面选项
chrome_options.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题

# 启动浏览器，获取网页源代码
browser = webdriver.Chrome(executable_path=r'D:\Program Files (x86)\chromedriver.exe', chrome_options=chrome_options)

def validateString_list(chart_table_names,chart_table_confirms,chart_table_deads,chart_table_heals):
    dataList = []
    nowTime = time.strftime("%Y_%m_%d_%H_%M", time.localtime()) ##%Y_%m_%d_%H_%M_%S
    with open("./CsvData/"+nowTime+'_163.csv', 'w', encoding='utf-8-sig', newline='') as csf:
        for i in range(len(chart_table_confirms)):
            data=[chart_table_names[i].replace("chart_table_name\">","").replace("chart_table_name \">","").replace("chart_table_name chart_table_name_long\">","").replace("</div",""),
                     chart_table_confirms[i].replace("chart_table_confirm\">","").replace("</div",""),
                     chart_table_deads[i].replace("chart_table_dead\">","").replace("</div",""),
                     chart_table_heals[i].replace("chart_table_heal\">","").replace("</div","")]
            dataList.append(data)
            writer = csv.writer(csf)
            writer.writerow(data)



def getInfo():
    mainUrl = "https://wp.m.163.com/163/page/news/virus_report/index.html?_nw_=1&_anw_=1#world_block"
    time.sleep(3)
    browser.get(mainUrl)
    browser.get(mainUrl)
    browser.get(mainUrl)
    time.sleep(5)
    pageSource = browser.page_source
    ## 国内 最长匹配
    item_names = re.findall('(item_name.*span)',pageSource)##地区
    item_newconfirms = re.findall('(item_newconfirm.*span)',pageSource)##新增确诊
    item_confirms = re.findall('(item_confirm.*span)', pageSource)##确诊
    item_deads = re.findall('(item_dead.*span)', pageSource)##累计死亡
    item_heals = re.findall('(item_heal.*span)', pageSource)  ##累计治愈
    item_mores = re.findall('(item_more.*span)', pageSource)  ##疫情
    ## 国外
    chart_table_names = re.findall('(chart_table_name.*div)', pageSource) ##国家
    chart_table_confirms = re.findall('(chart_table_confirm.*div)', pageSource) ##确诊
    chart_table_deads = re.findall('(chart_table_dead.*div)', pageSource) ##死亡
    chart_table_heals = re.findall('(chart_table_heal.*div)', pageSource) ##治愈

    validateString_list(chart_table_names,chart_table_confirms,chart_table_deads,chart_table_heals)


if __name__ =="__main__":
    getInfo()
    browser.quit()