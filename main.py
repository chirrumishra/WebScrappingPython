from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.espn.com/nfl/qbr"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
league_table = soup.find('table', class_="Table Table--align-right Table--fixed Table--fixed-left")
points_table = soup.find('table', class_='Table Table--align-right')

#csv file starts
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['SrNo','Name','Cou','QBR','PAA','PLAYS','EPA','PASS','RUN','SACK','PEN','RAW']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    #writer.writerow({'SrNo':'1','Name':'CHIRRU','Cou':'co','QBR':'Hey','PAA':'Blacnk','PLAYS':'jja','EPA':'kas','PASS':'akshhd','RUN':'ad','SACK':'ask','PEN':'sad','RAW':'asd'})
    for team in league_table.find_all('tbody',class_='Table__TBODY'):
        rows = team.find_all('tr')
        for row in rows:
            pl_team = row.find('a',class_='AnchorLink').text.strip()
            pl_spot = row.find_all('td',class_='Table__TD')[0].text
            pl_cou = row.find('span',class_='pl2 n10 athleteCell__teamAbbrev').text.strip()
            #print(pl_spot,pl_team,pl_cou)
            writer.writerow({'SrNo':str(pl_spot),'Name':str(pl_team),'Cou':str(pl_cou)})

    for point in points_table.find_all('tbody',class_='Table__TBODY'):
        rows1 = point.find_all('tr')
        for po in rows1:
            pl_qbr = po.find_all('td',class_='Table__TD')[0].text
            pl_paa = po.find_all('td',class_='Table__TD')[1].text
            pl_plays = po.find_all('td', class_='Table__TD')[2].text
            pl_epa = po.find_all('td', class_='Table__TD')[3].text
            pl_pass = po.find_all('td', class_='Table__TD')[4].text
            pl_run = po.find_all('td', class_='Table__TD')[5].text
            pl_sack = po.find_all('td', class_='Table__TD')[6].text
            pl_pen = po.find_all('td', class_='Table__TD')[7].text
            pl_raw = po.find_all('td', class_='Table__TD')[8].text
            #print(pl_qbr,pl_paa,pl_plays,pl_epa,pl_pass,pl_run,pl_sack,pl_pen,pl_raw)
            writer.writerow({'QBR':str(pl_qbr),'PAA':str(pl_paa),'PLAYS':str(pl_plays),'EPA':str(pl_epa),'PASS':str(pl_pass),'RUN':str(pl_run),'SACK':str(pl_sack),'PEN':str(pl_pen),'RAW':str(pl_raw)})
