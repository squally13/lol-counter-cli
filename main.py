from bs4 import BeautifulSoup
import requests

champion = str(input("Type champion: ")).lower()

url = f'https://u.gg/lol/champions/{champion}/counter'
 
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
        print(f'Best Lane Counters vs {champion.capitalize()}')
        for index, link in enumerate(links, start=1):
            champion_name_div = link.find('div', class_='col-2')
            champion_name = champion_name_div.find('div', class_='champion-name').text
            gold_lead_div = link.find('div', class_='col-3')
            gold_lead = gold_lead_div.find('div', class_='win-rate').text
            print(f"{index}. {champion_name} - {gold_lead}")
    else:
        print("Div element not found.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)