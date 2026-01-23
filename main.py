from bs4 import BeautifulSoup
import requests
import re

def get_soup() -> BeautifulSoup:
    headers: dict = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'}
    request = requests.get('https://www.bbc.com/news', headers=headers)
    html: bytes = request.content

    # Create soup
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_headlines(soup: BeautifulSoup) -> list[str]:
    headlines: set = set()

    for h in soup.find_all("h2", class_="sc-feaf8701-3"):
        headline: str = h.contents[0].lower()
        headlines.add(headline)

    return sorted(headlines)

def check_headlines(headlines: list, term: str):
    term_list: list[str] = []
    terms_found: int = 0

    for i, headline in enumerate(headlines, start=1):
        if term.lower() in headline:
            terms_found += 1
            term_list.append(headline)
            print(f'{i}: {headline.capitalize()} <---------------------- "{term}"')
        else:
            print(f'{i}: {headline.capitalize()}')

    print('-------------------------------')
    if terms_found:
        print(f'"{term}" was mentioned {terms_found} times.')
        print('-------------------------------')

        for i,headline in enumerate(term_list, start=1):
            print(f'{i}: {headline.capitalize()}')

        else:
            print(f'No matches found: for "{term}"')
            print('-------------------------------')


def main():
    soup: BeautifulSoup = get_soup()
    headlines: list[str] = get_headlines(soup=soup)

    # for headline in headlines:
    #     print(headline)
    user_input: str = 'ukraine'
    check_headlines(headlines, user_input)


if __name__ == '__main__':
    main()