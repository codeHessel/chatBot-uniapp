import json
import random
import time
import traceback
from requests_html import HTMLSession

out_path = r'/var/www/github-push/uniapp-server/server/log.txt'

TX_API_ROOT = r'http://api.tianapi.com'

session = HTMLSession()


class AutoCommit:
    def __init__(self, type='1'):
        self.type = type

    def start(self):
        User_Agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        url = "https://github.com/explore"
        try:
            res = session.get(url,headers={'User-Agent':random.choice(User_Agent)},verify=False)
            time.sleep(2)
            phtml = res.html.find('div.col-md-8.col-lg-6.py-4', first=True)
            chtml_li = phtml.find('h3.f3')
            timenow = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
            f = open(out_path,"a", encoding='utf-8')
            for li in chtml_li:
                url_li = li.find('a')
                con = ''
                for sub in url_li:
                    con = con + r'/' + sub.text
                f.write(con + '\n')
            f.write(timenow+ '\n')
            f.close()
        except Exception as e:
            traceback.print_exc()



setUrl = AutoCommit(1)
setUrl.start()
