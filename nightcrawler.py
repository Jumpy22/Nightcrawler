import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.parse import urlparse
import sys

def find_links(url, max_depth, current_depth=0, visited=None):
    if visited is None:
        visited = set()
    
    if current_depth > max_depth:
        return
    
    try:
        ua = UserAgent()
        header = {'User-Agent': ua.random}
        response = requests.get(url, headers=header)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            domain = urlparse(url).netloc
            links = soup.find_all('a')
            
            with open('links.txt', 'a') as file:
                with open("parameters.txt", "a") as paramTXT:
                    for link in links:
                        href = link.get('href')
                        if href:
                            parsed_href = urlparse(href)
                            if parsed_href.netloc == domain:
                                if href not in visited:
                                    visited.add(href)
                                    if "?" in href:
                                        paramTXT.write(href + '\n')
                                    else:
                                        file.write(href + '\n')
                                    find_links(href, max_depth, current_depth + 1, visited)
                            else:
                                print('Target domain not present in:', href)
            if current_depth == 0:
                print("Crawl completed up to depth", max_depth)
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Error:", e)

def main():
    args = sys.argv[1:]
    
    if len(args) != 2:
        url = input("URL >> ")
        depth = int(input("Depth >> "))
        find_links(url, depth)
    else:
        url = args[0]
        depth = int(args[1])
        find_links(url, depth)

if __name__ == "__main__":
    main()
