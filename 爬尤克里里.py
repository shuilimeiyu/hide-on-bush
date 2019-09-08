'''
Created on 2019-6-5

@author: Administrator
'''
import random
import requests 
import urllib
import re

for i in range(1,94):
    req = requests.get("http://www.ukulelefan.com/solo/page/{}/".format(i)).text
    results = re.findall('<h2 class="list-title"><a href="(.*?)" rel="bookmark">(.*?)</a></h2>',req,re.S)
    for result in results :
        (url,name)=result
        newname = re.sub(r'[\/:*?"<> •|]', "", name)
        req = requests.get(url).text
        results1 = re.findall('<img class="alignnone size-full wp-image-.*?" (data-original|src)="(.*?).jpg"',req,re.S)
        for result in results1 :
            (laji,url1)=result
            url1=url1+".jpg"
            try :
                a=int(random.randint(0,20))
                print(a)
                urllib.request.urlretrieve(url1,"D:/youkell/{0}{1} .jpg".format(newname,str(a)))
                break
            except:
                 print(url+"   "+name+"  出错在第   "+str(i)+" 页")
               
