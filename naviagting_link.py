from config import driver, test_link_for_navigation
from time import sleep
import json
import unicodedata
import re


def start_navigation(f):
    data = json.load(f)
    links = []
    for a in driver.find_elements_by_tag_name('a'):
        link = a.get_attribute('href')
        if "localhost" in str(link):
            if "?id=" in str(link):
                sep = '='
                stripped = link.split(sep, 1)[0]
                links.append(stripped + "=")
            else:
                links.append(link)

    links = list(set(links))

    for link in links:
        if '?id' in str(link):
            for obj in data:
                final_link = link + obj
                driver.get(final_link)
                sleep(2)
                driver.save_screenshot(
                    f"./screenshots/nav_{slugify(final_link)}.png")
        else:
            driver.get(link)
            sleep(2)
            driver.save_screenshot(f"./screenshots/nav_{slugify(link)}.png")


def slugify(value, allow_unicode=False):
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode(
            'ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


if __name__ == "__main__":
    driver.get(test_link_for_navigation)
    f = open('malicious_navigation.json')
    sleep(2)
    start_navigation(f)
