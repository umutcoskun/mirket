#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

from mirket import Mirket


class MirketTestCase(unittest.TestCase):
    """Tests for Mirket."""

    def setUp(self):
        self.mirket = Mirket()
        # A test URL that has lots of stats on all the available networks.
        self.URL = "http://etsy.com"

    def test_valid_stats(self):
        # Check for some valid networks.
        stats = self.mirket.get_stats(self.URL, ["facebook", "pinterest"])
        self.assertTrue("facebook" in stats)
        self.assertTrue("pinterest" in stats)

    def test_invalid_stats(self):
        # Check for an invalid network.
        with self.assertRaises(ValueError):
            self.mirket.get_stats(self.URL, ["salyangoz.me"])

    def test_facebook(self):
        # Check URL has Facebook likes.
        stats = self.mirket.get_facebook_stats(self.URL)
        self.assertGreaterEqual(stats.likes, 1)

    def test_pinterest(self):
        # Check URL has Pinterest pins.
        stats = self.mirket.get_pinterest_stats(self.URL)
        self.assertGreaterEqual(stats.pins, 1)

    def test_linkedin(self):
        # Check URL has LinkedIn shares.
        stats = self.mirket.get_linkedin_stats(self.URL)
        self.assertGreaterEqual(stats.shares, 1)

    def test_stambleupon(self):
        # Check URL has StambleUpon views.
        stats = self.mirket.get_stambleupon_stats(self.URL)
        self.assertGreaterEqual(stats.views, 1)

    def test_stambleupon_invalid(self):
        # Check a URL that has no views.
        blog = "http://safkaninsan.blogspot.com.tr/"
        stats = self.mirket.get_stambleupon_stats(blog)
        self.assertEqual(stats.views, 0)


if __name__ == "__main__":
    unittest.main()
