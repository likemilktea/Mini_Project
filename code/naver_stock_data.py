from bs4 import BeautifulSoup
from urllib.request import urlopen
stock_names=[] # 상한가 타이틀
stock_values=[] # 상한가 값
stock_lower_names=[] # 하한가 타이틀
stock_lower_values=[] # 하한가 값

url = "https://finance.naver.com/sise/"
page = urlopen(url)

soup = BeautifulSoup(page, 'html.parser') # html.parser로 url페이지 오픈
stock_table=soup.find('table',summary="탑종목 상한가 리스트") # table 중에 summary가 "탑종목 상한가 리스트"인 부분 할당
stock_rows=stock_table.find_all('a') # 모든 a태그 할당
for i in stock_rows: # 상한가 타이틀 할당
    stock_names.append(i.text)

value_rows_etc=stock_table.find_all('td', class_="number") # td 태그에서 class_="number"만 할당
value_rows=[value_rows_etc[i] for i in range(len(value_rows_etc)) if i%9==2 ] # 9개의 값 중 2번째 값만 할당 반복
for i in value_rows: # 상한가 값 할당
    stock_values.append(i.text)

stock_lower_table=soup.find('table',summary="탑종목 하한가 리스트") # table 중에 summary가 "탑종목 하한가 리스트"인 부분 할당
stock_lower_rows=stock_lower_table.find_all('a') # 모든 a태그 할당
for i in stock_lower_rows: # 하한가 타이틀 할당
    stock_lower_names.append(i.text)

value_lower_rows_etc=stock_lower_table.find_all('td', class_="number") # td 태그에서 class_="number"만 할당
value_lower_rows=[value_lower_rows_etc[i] for i in range(len(value_lower_rows_etc)) if i%9==2 ] # 9개의 값 중 2번째 값만 할당 반복
for i in value_lower_rows: # 하한가 값 할당
    stock_lower_values.append(i.text)

print("==TOP상한가==")
for i,j in zip(stock_names,stock_values): # 상한가 타이틀 : 값 순으로 출력
    print(i,':',j)

print("==TOP하한가==")
for i,j in zip(stock_lower_names,stock_lower_values): # 하한가 타이틀 : 값 순으로 출력
    print(i,':',j)