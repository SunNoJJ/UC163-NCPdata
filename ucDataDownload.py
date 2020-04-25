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

            ##现存确诊
            now_con = num.findall(re.findall("(<span>.*?span)", now_confirms[i])[0])[0].replace("-","-1")
            ##累计确诊 'second-cell"><span data-v-189f4250="">1356</span></div'
            confirm = num.findall(re.findall("(<span>.*?span)",item_confirms[i])[0])[0].replace("-","-1")
            ##新增确诊'cell-incr"><span data-v-eaacc57a="">4714</span>'
            new_confirm = re.findall('(>.*?<)',item_newconfirms[i].replace("><",''))[0].replace('>',"").replace("<","").replace("-","-1")
            ##累计治愈'span-green">49130</span'  'span-green">-</span'
            heals = re.findall("(>.*?<)", item_heals[i])[0].replace(">", "").replace("<", "").replace("-","-1")
            ##累计死亡'span-gray">3046</span' 'span-gray">-</span'
            deads_num = re.findall("(>.*?<)", item_deads[2*i])[0].replace(">", "").replace("<", "").replace("-","-1")
            deads_rate = re.findall("(>.*?<)", item_deads[2 * i+1])[0].replace(">", "").replace("<", "").replace("-", "-1")
            deads =deads_num +"="+deads_rate
            populationcsv = re.findall("(>.*?<)", population[i].replace("><", ""))[0].replace(">", "").replace("<", "").replace("-","-1")
            sureRatecsv = re.findall("(>.*?<)", sureRate[i].replace("><", ""))[0].replace(">", "").replace("<", "").replace("-","-1")
            data = [primary, now_con, confirm, new_confirm, heals, deads,populationcsv,sureRatecsv]
            print(i,primary, now_con, confirm, new_confirm, heals, deads,populationcsv,sureRatecsv)
            # dataList.append(data)
            writer.writerow(data)





def getInfo():
    mainUrl = "https://iflow.uc.cn/webview/article/newspecial.html?ab_tag_page_biz=,3055,3057,2970,2992,3023,2855,2662,2999,2655,3028,3026,2130,2890,2957,3031,3049,3047,3048,2154,2940,2885,3052,3029,3020,_,3055_B,3057_A,2970_B,2992_D,3023_A,2855_A,2662_C,2999_B,2655_C,3028_D,3026_B,2130_C,2890_E,2957_C,3031_B,3049_D,3047_C,3048_F,2154_C,2940_B,2885_B,3052_A,3029_D,3020_B,&uc_biz_str=S%3Acustom%7CC%3Atitlebar_hover_2&aid=3804775841868884355&cid=100&uc_param_str=lodndseiwifrvesvntgipf&sm_article_id=3804775841868884355&uc_h5_page_name=iflowspecial&feiyan=1&feiyan_jump=-3&external=1&app=uc-iflow&enterfrom=xxl-47haiwaicard&zzd_from=uc-iflow&dl_type=2&recoid=11431670214199215394&activity=1&activity2=1"
    time.sleep(1)
    browser.get(mainUrl)
    time.sleep(2)
    browser.find_element_by_class_name("expand-text").click()##模拟点击
    clickNo = 0
    while True:
        try:
            browser.find_element_by_class_name("expand-text").click()##模拟点击
            clickNo = clickNo+1
            time.sleep(1)
            print("第_"+str(clickNo)+"_次点击。。。。。。。。")
        except NoSuchElementException:
            print("点击完成")
            break
    time.sleep(0.3)
    if clickNo<60:
        print("网页源码变化，请修正。。。。。。。。")
        exit()
    pageSource1 = browser.page_source

    pageSource = re.findall(r'(人口数.*便民服务)', pageSource1)[0]  ##

    ## 国内 最短匹配：.*?
    primary_cells = re.findall('(primary-cell.*?div)',pageSource)##地区2
    now_confirms = re.findall('(cell-sure".*?div)', pageSource) ##现存确诊
    item_confirms = re.findall('(cell-sure-sum.*?div)', pageSource)  ##累计确诊1
    item_newconfirms = re.findall('(cell-incr.*?/div)',pageSource)##新增确诊4

    item_heals = re.findall('(span-green.*?span)', pageSource)  ##累计治愈1

    item_deads = re.findall('(span-gray.*?span)', pageSource)  ##累计死亡、死亡率
    sureRate = re.findall('(row-sureRate.*?div)', pageSource)  ##每十万人确诊数
    population = re.findall('(row-population.*?div)', pageSource)  ##总人口数


    print("地区",len(primary_cells),"现存确诊",len(now_confirms),"累计确诊",len(item_confirms),
          "新增确诊",len(item_newconfirms),"累计治愈",len(item_heals),"累计死亡",len(item_deads),
          "人口数（万）",len(population),"每10万人确诊",len(sureRate))
    validateString_list(primary_cells,now_confirms,item_confirms,item_newconfirms,item_deads,item_heals,population,sureRate)


if __name__ =="__main__":
    getInfo()
    browser.quit()