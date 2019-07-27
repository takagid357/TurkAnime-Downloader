import httpx,os,re

class TurkAnime:
    
    url="http://www.turkanime.tv/arama"
    cookies = {
        '__cfduid': 'deb9e04ac510c1b707412b1fd7daadec91564216182',
        'yew490': '1',
        '_ga': 'GA1.2.284686093.1564216182',
        '_gid': 'GA1.2.1256976049.1564216182',
        '__PPU_SESSION_1_1683592_false': '1564216202929|1|1564216202929|1|1',
        '_gat': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Alt-Used': 'www.turkanime.tv:443',
        'Connection': 'keep-alive',
        'Referer': 'http://www.turkanime.tv/',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers',
    }

 
    def __init__(self):
        pass
    def ara(self,ara):
        
        data = {
        'arama': ara
        }
        veri=httpx.post(self.url, headers=self.headers, cookies=self.cookies, data=data).content.decode("utf8")
        liste=[]
        r=re.findall('<div class="panel-ust-ic"><div class="panel-title"><a href="\/\/www\.turkanime\.tv\/anime\/(.*?)" (.*?)>(.*?)<\/a>',veri)
        for slug,_,title in r:
            liste.append([title,slug])
        return liste
if __name__=="__main__":
    t=TurkAnime()
    t.ara("naruto")
