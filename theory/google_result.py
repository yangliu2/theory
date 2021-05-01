from re import search
import argparse
import logging
from typing import List
from pprint import pprint
from googlesearch import search
from tqdm import tqdm
import urllib
from bs4 import BeautifulSoup


def google_scrape(url) -> str:
    """Scrape a website for title text

    Args:
        url ([type]): website url

    Returns:
        str: title of website
    """
    thepage = urllib.request.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text


def google_query(query: str,
                 page_count: int) -> List:
    """Use the google package to pull weburls from google results.

    Args:
        query (str): query string
        page_count (int): how many results to get from google

    Returns:
        List: List of result dict {title: title string, url: url string}
    """
    results = []
    search_results = search(query, stop=page_count)
    logging.debug("Start scraping individual website for title.")
    for url in tqdm(search_results):
        title = google_scrape(url)
        results.append({"title": title, "url": url})

    return results


def main():
    parser = argparse.ArgumentParser(
        description='Get results from Google search')
    parser.add_argument('-q',
                        '--query',
                        help="query to get Google search results")
    parser.add_argument('-p',
                        '--page_count',
                        default=1,
                        help="how many pages of search results")
    args = parser.parse_args()
    results = google_query(query=args.query,
                           page_count=int(args.page_count))
    pprint(results)


if __name__ == "__main__":
    main()
