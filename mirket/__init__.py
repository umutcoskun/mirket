#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import json
from urllib.parse import quote_plus

import requests

from mirket.stats import (
    FacebookStats, PinterestStats, LinkedInStats, StambleUponStats
)


class Mirket(object):
    _available_networks = {}

    def __init__(self):
        self._available_networks = {
            "facebook": self.get_facebook_stats,
            "pinterest": self.get_pinterest_stats,
            "linkedin": self.get_linkedin_stats,
            "stambleupon": self.get_stambleupon_stats,
        }

    def get_stats(self, URL: str, networks: list=None) -> dict:
        """
        Retrieves a social stat summary.

        Arguments:
            URL
            networks (optional) --  just get stats for selected networks.
                eg: ["facebook", "linkedin"]

        Returns:
            stats -- dict
        """

        # Check for "networks" parameter if it's wrong type.
        if networks is not None and not isinstance(networks, list):
            raise TypeError("Networks argument should be a list, not {}"
                            .format(type(networks)))

        # If "networks" is None, get all available networks.
        if networks is None:
            networks = [network for network in self._available_networks.keys()]

        stats = {}

        # Get stats for selected or default networks.
        for network in networks:
            if network not in self._available_networks:
                raise ValueError("Network {} is not available."
                                 .format(network))

            stats[network] = self._available_networks[network](URL)

        return stats

    def get_facebook_stats(self, URL: str) -> FacebookStats:
        """
        Retrieves Facebook stats of a URL.
        Which are shares, likes, comments and clicks.

        Arguments:
            URL

        Returns:
            FacebookStats (object)
        """

        API = ("https://api.facebook.com"
               "/method/links.getStats?urls={URL}&format=json")

        if isinstance(URL, list):
            raise Exception("Only one URL can be used at once.")

        elif not isinstance(URL, str):
            raise TypeError("URL should be a string.")

        response = requests.get(API.format(
            URL=quote_plus(URL)
        ))

        data = json.loads(response.text)

        if not data:
            raise Exception("No Facebook data found for the URL.")

        stats = FacebookStats(
            data[0]["url"],
            int(data[0]["share_count"]),
            int(data[0]["like_count"]),
            int(data[0]["comment_count"]),
            int(data[0]["click_count"]),
        )
        return stats

    def get_pinterest_stats(self, URL: str) -> PinterestStats:
        """
        Retrieves pin count for a URL.

        Arguments:
            URL

        Returns:
            PinterestStats (object)
        """

        API = ("http://api.pinterest.com"
               "/v1/urls/count.json?&url={URL}")

        if isinstance(URL, list):
            raise Exception("Only one URL can be used at once.")

        elif not isinstance(URL, str):
            raise TypeError("URL should be a string.")

        response = requests.get(API.format(
            URL=quote_plus(URL)
        ))

        # Remove receiveCount() wrapper from the response.
        data = response.text[13:-1]

        data = json.loads(data)

        if not data:
            raise Exception("No Pinterest data found for the URL.")

        stats = PinterestStats(
            data["url"],
            int(data["count"]),
        )
        return stats

    def get_linkedin_stats(self, URL: str) -> LinkedInStats:
        """
        Retrieves LinkedIn share count for a URL.

        Arguments:
            URL

        Returns:
            LinkedInStats (object)
        """

        API = ("http://www.linkedin.com"
               "/countserv/count/share?url={URL}&format=json")

        if isinstance(URL, list):
            raise Exception("Only one URL can be used at once.")

        elif not isinstance(URL, str):
            raise TypeError("URL should be a string.")

        response = requests.get(API.format(
            URL=quote_plus(URL)
        ))

        data = json.loads(response.text)

        if not data:
            raise Exception("No LinkedIn data found for the URL.")

        stats = LinkedInStats(
            data["url"],
            int(data["count"]),
        )

        return stats

    def get_stambleupon_stats(self, URL: str) -> StambleUponStats:
        """
        Retrieves StambleUpon view count for a URL.

        Arguments:
            URL

        Returns:
            StambleUponStats (object)
        """

        API = ("http://www.stumbleupon.com"
               "/services/1.01/badge.getinfo?url={URL}")

        if isinstance(URL, list):
            raise Exception("Only one URL can be used at once.")

        elif not isinstance(URL, str):
            raise TypeError("URL should be a string.")

        response = requests.get(API.format(
            URL=quote_plus(URL)
        ))

        data = json.loads(response.text)

        if not data:
            raise Exception("No StambleUpon data found for the URL.")

        if "views" in data["result"]:
            views = int(data["result"]["views"])

        else:
            views = 0

        stats = StambleUponStats(
            data["result"]["url"],
            views,
        )

        return stats

    @property
    def available_networks(self) -> list:
        """
        Returns available social networks to use
        with get_stats function.
        """
        return list(self._available_networks.keys())
