"""Data Scrape
==============

This module contains code for scraping data from the web.
"""

# Ignore pylint warnings
# pylint: disable=line-too-long
# pylint: disable=wrong-import-position

import os
import json
from bs4 import BeautifulSoup
import requests

os.chdir("..")

from constants.constants import Constants
from utils.data_scraping import get_team_names, get_player_stats_info


INAZUMA_ELEVEN3_WEB_FEATURES = Constants.INAZUMA_ELEVEN3_WEB_FEATURES
WEB_INAZUMA_URL = Constants.Scripts.WEB_INAZUMA_ELEVEN_URL
PLAYER_STATS_WEBSITE = WEB_INAZUMA_URL.format(INAZUMA_ELEVEN3_WEB_FEATURES["level_99_stats"])
FRIENDLY_MATCHES_WEBSITE = WEB_INAZUMA_URL.format(INAZUMA_ELEVEN3_WEB_FEATURES["friendly_matches"])
TEAM_NAMES_DATA = "data/team_names.json"
TEAM_STATS_DATA = "data/player_stats.json"


player_stats_response = requests.get(PLAYER_STATS_WEBSITE)
html_content = player_stats_response.content
soup = BeautifulSoup(html_content, "lxml")

# All Teams
team_names = get_team_names(soup=soup, class_="menu")
json_team_names = json.dumps(team_names, indent=4, default=str)
json.dump(team_names, open(TEAM_NAMES_DATA, "w"), indent=4)

# Player Stats Data
player_stats_dict = {}
player_stats_table = soup.find("table", class_=None)

# Header Columns present in table to store to json
headers = [cell.get_text(strip=True) for cell in soup.find("table", class_=None).find("tr").find_all("td")]
player_stats_dict = {header: [] for header in headers}

# All Player Stats Tables Present on Website
player_stats_table = soup.find_all("table", class_=None)
player_stats_dict = get_player_stats_info(player_stats_dict=player_stats_dict, player_stats_table=player_stats_table, headers=headers,)
json_player_stats = json.dumps(player_stats_dict, indent=4, default=str)
json.dump(player_stats_dict, open(TEAM_STATS_DATA, "w"), indent=4)

# Friendly Matches Data
