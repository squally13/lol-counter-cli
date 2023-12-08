# lol-counter-cli
CLI program that prints out counter stats from u.gg with web scraping.

To use you need to install `BeautifulSoup` and `requests` dependency.

```
pip install beautifulsoup4 requests
```

Output for Ahri (08-12-2023 patch 13.24):
```
Best Picks vs Ahri
1. Twisted Fate - 57.94% WR
2. Neeko - 57.52% WR
3. Akshan - 56.6% WR
4. Pantheon - 56.03% WR
5. Veigar - 55.73% WR
6. Talon - 55.71% WR
7. Cassiopeia - 55% WR
8. Taliyah - 54.31% WR
9. Qiyana - 54.09% WR
10. Sylas - 53.91% WR

Worst Picks vs Ahri
1. Hwei - 30.23% WR
2. Malzahar - 43.63% WR
3. Swain - 45.71% WR
4. Jayce - 46.37% WR
5. Kassadin - 46.67% WR
6. Ekko - 46.73% WR
7. LeBlanc - 47.4% WR
8. Yone - 48.15% WR
9. Diana - 48.37% WR
10. Irelia - 48.39% WR

Best Lane Counters vs Ahri
1. Akshan - +657 GD15
2. Tristana - +604 GD15
3. Yasuo - +570 GD15
4. Zoe - +555 GD15
5. Twisted Fate - +491 GD15
6. Irelia - +489 GD15
7. Naafiri - +395 GD15
8. Diana - +378 GD15
9. Qiyana - +312 GD15
10. LeBlanc - +307 GD15
```