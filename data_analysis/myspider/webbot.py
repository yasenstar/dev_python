from bs4 import BeautifulSoup
import mechanize
import time
import urllib
import string

start = input("Where would you like to start searching?\n")
br = mechanize.Browser()
r = br.open(start)
# html = r.read()
html = "http://www.pbc.gov.cn/zhengwugongkai/127924/128041/2951606/1923625/1923629/d6d180ae/index4.html"

soup = BeautifulSoup(html)
for link in soup.find_all('a'):
    print (link.get('href'))
