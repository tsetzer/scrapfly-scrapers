# Similarweb.com Scraper

This scraper is using [scrapfly.io](https://scrapfly.io/) and Python to scrape property listing data from Similarweb.com 

Full tutorial <https://scrapfly.io/blog/how-to-scrape-similarweb/>

The scraping code is located in the `similarweb.py` file. It's fully documented and simplified for educational purposes and the example scraper run code can be found in `run.py` file.

This scraper scrapes:
- Similarweb.com website pages for website traffic inisghts
- Similarweb.com website comparing pages for comparing insights
- Similarweb.com website trend pages for trending websites data
- Similarweb.com sitemaps for urls

For output examples see the `./results` directory.

## Fair Use Disclaimer

Note that this code is provided free of charge as is, and Scrapfly does __not__ provide free web scraping support or consultation. For any bugs, see the issue tracker.

## Setup and Use

This Realestate.com.au scraper uses __Python 3.10__ with [scrapfly-sdk](https://pypi.org/project/scrapfly-sdk/) package which is used to scrape and parse Realestatecom's data.

0. Ensure you have __Python 3.10__ and [poetry Python package manager](https://python-poetry.org/docs/#installation) on your system.
1. Retrieve your Scrapfly API key from <https://scrapfly.io/dashboard> and set `SCRAPFLY_KEY` environment variable:
    ```shell
    $ export SCRAPFLY_KEY="YOUR SCRAPFLY KEY"
    ```
2. Clone and install Python environment:
    ```shell
    $ git clone https://github.com/scrapfly/scrapfly-scrapers.git
    $ cd scrapfly-scrapers/similarweb-scraper
    $ poetry install
    ```
3. Run example scrape:
    ```shell
    $ poetry run python run.py
    ```
4. Run tests:
    ```shell
    $ poetry install --with dev
    $ poetry run pytest test.py
    # or specific scraping areas
    $ poetry run pytest test.py -k test_website_scraping
    $ poetry run pytest test.py -k test_website_compare_scraping
    $ poetry run pytest test.py -k test_trend_scraping
    $ poetry run pytest test.py -k test_sitemap_scraping
    ```