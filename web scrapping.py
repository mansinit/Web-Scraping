'''import urllib.request

wiki="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
#wiki="https://twitter.com/search?q=%23KashmirWelcomesChange&src=trend_click"
page=urllib.request.urlopen(wiki)

from bs4 import BeautifulSoup
soup=BeautifulSoup(page)

print(soup.prettify())
print(soup.title.string)

all_links=soup.findAll("a")
for x in all_links:
    print(x.get("href"))
print('..........................................................................')
all_table=soup.findAll('table')
#print(all_table)

right_table=soup.find('table',class_="wikitable sortable plainrowheaders")

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in right_table.findAll("tr"):
    cell=row.findAll("td")
    state=row.findAll("th")
    if(len(cell)==6):
        A.append(cell[0].find(text=True))
        B.append(state[0].find(text=True))
        C.append(cell[1].find(text=True))
        D.append(cell[2].find(text=True))
        E.append(cell[3].find(text=True))
        F.append(cell[4].find(text=True))
        G.append(cell[5].find(text=True))

import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_capital']=C
df['Legislative Capital']=D
df['Judicial Capital']=E
df['Year of Establishment']=F
df['Former Capital']=G
print(df)

'''

import urllib.request

wiki="https://www.theguardian.com/football/premierleague/table"
page=urllib.request.urlopen(wiki)

from bs4 import BeautifulSoup
soup=BeautifulSoup(page)

#print(soup.prettify())

right_table=soup.find('table',class_="table table--football table--league-table table--responsive-font table--striped")
#print(right_table)

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]
J=[]
K=[]
L=[]
for row in right_table.findAll("tr"):
    cell=row.findAll("td")
    spam=row.findAll("a")
    #print(spam[0].find(text=True))
    if(len(cell)==11):
        A.append(cell[0].find(text=True))
        B.append(spam[0].find(text=True))
        C.append(cell[1].find(text=True))
        D.append(cell[2].find(text=True))
        E.append(cell[3].find(text=True))
        F.append(cell[4].find(text=True))
        G.append(cell[5].find(text=True))
        H.append(cell[6].find(text=True))
        I.append(cell[7].find(text=True))
        J.append(cell[8].find(text=True))
        #K.append(cell[9].find(text=True))
        #L.append(cell[10].find(text=True))
import pandas as pd
df=pd.DataFrame(A,columns=['P'])
df['team']=B
df['GP']=C
df['W']=D
df['D']=E
df['L']=F
df['F']=G
df['A']=H
df['GD']=I
df['Pts']=J
#df['Form']=K
print(df)