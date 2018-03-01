import requests, bs4, sqlite3

url = 'http://3dtoday.ru/blogs/news3dtoday/' # url для второй страницы
r = requests.get(url)
b = bs4.BeautifulSoup(r.text, "html.parser")
#p1 = b.findAll(attrs={"class" : "title_bg"}).findNext(a)
g = open('text.txt','w')
conn = sqlite3.connect('FirstBD.db')
cursor = conn.cursor()
for row in b.findAll(attrs={"class" : "title_bg"}):
		cols = row.findAll('a')[0]["href"]
		url2 = "http://3dtoday.ru" + cols
		f = requests.get(url2)
		v = bs4.BeautifulSoup(f.text, "html.parser")
		p3 = v.findAll(attrs={"class" : "blog_post_body"})
		p4 = p3[0].text
		p4 = p4[0:-190]
		p3 = v.findAll('h1')
		p5 = p3[0].getText()
		print(p5)
		print(" ")
		print(p4)
		print(" ")
		print(" ")
		cursor.execute("INSERT INTO Main (NameNews, TextNews) VALUES(?, ?)", (p5, p4))
		conn.commit()
g.close
conn.close()		
#p2 = p1[0]["class"]
#for element in p1:
	#print(element.attrs["href"])
#s = p1[0].getText()
# p1 = b.select('.post_list .post_list_item .post_list_item_title .title_bg')
# testText = p1[0].getText()
#print (p1.findNext('a'))
# print("Тестовый текст таков: " + testText)