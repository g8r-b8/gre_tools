''' Get lists of books to search'''

import requests
from tqdm import tqdm

def get_books_thegreatestbooks():
    '''Get books from thegreatestbooks.org'''
    avail_pages = range(1,54)
    master_dict = {}
    master_list = []
    for i in tqdm(avail_pages):
        path = f'https://thegreatestbooks.org/?page={i}'
        content = requests.get(path,timeout=10).text
        l = [e for e in content.split('\n')
                if '/items/' in e
                if '/authors/' in e
                if ' by ' in e
                if 'href' in e]
        d = {e.split('>')[1].replace('</a','').replace('&#39;',"'")
                : e.split('>')[3].replace('</a','')
                for e in l}
        books = [format_title_author(e) for e in l]
        master_dict.update(d)
        master_list.extend(books)
    pretty(master_dict)
    print(master_list)

def format_title_author(e):
    return f"{get_title(e)} by {get_author(e)}"

def get_author(e):
    return e.split('>')[3].replace('</a','')

def get_title(e):
    return e.split('>')[1].replace('</a','').replace('&#39;',"'")

def pretty(d, indent=0):
    '''Pretty print dict'''
    for key, value in d.items():
        print('\t' * indent + str(key), end='\n')
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value), end='\n\n')

if __name__ == "__main__":
    get_books_thegreatestbooks()
