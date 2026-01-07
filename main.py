from bs4 import BeautifulSoup
import requests

def get_soup() -> BeautifulSoup:
    headers: dict = {'User-Agent': }