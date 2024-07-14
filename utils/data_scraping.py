import os
import requests
from bs4 import BeautifulSoup

os.chdir("..")


def get_team_names(**kwargs):
    soup = kwargs.get("soup")
    class_ = kwargs.get("class_", None)

    class_table = soup.find("table", class_=class_)
    team_names = {
        "Teams": [cell.text for row in class_table.find_all("tr") for cell in row.find_all("td")]
    }

    return team_names


def get_player_stats_info(**kwargs):
    soup = kwargs.get("soup")
    player_stats_dict = kwargs.get("player_stats_dict", {})
    headers = kwargs.get("headers")

    current_team = ""
    for element in soup.find_all(['h1', 'table']):
        if element.name == 'h1':
            current_team = element.get_text(strip=True)
        elif element.name == 'table' and element.get('class') is None:
            for row in element.find_all('tr')[1:]:
                player_stats_dict['Team'].append(current_team)
                for idx, cell in enumerate(row.find_all('td')):
                    header = headers[idx + 1]  # Adjust index for 'Team' header
                    player_stats_dict[header].append(cell.get_text(strip=True))

    return player_stats_dict
