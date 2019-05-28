import aiohttp
import asyncio
import re
from bs4 import BeautifulSoup

async def get_html(session, url):
    async with session.get(url, ssl=False) as res:
            
        return await res.text()
    
async def main(url):
    async with aiohttp.ClientSession() as session:
        html = await get_html(session, url)
        soup = BeautifulSoup(html,'html.parser')
        items = soup.findAll('div',attrs={'class':'m-review'})
        for i in items:
            stars = i.find('div',attrs={'class':'m-stars'})
            #m =stars.findAll('div',attrs={'class':'star  yellow'})
            p = stars.find_all('div')
           
            
            reviews = i.find('p',attrs={'class':'review-txt'}).text
            fian = (reviews.strip()).replace('\n','')
            fins = fian.split('\r')
            sep = ' '
            fin = sep.join(fins)    
    
            with open('project name here', 'a') as the_file:
                temp = fin[:1]
                k = ord(temp)
                if (k in range(97,123) or k in range(65,91) or k in range(48,58)):
                    
                    the_file.write(fin)
                    the_file.write('\n')
                    print('done')
                
            
            
            
urls=[]
for i in range(0,301,25):
    urls.append(f'https://sourceforge.net/projects/'project name here'/reviews/?offset={i}#reviews')
    
         
print(urls)

loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(*(main(url) for url in urls))
)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())