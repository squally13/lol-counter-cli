from bs4 import BeautifulSoup
import requests
 
url = 'https://u.gg/lol/champions/garen/counter'
 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
 
response = requests.get(url, headers=headers)
 
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first div element with a specific class
    div_element = soup.find('div', class_='counters-list gold-diff')
    links = div_element.find_all('a')

    if links:
        for index, link in enumerate(links, start=1):
            champion_div = link.find('div', class_='col-2')
            champion_name = champion_div.find('div', class_='champion-name').text
            print(f"{index}. {champion_name}")
    else:
        print("Div element not found.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)