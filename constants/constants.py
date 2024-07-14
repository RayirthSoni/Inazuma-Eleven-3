"""Constants
============

This module contains constants that have been used in entire codebase
"""

# Ignore pylint warngings
# pylint: disable=line-too-long


class Constants:
    """constants configurations"""

    INAZUMA_ELEVEN1_WEB_FEATURES = {"level_99_stats": "1/stats_ie1"}

    INANUMA_ELEVEN2_WEB_FEATURES = {
        "connection_map": "2/inazuma_eleven_2_connection_map",
        "moves_list": "2/waza_ie2",
        "recuritments": "2/recruit",
        "friendly_matches": "2/ie2_friendly_matches",
        "level_99_stats": "2/stats_ie2",
        "cheats": "2/inazuma-eleven-2-cheats-action-replay-codes",
    }

    INAZUMA_ELEVEN3_WEB_FEATURES = {
        "connection_map": "3/ie3_connection_map",
        "recuritments": "3/ie3_recruit",
        "friendly_matches": "3/ie3_friendly_matches",
        "level_99_stats": "3/inazuma-eleven-3-stats-players-level-99",
    }

    class Scripts:
        """scripts constants"""

        # WEB_HOME_URL = "http://watashiwa7.altervista.org/ie/index.html"
        WEB_INAZUMA_ELEVEN_URL = "http://watashiwa7.altervista.org/ie/{}.htm"

    class Data:
        """data constants"""

        TEAM_NAMES_DATA = r"INAZUMA-ELEVEN-3/data/team_names.json"
        TEAM_STATS_DATA = r"INAZUMA-ELEVEN-3/data/player_stats.json"

