# import urllib.request
# from bs4 import BeautifulSoup
#
# fp = urllib.request.urlopen('chapter1.html')
# source = fp.read()
#
# soup = BeautifulSoup(source)
#
# print(soup)


from bs4 import BeautifulSoup


file = open("chapter1.html","r")
lines = file.readlines()

for line in lines:

    soup = BeautifulSoup(line,'lxml')
    text=soup.text
    if text != '\n' and text != '':
        print(soup.text)
