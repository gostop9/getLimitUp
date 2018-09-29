# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetlimitupItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    code = scrapy.Field()    
    name = scrapy.Field()
    
    liangBi = scrapy.Field()
    ziYouHuanShouLv = scrapy.Field()
    ziYouLiuTongShiZhi = scrapy.Field()
    continueDay = scrapy.Field()
    firstLimitTime = scrapy.Field()
    lastLimitTime = scrapy.Field()
    limitOpenCount = scrapy.Field()
    limitVsDeal = scrapy.Field()
    limitVsCirculate = scrapy.Field()
    limitUpMoney = scrapy.Field()
    limitReason = scrapy.Field()
    guXingPingFen = scrapy.Field()
    limitShareNumber = scrapy.Field()
    startPrice = scrapy.Field()
    endPrice = scrapy.Field()
    maxPrice = scrapy.Field()
    minPrice = scrapy.Field()
    zhenFu = scrapy.Field()
    chengJiaoE = scrapy.Field()
    chengJiaoLiang = scrapy.Field()
    huanShouLv = scrapy.Field()
    ziYouLiuTongGu = scrapy.Field()
    liuTongGu = scrapy.Field()
    liuTongShiZhi = scrapy.Field()
    ipoDays = scrapy.Field()
    zongGuBen = scrapy.Field()
    hangYe = scrapy.Field()
    
    minLen = scrapy.Field()
    dateYMD = scrapy.Field()
    otherItem = scrapy.Field()
    
    pass
