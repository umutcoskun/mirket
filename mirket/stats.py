#!/usr/bin/python3


class FacebookStats(object):
    """
    Stores Facebook's social stats.
    """

    def __init__(self, URL, shares, likes, comments, clicks):
        self.URL = URL
        self.shares = shares
        self.likes = likes
        self.comments = comments
        self.clicks = clicks

    @property
    def total_actions(self):
        return self.shares + self.likes + self.comments + self.clicks

    def __str__(self):
        return "{} shares, {} likes, {} comments".format(
            self.shares,
            self.likes,
            self.comments,
        )


class PinterestStats(object):
    """
    Stores Pinterest's social stats.
    """
    def __init__(self, URL, pins):
        self.URL = URL
        self.pins = pins

    @property
    def total_actions(self):
        return self.pins

    def __str__(self):
        return "{} pins".format(
            self.pins,
        )


class LinkedInStats(object):
    """
    Stores LinkedIn's social stats.
    """

    def __init__(self, URL, shares):
        self.URL = URL
        self.shares = shares

    @property
    def total_actions(self):
        return self.shares

    def __str__(self):
        return "{} shares".format(
            self.shares,
        )


class StambleUponStats(object):
    """
    Stores StambleUpon's social stats.
    """

    def __init__(self, URL, views):
        self.URL = URL
        self.views = views

    @property
    def total_actions(self):
        return self.views

    def __str__(self):
        return "{} views".format(
            self.views,
        )
