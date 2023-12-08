from bs4 import BeautifulSoup
import requests
while True:
    champion = str(input("Type champion (q to quit): ")).lower().strip()

    if champion == 'q':
        print("Exiting...")
        break

    use_previous = str(input("Use previous patch? (y - yes): ")).lower()

    url = f'https://u.gg/lol/champions/{champion}/counter'

    if use_previous == 'y':
        url2 = 'https://www.leagueoflegends.com/en-us/news/tags/patch-notes/'
        response_patch = requests.get(url2)
        soup2 = BeautifulSoup(response_patch.text, 'html.parser')
        article_list = soup2.find('ol', class_='style__List-sc-106zuld-2 cGSeTq').find_all('article')
        for index, article in enumerate(article_list, start=1):
            if index == 2:
                last_patch = article.find('h2', class_='style__Title-sc-1h41bzo-8 hvOSAW').text    
                last_patch = last_patch[6:11].strip().replace('.','_')
                break
        url = f'https://u.gg/lol/champions/{champion}/counter?patch={last_patch}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first div element with a specific class
        div_best_winrate = soup.find('div', class_='counters-list best-win-rate')
        div_worst_winrate = soup.find('div', class_='counters-list worst-win-rate')
        div_best_lane_counter = soup.find('div', class_='counters-list gold-diff')
        links_best = div_best_winrate.find_all('a')
        links_worst = div_worst_winrate.find_all('a')
        links_lane_counter = div_best_lane_counter.find_all('a')

        if links_lane_counter:
            if use_previous == 'y':
                print(f'Previous Patch {last_patch}')
            else:
                print('Latest Patch')
            print(f'Best Picks vs {champion.capitalize()}')
            for index, link in enumerate(links_best, start=1):
                champion_name_div = link.find('div', class_='col-2')
                champion_name = champion_name_div.find('div', class_='champion-name').text
                best_wr_div = link.find('div', class_='col-3')
                best_wr = best_wr_div.find('div', class_='win-rate').text
                print(f"{index}. {champion_name} - {best_wr}")
            print('')
            print(f'Worst Picks vs {champion.capitalize()}')
            for index, link in enumerate(links_worst, start=1):
                champion_name_div = link.find('div', class_='col-2')
                champion_name = champion_name_div.find('div', class_='champion-name').text
                worst_wr_div = link.find('div', class_='col-3')
                worst_wr = worst_wr_div.find('div', class_='win-rate').text
                print(f"{index}. {champion_name} - {worst_wr}")
            print('')
            print(f'Best Lane Counters vs {champion.capitalize()}')
            for index, link in enumerate(links_lane_counter, start=1):
                champion_name_div = link.find('div', class_='col-2')
                champion_name = champion_name_div.find('div', class_='champion-name').text
                gold_lead_div = link.find('div', class_='col-3')
                gold_lead = gold_lead_div.find('div', class_='win-rate').text
                print(f"{index}. {champion_name} - {gold_lead}")
            print('')
        else:
            print("Div element not found.")
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)