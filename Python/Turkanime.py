# -*- coding: cp1254 -*-
import urllib2,os,urllib

folroot="./Animeler/"
anime="Naruto Shippuuden"
root="http://www.turkanime.tv/"

bolumlist_url="http://www.turkanime.tv/icerik/bolumler&ID=76"
bolumlist=[]

def create_folder_and_write_file(bol_string,link_string):
    if not os.path.exists(folroot+anime): os.makedirs(folroot+anime)
    bol_string=bol_string.replace("-", " ").replace("Bolum", "Bölüm")
    open(folroot+anime+"/"+bol_string,"wb").write(link_string)
    
def get_bolumlist():
    bolumlist_read=urllib2.urlopen(bolumlist_url).read()
    bolumlist_read=bolumlist_read.split('<div id="bolumlist">')[1].split("</div>")[0]
    for a in bolumlist_read.split('<a href="'):
        b=a.split('" class="btn"')[0]
        bolumlist.append(b)
    bolumlist.remove("")
    
def get_vklink(link):
 
    vk_links={}
    kalite=["720","480","360","240"]
    vklink_read=urllib2.urlopen(root+link).read()
    a=vklink_read.split("""','#video');"><i class="icon-play"></i> VK</a>""")
    if len(a)==3:
        pass
    else:
        print root+link
        a=a[0]
        b=a.split("&video=")[-1]
        
        code=str(b)
        fansub=a.split("&fansub=")[1].split("&")[0].replace("Ä±", "ı")
        lnk=root+link+"&fansub="+fansub+"&giris=&video="+code
        
        vklink_read=urllib.urlopen(lnk).read()
        #print vklink_read
        print lnk
        vklink_rad=urllib.urlopen(lnk).read()
        #open("a.html", "w").write(vklink_rad)
        #print vklink_rad
        #print lnk
        try:
            vk_url=vklink_read.split('</i></a><iframe src="')[1].split('" width="')[0]
        except:
           
            vk_url=vklink_read.split('http://vk.com/video_ext.php')#.split('" width="')[0]
        
        vklink_read=urllib2.urlopen(vk_url).read()
        for x in kalite:
            sp=vklink_read.split('url'+x+'":"')
            if len(sp)!=1:
                vklink_mp4=sp[1].split('","')[0]
                vklink_mp4=vklink_mp4.replace("\\", "")
                print "-"*80
                print "-"*80
                print x
                print vklink_mp4

##        
##        link_stirng=vklink_mp4
##        bol_string=link.split("/")[1]
##        
##        create_folder_and_write_file(bol_string,link_stirng)
##        #vk_links[k]=vklink_mp4

get_bolumlist()

get_vklink(bolumlist[0])
