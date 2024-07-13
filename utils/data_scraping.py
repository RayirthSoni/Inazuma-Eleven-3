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
    player_stats_dict = kwargs.get("player_stats_dict", {})
    player_stats_table = kwargs.get("player_stats_table")
    headers = kwargs.get("headers")

    for table in player_stats_table:
        for row in table.find_all("tr")[1:]:
            for idx, cell in enumerate(row.find_all("td")):
                header = headers[idx]
                player_stats_dict[header].append(cell.get_text(strip=True))

    return player_stats_dict
