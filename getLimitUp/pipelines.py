# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import datetime
from operator import itemgetter, attrgetter
import pymongo
from scrapy.conf import settings

class CShareTdxSave:
    @staticmethod
    def shareCodeSave(lists):
        fileNameSws = 'C:/sws2010/T0002/blocknew/ZRZT.blk'
        fsws = open(fileNameSws, "w")
        for i in range(len(lists)):        
            fsws.write('\n')
            code = lists[i][0]
            if('6' == code[0]):
                fsws.write('1')
            else:
                fsws.write('0')
            fsws.write(code)
        fsws.close()
        
        fileNameHt = 'C:/new_haitong/T0002/blocknew/ZXG.blk'
        fht = open(fileNameHt, "w")
        for i in range(len(lists)):        
            fht.write('\n')
            code = lists[i][0]
            if('6' == code[0]):
                fht.write('1')
            else:
                fht.write('0')
            fht.write(code)
        fht.close()
    
    @staticmethod    
    def getCurrentTimeInt():
        #获取当前时间
        now_time = datetime.datetime.now().strftime('%H%M%S')
        now_time_int = int(now_time)
        return now_time_int

class GetlimitupPipeline(object):
    def __init__(self):
        
        now = datetime.datetime.now()
        string = now.strftime('%Y%m%d')
        fileName = 'D:/share/zhangting_' + string + '.txt'
        self.fwencai = open(fileName, "w")
        
        #数据库
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = 'zhangting_' + string
        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.client = mydb[sheetname]
        
        pass
        
    def process_item(self, item, spider):
        '''
        string = item['dateYMD']
        fileName = 'D:/share/zhangting_' + string + '.txt'
        self.fwencai = open(fileName, "w")
        
        
        #数据库
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = 'zhangting_' + string
        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.client = mydb[sheetname]
        '''
        
        mongoData = dict(item)
        self.client.insert(mongoData)
        
        print(item['minLen'])
        lists = []
        for i in range(item['minLen']):
            list = []
            list.append(item['code'][i])
            list.append(item['name'][i])
            list.append(item['liangBi'][i])  
            list.append(item['ziYouHuanShouLv'][i])
            list.append(item['ziYouLiuTongShiZhi'][i])
            list.append(item['continueDay'][i])
            list.append(item['firstLimitTime'][i])
            list.append(item['lastLimitTime'][i])
            list.append(item['limitOpenCount'][i])
            list.append(item['limitVsDeal'][i])
            list.append(item['limitVsCirculate'][i])#10
            list.append(item['limitUpMoney'][i])
            list.append(item['limitReason'][i])
            list.append(item['guXingPingFen'][i])
            list.append(item['limitShareNumber'][i])
            list.append(item['startPrice'][i])
            list.append(item['endPrice'][i])
            list.append(item['maxPrice'][i])
            list.append(item['minPrice'][i])
            list.append(item['zhenFu'][i])
            list.append(item['chengJiaoE'][i])
            list.append(item['chengJiaoLiang'][i])
            list.append(item['huanShouLv'][i])  
            list.append(item['ziYouLiuTongGu'][i])
            list.append(item['liuTongGu'][i]) 
            list.append(item['liuTongShiZhi'][i])       
            list.append(item['ipoDays'][i])
            list.append(item['zongGuBen'][i])
            
            lists.append(list)
        
        # sort as limitVsCirculate
        lists.sort(key = lambda x:(float(x[10])), reverse = True)
        
        self.fwencai.write(str(len(lists)))
        text = '\ncode\t'+'name\t'+'量比\t'+'实际换手\t'+'自由流通市值\t'+'连续涨停天数\t'+'首次涨停时间\t'+'最终涨停时间\t'+'涨停打开次数\t'+'封成比\t'+'封流比\t'+'封单额\t'+'涨停原因\t'+'股性评分\t'+'封单量\t'+'开盘价\t'+'收盘价\t'+'最高价\t'+'最低价\t'+'振幅\t'+'成交额\t'+'成交量\t'+'换手率\t'+'自由流通股\t'+'流通A股\t'+'流通市值\t'+'上市天数 '+'总股本\n'
        self.fwencai.write(text)
        
        for i in range(len(lists)):
            for j in range(len(lists[i])):
                #printStr = '%(item)-5s'%{'item':str(lists[i][j])}
                printStr = '{: <10s}'.format(str(lists[i][j]))
                self.fwencai.write(printStr + '\t')
            self.fwencai.write('\n')
        self.fwencai.write('\n')
        
        
        #
        shareSave = CShareTdxSave()        
        if(shareSave.getCurrentTimeInt() > 150000):
            shareSave.shareCodeSave(lists)
        
        #self.fwencai.close()
        
        
        #mongoData = dict(lists)
        #self.client.insert(mongoData)
        
        return item

        
    def close_spider(self, spider):
        self.fwencai.close()
        #self.f.close()
        #self.client.close()
        pass
        
        