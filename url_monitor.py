import requests
import logging


def check_url(url: str) -> dict:
    """
    Checks the URL and returns a dictionary(json) of the content.
    """
    try:
        response = requests.get(url)
        if response.status_code != 200:
            logging.fatal("The response status code is not 200")
        return response.text
    except Exception as e:
        logging.error("an error occurred while checking the url", e)
        return None
    