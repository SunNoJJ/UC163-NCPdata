# coding: utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import re
import csv

browser = webdriver.Firefox()

chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless') #增加无界面选项
chrome_options.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题

# 启动浏览器，获取网页源代码
browser = webdriver.Chrome(executable_path=r'D:\Program Files (x86)\chromedriver.exe', chrome_options=chrome_options)

def validateString_list(primary_cells,now_confirms,item_confirms,item_newconfirms,item_deads,item_heals,population,sureRate):
    zh = re.compile(r'[\u4e00-\u9fa5]+')  # 查找中文
    num = re.compile(r'\d+')  # 查找数字
    dataList = ["地区","现存确诊","累计确诊","新增确诊","累计治愈","累计死亡","人口数（万）","每10万人确诊"]
    nowTime = time.strftime("%Y_%m_%d_%H_%M", time.localtime()) ##%Y_%m_%d_%H_%M_%S
    with open("./CsvData/UC/"+nowTime+'_uc.csv', 'w', encoding='utf-8-sig', newline='') as csf:
        writer = csv.writer(csf)
        writer.writerow(dataList)
        cell_inc = 4
        flage = 0  ##population,sureRate
        for i in range(len(primary_cells)):
            ##地区'primary-cell">湖北省</div'
            primary = zh.findall(primary_cells[i].replace("<br>", ""))[0]
            print(i,"地区",primary,flage)
            ##现存确诊
            now_con = num.findall(re.findall("(<span>.*?span)", now_confirms[i])[0])[0]
            ##累计确诊 'second-cell"><span data-v-189f4250="">1356</span></div'
            confirm = num.findall(re.findall("(<span>.*?span)",item_confirms[i])[0])[0]
            ##新增确诊'cell-incr"><span data-v-eaacc57a="">4714</span>'
            new_confirm = re.findall('(>.*?<)',item_newconfirms[i+cell_inc].replace("><",''))[0].replace('>',"").replace("<","")
            ##累计治愈'span-green">49130</span'  'span-green">-</span'
            heals = re.findall("(>.*?<)", item_heals[i])[0].replace(">", "").replace("<", "")
            ##累计死亡'span-gray">3046</span' 'span-gray">-</span'
            deads = re.findall("(>.*?<)", item_deads[i])[0].replace(">", "").replace("<", "")
            if flage == 0:
                data=[primary,now_con,confirm,new_confirm,heals,deads,"-","-"]
            else:
                populationcsv = re.findall("(>.*?<)", population[i-flage].replace("><", ""))[0].replace(">", "").replace("<", "")
                sureRatecsv = re.findall("(>.*?<)", sureRate[i-flage].replace("><", ""))[0].replace(">", "").replace("<", "")
                data = [primary, now_con, confirm, new_confirm, heals, deads,populationcsv,sureRatecsv]
            if "西藏自治区"==zh.findall( primary_cells[i].replace("<br>",""))[0]:
                cell_inc = 5
                flage = i
                print("######flage:",flage)
            # dataList.append(data)
            writer.writerow(data)





def getInfo():
    mainUrl = "https://iflow.uc.cn/webview/article/newspecial.html?ab_tag_page_biz=,2872,2891,2818,1744,2793,2855,2662,2655,2658,2795,2130,2890,2824,2861,2869,2775,2154,2827,2803,_,2872_A,2891_A,2818_A,1744_B,2793_C,2855_A,2662_C,2655_C,2658_D,2795_D,2130_C,2890_E,2824_A,2861_A,2869_C,2775_A,2154_C,2827_F,2803_B,&uc_biz_str=S%3Acustom%7CC%3Atitlebar_hover_2&aid=3804775841868884355&cid=100&uc_param_str=lodndseiwifrvesvntgipf&sm_article_id=3804775841868884355&uc_h5_page_name=iflowspecial&feiyan=1&feiyan_jump=-3&external=1&app=uc-iflow&enterfrom=xxl-47haiwaicard&zzd_from=uc-iflow&dl_type=2&recoid=13764386211984591365&activity=1&activity2=1"
    time.sleep(1)
    browser.get(mainUrl)
    time.sleep(1)
    browser.find_element_by_class_name("expand-text").click()##模拟点击

    while True:
        try:
            browser.find_element_by_class_name("expand-text").click()##模拟点击
            time.sleep(1)
            print("正在点击。。。。。。。。")
        except NoSuchElementException:
            print("点击完成")
            break
    time.sleep(3)
    pageSource = browser.page_source
    ## 国内 最短匹配：.*?
    primary_cells = re.findall('(primary-cell.*?div)',pageSource)##地区2
    now_confirms = re.findall('(cell-sure".*?div)', pageSource) ##现存确诊
    item_confirms = re.findall('(cell-sure-sum.*?div)', pageSource)  ##累计确诊1
    item_newconfirms = re.findall('(cell-incr.*?/div)',pageSource)##新增确诊4
    item_deads = re.findall('(span-gray.*?span)', pageSource)##累计死亡1
    item_heals = re.findall('(span-green.*?span)', pageSource)  ##累计治愈1
    population = re.findall('(row-population.*?万)',pageSource)  ##总人口数
    sureRate = re.findall('(row-sureRate.*?div)', pageSource)  ##总人口数



    validateString_list(primary_cells,now_confirms,item_confirms,item_newconfirms,item_deads,item_heals,population,sureRate)


if __name__ =="__main__":
    getInfo()
    browser.quit()