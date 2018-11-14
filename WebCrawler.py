from bs4 import BeautifulSoup

myHtml=''''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>This is my title</title>
</head>
<body>
<h1>This is H1, love you</h1>
<h1>這是另一個H1 tag</h1>
<h2>This is H2, 小一點的字體</h2>
<p>this is Joe, I love you guys.  yes!!!!</p>
</body>
</html>'''


soup=BeautifulSoup(myHtml,'html.parser')

#myH1=soup.find('h1')
myH1=soup.findAll('h1')

for i in myH1:
    if '這是' in i.string:
        print(i.string)
#print(myH1)
#print(myH1.string)