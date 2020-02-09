# -*- coding: utf-8 -*-
import scrapy
import time
import datetime
from getLimitUp.items import GetlimitupItem

def attrStrCmp(s):
    if (s == '量比'):
        return 'liangBi'
    if (s == '实际换手率(%)'):
        return 'ziYouHuanShouLv'
    if (s == '自由流通市值(元)'):
        return 'ziYouLiuTongShiZhi'
    if (s == '连续涨停天数(天)'):
        return 'continueDay'
    if (s == '首次涨停时间'):
        return 'firstLimitTime'
    if (s == '最终涨停时间'):
        return 'lastLimitTime'
    if (s == '涨停开板次数(次)'):
        return 'limitOpenCount'
    if (s == '涨停封成比(%)'):
        return 'limitVsDeal'
    if (s == '涨停封流比(%)'):
        return 'limitVsCirculate'
    if (s == '涨停封单额(元)'):
        return 'limitUpMoney'
    if (s == '涨停原因类别'):
        return 'limitReason'
    if (s == '股性评分'):
        return 'guXingPingFen'
    if (s == '涨停封单量(股)'):
        return 'limitShareNumber'
    if (s == '开盘价:前复权(元)'):
        return 'startPrice'
    if (s == '收盘价:前复权(元)'):
        return 'endPrice'
    if (s == '最高价:前复权(元)'):
        return 'maxPrice'
    if (s == '最低价:前复权(元)'):
        return 'minPrice'
    if (s == '振幅(%)'):
        return 'zhenFu'
    if (s == '成交额(元)'):
        return 'chengJiaoE'
    if (s == '成交量(股)'):
        return 'chengJiaoLiang'
    if (s == '换手率(%)'):
        return 'huanShouLv'
    if (s == '自由流通股(股)'):
        return 'ziYouLiuTongGu'
    if (s == '流通a股(股)'):
        return 'liuTongGu'
    if s.find(u'a股流通市值') != -1:
        return 'liuTongShiZhi'
    if (s == '上市天数(天)'):
        return 'ipoDays'
    if (s == '总股本(股)'):
        return 'zongGuBen'
    if (s == '所属同花顺行业'):
        return 'hangYe'
    else:    
        return 'otherItem'

class GetsharelimitupSpider(scrapy.Spider):
    name = 'getShareLimitUp'
    allowed_domains = ['www.iwencai.com']
    start_urls = ['http://www.iwencai.com/stockpick/search']
    
    headers={
        'Accept':'pplication/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        #'Cookie':'cid=nskbfvr9pc29m4mjtsdeit4jf31510283024; ComputerID=nskbfvr9pc29m4mjtsdeit4jf31510283024; guideState=1; other_uid=Ths_iwencai_Xuangu_b9b3a6b974ef2a54915c94512d5b3719; PHPSESSID=4cf5e5ab98be906203372c16ab5a17de; v=AlTVo_lY8xjlpGdUEaCtTgtMJZnDrXjcutEM2-404F9i2fqNFr1IJwrh3G09',
        'Host':'www.iwencai.com',
        #'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
        'hexin-v':'AlzdSzEAblIXdxoOzpZZJSTMLXEN1QB4gnoUwzZdaMcqgfKnXuXQj9KJ5FmF'
    }
    formatStr = "今日涨停，成交额，量比，换手率，振幅，流通股，自由流通股，自由流通市值，收盘价前复权，股性评分，连续涨停天数，涨停开板次数，涨停封成比，涨停封流比，涨停封单额，涨停原因类别，涨停封单量，成交量，实际换手率，首次涨停时间，最终涨停时间，开盘价前复权，收盘价前复权，最高价前复权，最低价前复权，流通市值，上市天数，总股本，所属同花顺行业"
    querystring = {
        'w':formatStr,
        'tid':'stockpick',
        'qs':'stockpick_h',
        'querytype':'stock',
        'p':'1',
        'perpage':'400',
        'changeperpage':'1'
    }
    cookies = {
        'cid':'nskbfvr9pc29m4mjtsdeit4jf31510283024',
        'ComputerID':'nskbfvr9pc29m4mjtsdeit4jf31510283024',
        'guideState':'1',
        'other_uid':'Ths_iwencai_Xuangu_b9b3a6b974ef2a54915c94512d5b3719',
        'user':'MDptb18yNTI0MjY2MjM6Ok5vbmU6NTAwOjI2MjQyNjYyMzo1LDEsNDA7NiwxLDQwOzcsMTExMTExMTExMTEwLDQwOzgsMTExMTAxMTEwMDAwMTExMTEwMDEwMDEwMDEwLDQwOzMzLDAwMDEwMDAwMDAwMCwyODE7MzYsMTAwMTExMTEwMDAwMTEwMDEwMTExMTExLDI4MTs0NiwwMDAwMTEwMDEwMDAwMDExMTExMTExMTEsMjgxOzUxLDExMDAwMDAwMDAwMDAwMDAsMjgxOzU4LDAwMDAwMDAwMDAwMDAwMDAxLDI4MTs3OCwxLDI4MTs4NywwMDAwMDAwMDAwMDAwMDAwMDAwMTAwMDAsMjgxOzQ0LDExLDQwOzEsMSw0MDsyLDEsNDA7MywxLDQwOjI0Ojo6MjUyNDI2NjIzOjE1NDM1NDkxOTQ6OjoxNDMyNDYwODIwOjQwMDgwNjowOjFlOTNmZDFjNzkwZjY0ODlhNmI4YmY5MTY2M2IyODZkYjpkZWZhdWx0XzI6MQ%3D%3D',
        'userid':'252426623',
        'u_name':'mo_252426623',
        'escapename':'mo_252426623',
        'ticket':'7197fceb268431d3bad66ce1704b645b',
        'PHPSESSID':'bbc2ece0356a87571a88028db40d6ba1',
        'v':'ApsaDnplQyiynb_cUV2ohLuDKvQGcK0gqYhzJo38dxqxbLXiFUA_wrlUA16e'
    }
    
    def start_requests(self):
        for url in self.start_urls:            
            yield scrapy.FormRequest(
                url=url, 
                headers=self.headers, 
                cookies=self.cookies,
                method = 'GET',
                meta={},
                formdata=self.querystring, 
                callback=self.parse,
                errback = self.error,
                dont_filter = True
            )

    def parse(self, response):
        item = GetlimitupItem()
        nodeList = response.xpath('//*[@id="tableWrap"]/div[2]/div/div[1]/div/div/div[1]/ul/li')
        
        stringTime = str(self.formatStr[0:8])
        if stringTime.find('今日') != -1:
            now = datetime.datetime.now()
            stringTime = now.strftime('%Y%m%d')
        item['dateYMD'] = stringTime
        #item['dateYMD'] = str(self.formatStr[0:8])
        
        item['minLen'] = 10000
        item['code'] = response.xpath('//div[@id="tableWrap"]/div[2]/div/div[2]/div/table/tbody/tr[*]/td[3]/div/text()').extract()
        item['name'] = response.xpath('//div[@id="tableWrap"]/div[2]/div/div[2]/div/table/tbody/tr[*]/td[4]/div/a/text()').extract()
        
        col = 1
        for node in nodeList:
            colNum = 0
            if(len(node.xpath('./dl'))): #如果是分列的
                colNum = len(node.xpath('./dl/dd')) - 1
                if(len(node.xpath('./dl/dt/div/span'))):
                    attr = node.xpath('./dl/dt/div/span[1]/text()').extract()[0]
                else:
                    attr = node.xpath('./dl/dt/div/text()').extract()[0]
            else:
                if(len(node.xpath('./div[1]/span'))): #有解释
                    attr = node.xpath('./div[1]/span[1]/text()').extract()[0]
                else:
                    attr = node.xpath('./div[1]/text()').extract()[0]
            
            string = attrStrCmp(attr)
            if(string == 'otherItem'):
                col = col + 1 + colNum
                continue

            text = '//div[@class="scroll_tbody_con"]/table/tbody/tr[*]/td[{:d}]/div/'.format(col)

            if ((string == 'firstLimitTime') or (string == 'lastLimitTime')):
                s1 = response.xpath(text+'span[1]/text()').extract()
                s2 = response.xpath(text+'span[2]/text()').extract()
                s3 = response.xpath(text+'span[3]/text()').extract()
                s4 = response.xpath(text+'span[4]/text()').extract()
                s5 = response.xpath(text+'span[5]/text()').extract()
                s6 = response.xpath(text+'span[6]/text()').extract()
                times = []
                for i in range(len(s1)):
                    tiem = s1[i]+s2[i]+':'+s3[i]+s4[i]+':'+s5[i]+s6[i]
                    times.append(tiem)
                item[string] = times
            else:
                item[string] = response.xpath(text+'a/text()' + '|' + text+'text()' + '|' + text+'span[1]/text()' + '|' + text+'/text()').extract()
            col = col + 1 + colNum

            item['minLen'] = min(item['minLen'], len(item[string]))
        
        yield item
    
    
    def error(self, response):
        print ('spider error!\n')
        pass