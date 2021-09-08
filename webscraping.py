import requests
from bs4 import BeautifulSoup
import pprint
import time

#res = requests.get('https://news.ycombinator.com/news')
#soup = BeautifulSoup(res.text , 'html.parser')


#links = soup.select('.storylink')
#subtext = soup.select('.subtext')

#SORTING ALGORITHM
def sort_by_votes(hlist):
    return sorted(hlist , key=lambda k:k['Votes'] , reverse=True)


def custom_hnews(links,subtext):
    hnews= []
    for indx,item  in enumerate(links):
        #print(indx,item)
        tittle = item.getText()  
        href = item.get('href', None)  
        votes = subtext[indx].select('.score')  #All links w votes
        if len(votes):
            points = int(votes[0].getText().replace(' points',''))   #shows just the number
            if points > 100:
                hnews.append({'Tittle': tittle , 'Link': href , 'Votes': points})
    return sort_by_votes(hnews)

#print('****MAIN PAGE****')

#pprint.pprint(custom_hnews(links,subtext))

Other_page= input('What page do u want to scrape, type the number or MP for multiple pages')

if Other_page == 'mp' or Other_page=='MP':
    while True:
        try:
            mpages=int(input('How many pages do u wanna print?')) +1
            for item in range(1,mpages):
                res0 = requests.get(f'https://news.ycombinator.com/news?p={item}')
                soup0 = BeautifulSoup(res0.text , 'html.parser')
                links0 = soup0.select('.storylink')
                subtext0 = soup0.select('.subtext')
                print('\n\n')
                print(f'****PAGE NUMBER: {item}****')
                pprint.pprint(custom_hnews(links0,subtext0))
                time.sleep(30)
        except:
            print('please enter a number')
        else:
            break
        
                
else:
    try:
        Other_page==int(Other_page)
        res1 = requests.get(f'https://news.ycombinator.com/news?p={Other_page}')
        soup1 = BeautifulSoup(res1.text , 'html.parser')

        links1 = soup1.select('.storylink')
        subtext1 = soup1.select('.subtext')
        print('\n\n')
        print(f'****PAGE NUMBER: {Other_page}****')
        pprint.pprint(custom_hnews(links1,subtext1))
    except:
        print('please enter a number or mp')