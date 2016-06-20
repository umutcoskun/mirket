from distutils.core import setup

setup(
    name="mirket",
    version="0.1",

    description="Get social network stats for a URL.",

    author="Umut Çağdaş Coşkun",
    author_email="umut34@outlook.com",

    url="https://github.com/umutcoskun/mirket",
    download_url="https://github.com/umutcoskun/mirket/tarball/0.1",

    packages=["mirket"],
    keywords=["social network", "restful api"],
    classifiers=[],
    install_requires=[
        "requests",
    ]
)
