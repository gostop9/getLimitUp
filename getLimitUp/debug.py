#!/usr/bin/python
'''
import requests

headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'cid=nskbfvr9pc29m4mjtsdeit4jf31510283024; ComputerID=nskbfvr9pc29m4mjtsdeit4jf31510283024; guideState=1; other_uid=Ths_iwencai_Xuangu_b9b3a6b974ef2a54915c94512d5b3719; PHPSESSID=4cf5e5ab98be906203372c16ab5a17de; v=AlTVo_lY8xjlpGdUEaCtTgtMJZnDrXjcutEM2-404F9i2fqNFr1IJwrh3G09',
    'Host':'www.iwencai.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
params={
    'w':'机构动向，股性评分，大单买入比大于大单卖出比，主动买入比大于主动卖出比',
    'tid':'stockpick',
    'qs':'stockpick_h',
    'querytype':'stock',
}
def scrapy():
    reps= requests.get('http://www.iwencai.com/stockpick/search?w=%E6%9C%BA%E6%9E%84%E5%8A%A8%E5%90%91%EF%BC%8C%E8%82%A1%E6%80%A7%E8%AF%84%E5%88%86%EF%BC%8C%E5%A4%A7%E5%8D%95%E4%B9%B0%E5%85%A5%E6%AF%94%E5%A4%A7%E4%BA%8E%E5%A4%A7%E5%8D%95%E5%8D%96%E5%87%BA%E6%AF%94%EF%BC%8C%E4%B8%BB%E5%8A%A8%E4%B9%B0%E5%85%A5%E6%AF%94%E5%A4%A7%E4%BA%8E%E4%B8%BB%E5%8A%A8%E5%8D%96%E5%87%BA%E6%AF%94&tid=stockpick&qs=stockpick_h&querytype=stock',headers=headers)
    reps.encoding = 'utf-8'
    return reps.text

if __name__=='__main__':
    scrapy()
'''
from scrapy.cmdline import execute
execute()