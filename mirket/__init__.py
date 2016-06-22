#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
from urllib.parse import quote_plus, urlencode

from requests_futures.sessions import FuturesSession

from mirket.stats import (
    FacebookStats, PinterestStats, LinkedInStats, StumbleUponStats
)


class Mirket(object):

    # Default request headers.
    headers = {"Connection": "close"}

    def __init__(self):
        # Create a FuturesSession instance
        # to make asynchronous requests.
        self.session = FuturesSession()

        # Index all callables to use with
        # the `get_stats` function.
        self._available_networks = {
            "facebook": self.get_facebook_stats,
            "pinterest": self.get_pinterest_stats,
            "linkedin": self.get_linkedin_stats,
            "stumbleupon": self.get_stumbleupon_stats,
        }

    @property
    def available_networks(self) -> list:
        """
        Returns available social networks to use
        with get_stats function.
        """
        return list(self._available_networks.keys())

    def _make_request(self, API: str, URL: str) -> object:
        """
        Make a GET request to target API,
        with the given URL as payload.

        Arguments:
            API -- Target API's endpoint to get stats.
            URL -- Payload for request.

        Returns:
            response (object)
        """

        if isinstance(URL, list):
            raise Exception("Only one URL can be used at once.")

        elif not isinstance(URL, str):
            raise TypeError("URL should be a string.")

        future = self.session.get(
            API.format(URL=quote_plus(URL)),
            headers=self.headers,
        )

        return future.result()

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

        # If `networks` is None, get all available networks.
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

        response = self._make_request(API, URL)

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

        response = self._make_request(API, URL)

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

        response = self._make_request(API, URL)

        data = json.loads(response.text)

        if not data:
            raise Exception("No LinkedIn data found for the URL.")

        stats = LinkedInStats(
            data["url"],
            int(data["count"]),
        )

        return stats

    def get_stumbleupon_stats(self, URL: str) -> StumbleUponStats:
        """
        Retrieves StumbleUpon view count for a URL.

        Arguments:
            URL

        Returns:
            StumbleUponStats (object)
        """

        API = ("http://www.stumbleupon.com"
               "/services/1.01/badge.getinfo?url={URL}")

        response = self._make_request(API, URL)

        data = json.loads(response.text)

        if not data:
            raise Exception("No StumbleUpon data found for the URL.")

        if "views" in data["result"]:
            views = int(data["result"]["views"])

        else:
            views = 0

        stats = StumbleUponStats(
            data["result"]["url"],
            views,
        )

        return stats

    def get_facebook_share_link(self, URL: str, **kwargs) -> str:
        """
        Creates Facebook share link with the UTM parameters.

        Arguments:
            URL -- Link that you want to share.

        Keyword Arguments:
            You can pass query string parameters as keyword arguments.
            Example: utm_source, utm_medium, utm_campaign etc...

        Returns:
            URL -- Facebook share link for the URL.
        """

        URL = "https://facebook.com/sharer/sharer.php?u={URL}?{args}".format(
            URL=quote_plus(URL),
            args=quote_plus(urlencode(kwargs)),
        )

        return URL

    def get_twitter_share_link(self, URL: str, **kwargs) -> str:
        """
        Creates Twitter share link with the UTM parameters.

        Arguments:
            URL -- Link that you want to share.

        Keyword Arguments:
            You can pass query string parameters as keyword arguments.
            Example: utm_source, utm_medium, utm_campaign etc...

        Returns:
            URL -- Twitter share link for the URL.
        """

        URL = "https://twitter.com/home?status={URL}?{args}".format(
            URL=quote_plus(URL),
            args=quote_plus(urlencode(kwargs)),
        )

        return URL

    def get_gplus_share_link(self, URL: str, **kwargs) -> str:
        """
        Creates Google+ share link with the UTM parameters.

        Arguments:
            URL -- Link that you want to share.

        Keyword Arguments:
            You can pass query string parameters as keyword arguments.
            Example: utm_source, utm_medium, utm_campaign etc...

        Returns:
            URL -- Google+ share link for the URL.
        """

        URL = "https://plus.google.com/share?url={URL}?{args}".format(
            URL=quote_plus(URL),
            args=quote_plus(urlencode(kwargs)),
        )

        return URL
