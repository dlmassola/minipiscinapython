import sys, requests
from bs4 import BeautifulSoup

def SearchWikipeadia(query, links):
    try:

        URL = 'https://en.wikipedia.org{page}'.format(page=query)

        try:
            searchReturn = requests.get(url=URL)
            searchReturn.raise_for_status()
        except Exception as e:
            if (searchReturn.status_code == 404):
                return print("It's a dead end !")
            return print(e)

        soup = BeautifulSoup(searchReturn.text, 'html.parser') # example: <a class="vector-toc-link" href="#Name"><div class="vector-toc-text"><span class="vector-toc-numb">1</span>Name</div>... etc
        title = soup.find(id='firstHeading').text # example: <h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">Pain au chocolat</span></h1>

        if title in links:
            return print("It leads to an infinite loop !")

        print(title)
        links.append(title)
        
        if title == 'Philosophy':
            return print(len(links), "roads from", links[0], "to philosophy!") 
        
        content = soup.find(id='mw-content-text') 
        allLinks = content.select('p > a') 

        for link in allLinks: 
            if link.get('href') is not None and link['href'].startswith('/wiki/')\
                    and not link['href'].startswith('/wiki/Wikipedia:') and not link['href'].startswith('/wiki/Help:'):
                return SearchWikipeadia(link['href'], links)
        
        return print("It leads to a dead end !.")
    except Exception as e:
        return print(e)

def main():
    links = []

    if (len(sys.argv) == 2):
        SearchWikipeadia('/wiki/' + sys.argv[1], links)
    else:
        print('Enter just one parameter.')

if __name__ == '__main__':
    # pip install -r ./requirement.txt
    main()
