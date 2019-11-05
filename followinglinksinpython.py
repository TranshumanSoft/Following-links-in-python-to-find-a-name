from urllib import request
from bs4 import BeautifulSoup
import ssl

def get_html(url):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    html = request.urlopen(f"{url}", context=context).read()
    return html

def get_tags(html):
    result = []
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    for tag in tags:
        result.append(tag.get('href', None))
    return result

def get_name(url):
    t = url.split('_')[-1]
    return t.split('.')[0]

url = input("Enter url: ")
counter = int(input("Enter count: "))
position = int(input("Enter position: "))-1

for i in range(counter):
    html = get_html(url)
    tags = get_tags(html)
    url = tags[position]

print(get_name(url))