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
import struct

class CShareTdxSave:
    @staticmethod
    def zrzt_change(self, fileName, lists):
        fp = open(fileName, "w")
        for i in range(len(lists)):        
            fp.write('\n')
            code = lists[i][0]
            if('6' == code[0]):
                fp.write('1')
            else:
                fp.write('0')
            fp.write(code)
        fp.close()
        
    def zxg_change(self, fileName, lists):
        fp = open(fileName, 'r')
        lines = fp.readlines()
        num = len(lines)
        fp.close()
        
        list = []
        for i in range(len(lists)):
            code = lists[i][0]
            if('6' == code[0]):
                list.append('1' + code + '\n')
            else:
                list.append('0' + code + '\n')
                
        for i in range(len(list)):
            for j in range(len(lines)):        
                code = lines[j]
                if(list[i] == code):
                    lines.pop(j)
                    break
        fp = open(fileName, "w")
        
        fp.write('\n')
        for i in range(len(list)):
            fp.write(list[i])
        for i in range(len(lines)):
            fp.write(lines[i])
        
        fp.close()
        
    def mark_change(self, fileName, lists):
        #fht = open(fileNameHt, 'r', encoding='UTF-8')
        fp = open(fileName, 'r')
        lines = fp.readlines()
        num = len(lines)
        fp.close()
        
        group = (int)(num / 4)
        mark = lines[1:group]
        tip = lines[(group+1):2*group]
        tipword = lines[(2*group+1):3*group]
        time = lines[(3*group+1):4*group] 
        
        list = []
        for i in range(len(lists)):
            code = lists[i][0]
            if('6' == code[0]):
                list.append('01' + code + '=')
            else:
                list.append('00' + code + '=')
        
        for i in range(len(list)):
            for j in range(len(mark)):        
                code = mark[j][0:9]
                if(list[i] == code):
                    mark.pop(j)
                    break
        for i in range(len(list)):
            for j in range(len(tip)):        
                code = tip[j][0:9]
                if(list[i] == code):
                    tip.pop(j)
                    break            
        for i in range(len(list)):
            for j in range(len(tipword)):        
                code = tipword[j][0:9]
                if(list[i] == code):
                    tipword.pop(j)
                    break
        for i in range(len(list)):
            for j in range(len(time)):        
                code = time[j][0:9]
                if(list[i] == code):
                    time.pop(j)
                    break
        
        fp = open(fileName, "w")            
        fp.write('[MARK]\n')
        for i in range(len(list)):
            fp.write(list[i] + '7\n')
        for i in range(len(mark)):
            fp.write(mark[i])
        fp.write('[TIP]\n')
        for i in range(len(list)):
            continueDay = lists[i][5]
            fp.write(list[i] + continueDay + '\n')
        for i in range(len(tip)):
            fp.write(tip[i])
        fp.write('[TIPWORD]\n')
        for i in range(len(lists)):
            limitReason = lists[i][12]
            fp.write(list[i] + limitReason + '\n')
        for i in range(len(tipword)):
            fp.write(tipword[i])
        fp.write('[TIME]\n')
        for i in range(len(list)):
            firstLimitTime = lists[i][6]
            fTIme = str(int(firstLimitTime.replace(':', ''), 10))
            fp.write(list[i] + fTIme + '\n')
        for i in range(len(time)):
            fp.write(time[i])
        fp.close()
        
        return list
        
    def warn_change(self, fileName, list):
        fp = open(fileName, 'rb')
        read_buf = fp.read(868)
        fp.close()
        fp = open(fileName, "wb")
        #a = struct.pack('B', int(read_buf))
        fp.write(read_buf)
        a = struct.pack('L', int(len(list)))
        fp.write(a)
        for i in range(len(list)):
            for x in range(4):
                a = struct.pack('B', 0)
                fp.write(a)
            fp.write(str.encode(list[i][2:8]))
            for x in range(17):
                a = struct.pack('B', 0)
                fp.write(a)
            a = struct.pack('B', 1)
            fp.write(a)
            for x in range(33):
                a = struct.pack('B', 0)
                fp.write(a)
                
        fp.close()
        
    def shareCodeSave(self, lists):
        '''
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
        '''
        
        '''
        fileNameSws = 'C:/sws2010/T0002/blocknew/ZXG.blk'        
        
        fsws = open(fileNameSws, "a")
        for i in range(len(lists)):        
            fsws.write('\n')
            code = lists[i][0]
            if('6' == code[0]):
                fsws.write('1')
            else:
                fsws.write('0')
            fsws.write(code)
        fsws.close()
        '''
        
        fileNameHt = 'C:/new_haitong/T0002/blocknew/ZXG.blk'
        self.zxg_change(fileNameHt, lists)
        self.zxg_change('D:/new_jyqyb/T0002/blocknew/ZXG.blk', lists)
        self.zxg_change('D:/zd_cjzq/T0002/blocknew/ZXG.blk', lists)
        self.zxg_change('D:/new_jyplug/T0002/blocknew/ZXG.blk', lists)
        
        '''
        fht = open(fileNameHt, 'r')
        lines = fht.readlines()
        num = len(lines)
        fht.close()
        
        list = []
        for i in range(len(lists)):
            code = lists[i][0]
            if('6' == code[0]):
                list.append('1' + code + '\n')
            else:
                list.append('0' + code + '\n')
                
        for i in range(len(list)):
            for j in range(len(lines)):        
                code = lines[j]
                if(list[i] == code):
                    lines.pop(j)
                    break
        fht = open(fileNameHt, "w")
        
        fht.write('\n')
        for i in range(len(list)):
            fht.write(list[i])
        for i in range(len(lines)):
            fht.write(lines[i])
        
        fht.close()
        '''
        '''    
        fht = open(fileNameHt, "a")
        for i in range(len(lists)):        
            fht.write('\n')
            code = lists[i][0]
            if('6' == code[0]):
                fht.write('1')
            else:
                fht.write('0')
            fht.write(code)
        fht.close()
        '''
        '''
        fileNameHt = 'D:/Softs/通达信/通达信金融终端海通证券和谐版/T0002/blocknew/ZXG.blk'
        fht = open(fileNameHt, "a")
        for i in range(len(lists)):        
            fht.write('\n')
            code = lists[i][0]
            if('6' == code[0]):
                fht.write('1')
            else:
                fht.write('0')
            fht.write(code)
        fht.close()
        
        #save share mark
        fileNameHt = 'D:/Softs/通达信/通达信金融终端海通证券和谐版/T0002/mark.dat'
        fht = open(fileNameHt, "w")
        fht.write('[MARK]\n')
        for i in range(len(lists)):
            code = lists[i][0]
            if('6' == code[0]):
                fht.write('01')
            else:
                fht.write('00')
            fht.write(code + '=7\n')
        fht.write('[TIP]\n')
        for i in range(len(lists)):
            code = lists[i][0]
            if('6' == code[0]):
                fht.write('01')
            else:
                fht.write('00')
            fht.write(code + '=\n')
        fht.write('[TIPWORD]\n')
        for i in range(len(lists)):
            code = lists[i][0]
            if('6' == code[0]):
                fht.write('01')
            else:
                fht.write('00')
            limitReason = lists[i][12]
            fht.write(code + '=' + limitReason + '\n')
        fht.write('[TIME]\n')
        for i in range(len(lists)):
            code = lists[i][0]
            if('6' == code[0]):
                fht.write('01')
            else:
                fht.write('00')
            limitReason = lists[i][12]
            fht.write(code + '=0\n')
        fht.close()
        '''
        
        fileNameHt = 'C:/new_haitong/T0002/mark.dat'  
        list1 = self.mark_change(fileNameHt, lists)        
        list2 = self.mark_change('D:/new_jyqyb/T0002/mark.dat', lists)
        list3 = self.mark_change('D:/zd_cjzq/T0002/mark.dat', lists)        
        list4 = self.mark_change('D:/new_jyplug/T0002/mark.dat', lists)
        
        ##############读写条件预警文件
        fileNameHt = 'C:/new_haitong/T0002/col_cfgwarn.dat'  
        self.warn_change(fileNameHt, list1)
        self.warn_change('D:/new_jyqyb/T0002/col_cfgwarn.dat', list2)
        self.warn_change('D:/zd_cjzq/T0002/col_cfgwarn.dat', list3)
        self.warn_change('D:/new_jyplug/T0002/col_cfgwarn.dat', list4)
        
        '''
        #fht = open(fileNameHt, 'r', encoding='UTF-8')
        fht = open(fileNameHt, 'r')
        lines = fht.readlines()
        num = len(lines)
        fht.close()
        
        group = (int)(num / 4)
        mark = lines[1:group]
        tip = lines[(group+1):2*group]
        tipword = lines[(2*group+1):3*group]
        time = lines[(3*group+1):4*group] 
        
        list = []
        for i in range(len(lists)):
            code = lists[i][0]
            if('6' == code[0]):
                list.append('01' + code + '=')
            else:
                list.append('00' + code + '=')
        
        for i in range(len(list)):
            for j in range(len(mark)):        
                code = mark[j][0:9]
                if(list[i] == code):
                    mark.pop(j)
                    break
        for i in range(len(list)):
            for j in range(len(tip)):        
                code = tip[j][0:9]
                if(list[i] == code):
                    tip.pop(j)
                    break            
        for i in range(len(list)):
            for j in range(len(tipword)):        
                code = tipword[j][0:9]
                if(list[i] == code):
                    tipword.pop(j)
                    break
        for i in range(len(list)):
            for j in range(len(time)):        
                code = time[j][0:9]
                if(list[i] == code):
                    time.pop(j)
                    break
        
        fht = open(fileNameHt, "w")            
        fht.write('[MARK]\n')
        for i in range(len(list)):
            fht.write(list[i] + '7\n')
        for i in range(len(mark)):
            fht.write(mark[i])
        fht.write('[TIP]\n')
        for i in range(len(list)):
            continueDay = lists[i][5]
            fht.write(list[i] + continueDay + '\n')
        for i in range(len(tip)):
            fht.write(tip[i])
        fht.write('[TIPWORD]\n')
        for i in range(len(lists)):
            limitReason = lists[i][12]
            fht.write(list[i] + limitReason + '\n')
        for i in range(len(tipword)):
            fht.write(tipword[i])
        fht.write('[TIME]\n')
        for i in range(len(list)):
            firstLimitTime = lists[i][6]
            fTIme = str(int(firstLimitTime.replace(':', ''), 10))
            fht.write(list[i] + fTIme + '\n')
        for i in range(len(time)):
            fht.write(time[i])
        fht.close()
        '''
        
        
        '''
        fht = open(fileNameHt, 'rb')
        read_buf = fht.read(868)
        fht.close()
        fht = open(fileNameHt, "wb")
        #a = struct.pack('B', int(read_buf))
        fht.write(read_buf)
        a = struct.pack('L', int(len(list)))
        fht.write(a)
        for i in range(len(list)):
            for x in range(4):
                a = struct.pack('B', 0)
                fht.write(a)
            fht.write(str.encode(list[i][2:8]))
            for x in range(17):
                a = struct.pack('B', 0)
                fht.write(a)
            a = struct.pack('B', 1)
            fht.write(a)
            for x in range(33):
                a = struct.pack('B', 0)
                fht.write(a)
                
        fht.close()        
        '''
        
        '''    
        for i in range(len(lists)):
            code = lists[i][0]
            if('6' == code[0]):
                fht.write('01')
            else:
                fht.write('00')
            fht.write(code + '=7\n')
        fht.write('[TIP]\n')
        for i in range(len(lists)):
            code = lists[i][0]
            if('6' == code[0]):
                fht.write('01')
            else:
                fht.write('00')
            fht.write(code + '=\n')
        fht.write('[TIPWORD]\n')
        for i in range(len(lists)):
            code = lists[i][0]
            if('6' == code[0]):
                fht.write('01')
            else:
                fht.write('00')
            limitReason = lists[i][12]
            fht.write(code + '=' + limitReason + '\n')
        fht.write('[TIME]\n')
        for i in range(len(lists)):
            code = lists[i][0]
            if('6' == code[0]):
                fht.write('01')
            else:
                fht.write('00')
            limitReason = lists[i][12]
            fht.write(code + '=0\n')
        '''
        
        #fht.close()
    
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
        
        if (len(lists) > 10):
            
            mongoData = dict(item)
            self.client.insert(mongoData)
            
            # sort as limitVsCirculate
            #lists.sort(key = lambda x:(float(x[10])), reverse = True)            
            lists.sort(key = lambda x:(float(x[10])), reverse = True)
            lists.sort(key = lambda x:(int(x[7].replace(':', ''), 10)), reverse = False)
            lists.sort(key = lambda x:(float(x[5])), reverse = True)
            
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
        
        