import httpx,os,re

class TurkAnime:
    
    url="http://www.turkanime.tv/"
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
    def anime_ara(self,ara):
        
        data = {
        'arama': ara
        }
        veri=httpx.post(self.url+"/arama", headers=self.headers, cookies=self.cookies, data=data).content.decode("utf8")
        liste=[]
        r=re.findall('<div class="panel-ust-ic"><div class="panel-title"><a href="\/\/www\.turkanime\.tv\/anime\/(.*?)" (.*?)>(.*?)<\/a>',veri)
        for slug,_,title in r:
            liste.append([title,slug])
        return liste
    def bolumler(self,slug):
        veri=httpx.get(self.url+"/anime/"+slug, headers=self.headers, cookies=self.cookies).content.decode("utf8")
        h=self.headers.copy()
        h.update({"X-Requested-With":"XMLHttpRequest","Accept":"*/*"})
        animeId=veri.split("ajax/bolumler&animeId=")[1].split('"')[0]
        liste=[]
        a=httpx.get(f"http://www.turkanime.tv/ajax/bolumler&animeId={animeId}",headers=h,cookies=self.cookies).content.decode("utf8")
        r=re.findall('<a href="\/\/www\.turkanime\.tv\/video\/(.*?)" (.*?)><span class="bolumAdi">(.*?)<\/span><\/a>',a)
        for slug,_,title in r:
            liste.append([title,slug])
        return liste
    def deneme(self):
        h=self.headers.copy()
        h.update({"X-Requested-With":"XMLHttpRequest","Accept":"*/*"})
        url="http://www.turkanime.tv/ajax/videosec&b=tmti2rx5zQSA6qfdEHN9qKDtjK9ofy4lapT2SxY9l6c&v=0ommhLpH_LSEiQPqizi1_blqmdNCkrdzkDbbUs5ftEo&f=kvLxEP-QJkVNREiSNmb9iX397m9OqncJvJcxKlt1NGg"
        a=httpx.get(url,headers=h,cookies=self.cookies).content.decode("utf8")
        a=httpx.get("http://www.turkanime.tv/iframe?url=Sk3SXAueRmkPY_ghJ9h0kv-utaoKPi4lKnaUvyh2S40DY3JOMHfyTRcil1NK6lXPKaM38Ah0oJy3sZYl_lhMAkk2EOpkUxbfIbWXRw_dBcXizkJGj5pIaChARkz5NPZq884i7Cq-mwwWjvkOoIqUvkoTQhC_JAC9wPaRt6d79cuQVWPYIvLGaWlwC38cqMy2YyakI3pu0NGd-y7a7ODkjzzNlWqKjzhzRN0QLHRQRlCyteI0TmrJTxebjbTjVNdN",headers=h,cookies=self.cookies).content.decode("utf8")
        print(a)
if __name__=="__main__":
    t=TurkAnime()
    anime=t.anime_ara("Naruto")[0]#Aramadaki ilk sonuç
    
    #print(t.bolumler(anime[1]))
    t.deneme()
