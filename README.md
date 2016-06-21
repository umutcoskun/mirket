# Mirket
Get social network stats for a URL.

### Installation
* Development (current)
```python
pip3 install git+https://github.com/umutcoskun/mirket.git
```

### Testing
```python
python3 tests/unit_tests.py
python3 tests/stress_tests.py
```

### Usage
```python
from mirket import Mirket

mirket = Mirket()
```

Create a Mirket instance.

---

##### All Networks Available

```python
mirket.get_stats(URL: str, networks: list=None) -> dict
```

Retrieve social stats for selected networks. If `networks` is `None`, you will get stats for all the available networks.

Returns a `dict` that has networks as keys and social stats objects (like FacebookStats, PinterestStats etc. See `stats.py` for more) as values.

Example:

```python
stats = mirket.get_stats("http://etsy.com", ["facebook", "pinterest"])
print("Etsy has {} Facebook likes and {} Pinterest pins.".format(
    stats["facebook"].likes,
    stats["pinterest"].pins,
))
```

You can see `mirket.available_networks` (a list) for the networks that you can use with Mirket.

---

##### Facebook

```python
mirket.get_facebook_stats(URL: str) -> FacebookStats
```

Retrieve Facebook stats for a URL which are shares, likes, comments and clicks. Returns FacebookStats object.

Example:

```python
URL = ("https://medium.com/@erikdkennedy/"
       "7-rules-for-creating-gorgeous-ui-part-1-559d4e805cda")

stats = mirket.get_facebook_stats(URL)
print("This article shared {} times. Also has {} comments.".format(
    stats.shares,
    stats.comments,
))

```

You can use `stats.likes`, `stats.shares`, `stats.comments`, `stats.clicks` and `stats.total_actions`.

---

##### Pinterest

```python
mirket.get_pinterest_stats(URL: str) -> PinterestStats
```

Retrieve Pinterest pin count for a URL. Returns PinterestStats object.

Example:

```python
stats = mirket.get_pinterest_stats("http://9gag.com/gag/abqq8er")
print("This GAG pinned {} times.".format(
    stats.pins,
))
```

You can use `stats.pins` and `stats.total_actions`.

---

##### LinkedIn

```python
mirket.get_linkedin_stats(URL: str) -> LinkedInStats
```

Retrieve LinkedIn share count for a URL. Returns LinkedInStats object.

Example:

```python
URL = "https://blog.kissmetrics.com/marketers-guide-to-medium/"

stats = mirket.get_linkedin_stats(URL)
print("This article shared {} times on LinkedIn.".format(
    stats.shares,
))
```

You can use `stats.shares` and `stats.total_actions`.

---

##### StumbleUpon

```python
mirket.get_stumbleupon_stats(URL: str) -> StumbleUponStats
```

Retrieve StumbleUpon view count for a URL. Returns StumbleUponStats object.

Example:

```python
URL = ("http://flavorwire.com/"
       "446101/20-movies-guaranteed-to-make-you-feel-stupid")

stats = mirket.get_stumbleupon_stats(URL)
print("This list viewed {} times on StumbleUpon".format(
    stats.views,
))
```

You can use `stats.views` and `stats.total_actions`.

---

License: GNU General Public License
