import requests
from bs4 import BeautifulSoup as bs
import json
html = requests.get('https://www.iei.or.kr/intro/teacher.kh')

soup = bs(html.text,'html.parser')

th = soup.find('div',class_='intro_list')
one = th.select('li')
#print(one)

teacherList =[]

for i in one :
    img = i.find('img').attrs['src']
    name = i.find('p',attrs='intro_name').text
    tmp={}
    tmp['name'] = name
    tmp['img']=img
    #print(tmp)
    teacherList.append(tmp)

    #print(teacherList)
result={}
result['teacher'] =teacherList
#print(result)
result_joson = json.dumps(result,ensure_ascii=False)
print(result_joson)

with open('teacher.json','w',encoding='UTF-8')as myFile:
    myFile.write(result_joson)



