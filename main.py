import requests
import os, errno
from bs4 import BeautifulSoup


if __name__ == "__main__":
    with open('links.txt', 'r') as f:
        urls = f.readlines()

    headers = {
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Dest': 'document',
    }

    try:
        os.mkdir("products")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
        else:
            pass

    for i, url in enumerate(urls):
        response = requests.request("GET", url, headers=headers, )

        soup = BeautifulSoup(response.content, 'html.parser')
        article = soup.find(id="viewad-product")
        
        gallery = article.select("div:first-child")[0]
        image_container = gallery.find_all('div', {"class":"galleryimage-element"})
        image_container = [img.find('img') for img in image_container]
        img_links = []

        for img in image_container:
            if img:
                img_links.append(img.attrs['src'])

        price = soup.find(id="viewad-price").get_text(strip=True)
        title = soup.find(id="viewad-title").get_text(strip=True)

        description = soup.find(id="viewad-description")
        con = description.find(class_="l-container")
        
        path = f'products/{title}'
        
        try:
            os.mkdir(path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
            else:
                pass
        
        for idx, url in enumerate(img_links):
            page = requests.get(url)
            f_ext = os.path.splitext(url)[-1]
            f_name = f'{path}/{idx}{f_ext}'
            with open(f_name, 'wb') as f:
                f.write(page.content)
        with open(f'{path}/description.txt', 'w') as f:
            f.write(f"Title: {title}\n\n\n")
            f.write(f"Price: {price}\n\n\n")
            f.write(con.get_text(strip=True, separator="\n"))
        print(f'{i+1}/{len(urls)} processed')