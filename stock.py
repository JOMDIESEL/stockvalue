from bs4 import BeautifulSoup as soup
#ใช้ในการreq ข้อมูล ไม่ต้องเปิดweb site แต่อยากได้ข้อมูลมา โดยไม่ต้องเปิดbrowser
from urllib.request import urlopen as req
def checkprice(CODE):
	#สร้งfomat ใส่อะไรก็ได้
	url = 'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol={}&ssoPageId=10&selectPage=2'.format(CODE)
	webopen = req(url)
	#กำหนดpage_html = webopen.read เพื่ออ่านค่า
	page_html = webopen.read()
	webopen.close()

	data = soup(page_html,'html.parser')
		#findAll ไว้ค้นหา
	price = data.findAll('div',{'class':'col-xs-6'})
	#อัพเดตด้านหล่าง
	updatedata = data.findAll('span',{'class':'stt-remark'})


	print('count',len(price))
	print(price[0].text,price[1].text,price[2].text)


	title = price[0].text
	title = title.replace(' ','')


	stock_price = price[2].text
	#แปลงทศนิยม
	stock_price = float(stock_price)

	change = price[3].text
	#ตัดช่องว่าง
	change = change.replace('\n','')
	change = change.replace('\r','')
	change = change.replace('\t','')
	change = change.replace(' ','')
	#ตัด"" ออก
	change = float(change[11:])



	percentage = price[4].text
	percentage = percentage.replace('\n','')
	percentage = percentage.replace('\r','')
	percentage = percentage.replace(' ','')
	percentage = float(percentage[12:-1])

	update =  updatedata[0].text

	print([title,stock_price,change,percentage,update])



#checkprice('ITD')
print(help(soup))