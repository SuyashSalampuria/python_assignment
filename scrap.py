import requests
from bs4 import BeautifulSoup
from Person import Person
uname6=[]
names6=[]
works6=[]
citys6=[]
favou6=[]
def scrap(username,nams,citys,works,favs,foun):
    nams=None
    citys=None
    works=[]
    favs=[]
    favs2={}
    foun=False
    for x in uname6:
        if(x==username):
            foun=True
            break
    if(foun==True):
            index=uname6.index(username)
            nams=names6[index]
            citys=citys6[index]
            works=works6[index]
            favs=favou6[index]
            for x in favs:
                print(x)
    else:
        page = requests.get('https://en-gb.facebook.com/{}'.format(username))
        soup = BeautifulSoup(page.text, 'html.parser')
        city=soup.find(id='current_city')
        city1=city.find(class_='_2iel _50f7')
        city2 = city1.find_all('a')
        if(city2):
            for x in city2:
                citys=x.string    
  
        namea = soup.find(class_='_2nlw _2nlv')
        for x in namea:
            nams=x
        work1=soup.find(class_='_4qm1')   
        wo=work1.find(class_='_h72 lfloat _ohe _50f7')
        if(wo.string=='Work'):

            worka = work1.find_all(class_='_2lzr _50f5 _50f7')
            for x in worka:
                works.append(x.string)
        else:
            raise Exception('No work found')
        favo11 = soup.find('div', {'id': 'favorites'})
        if(favo11):
            favo12 = favo11.find_all('tbody')

            for x in favo12:

                label1=x.find(class_='label')
                lab=label1.string
                if(lab=='Other'):
                    dat=[]
                    data1=x.find(class_='data')
                    da=data1.find_all('a')
                    for z in da:
                        dat.append(z.string)
                    favs2[lab]=dat
                else:
                    for y in label1:

                        data1=x.find(class_='data')
                        da=data1.find('a')
                        dat=da.string
                        favs2[lab]=dat
        if(len(favs2)>0):
            print(favs2)
        else:
            print("no faourites")
        
        
        
        
        # favo = soup.find('div', {'id': 'pagelet_all_favorites'})
        # if (favo) :
        #     favo2 =favo.find_all('a')
        #     for x in favo2:
        #         if(x.string==None):
        #             continue
        #         print(x.string)
        #         favs.append(x.string)
        # else:
        #     print("There are no favourites")
        uname6.append(username)
        names6.append(nams)
        citys6.append(citys)
        works6.append(works)
        favou6.append(favs2)
    if(len(works)!=0 and citys!=""):
        p1=Person(name=nams,work=works,city=citys)
    elif(len(works)!=0 and citys==""):
        p1=Person(nams,works,city="Roorkee")
    elif (len(works)==0 and citys!=""):
        p1=Person(name=nams,city=citys)
    else:
        p1=Person(nams)
    p1.show()
    this_list=[nams,citys,works,favs2]
    return this_list
