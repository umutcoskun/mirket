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

```python
mirket.get_stats(URL: str, networks: list=None) -> dict
```

Retrieve social stats for selected networks. If "networks" is None, you will get stats for all the available networks.

Returns a dict that has networks as keys and social stats objects (like FacebookStats, PinterestStats etc. See `stats.py` for more) as values.

---

```python
mirket.get_facebook_stats(URL: str) -> FacebookStats
```

Retrieve Facebook stats for a URL which are shares, likes, comments and clicks. Returns FacebookStats object.

---

```python
mirket.get_pinterest_stats(URL: str) -> PinterestStats
```

Retrieve Pinterest pin count for a URL. Returns PinterestStats object.

---

```python
mirket.get_linkedin_stats(URL: str) -> LinkedInStats
```

Retrieve LinkedIn share count for a URL. Returns LinkedInStats object.

---

```python
mirket.get_stambleupon_stats(URL: str) -> StambleUponStats
```

Retrieve StambleUpon view count for a URL. Returns StambleUponStats object.

---

License: GNU General Public License
