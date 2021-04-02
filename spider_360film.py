# 爬360影视所有电影的图片加名称
from urllib import request
from bs4 import BeautifulSoup
print("剧名                演员")
for page in range(1,23):
    url="https://www.360kan.com/dianying/list.php?cat=103&pageno=%d"%page
    headder={'User-Agent':'User-Agent: Mozilla/5.0 (Linux; X11)','Accept':'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8' }
    req=request.Request(url)
    req.add_header('User-Agent','User-Agent: Mozilla/5.0 (Linux; X11)')
    with request.urlopen(req) as f:
        soup=BeautifulSoup(f.read(),"html.parser")
        film=soup.find_all('a', class_='js-tongjic')
        for i in film:
            print(i.find('span',class_='s1').text,"---------",i.find('p',class_='star').text)
            print(i.find('img')['src'])
            with open("d://360filmpa/%s.jpg"%(i.find('span',class_='s1').text),'wb+') as f:
                f.write(request.urlopen(i.find('img')['src']).read())
