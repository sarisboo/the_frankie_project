import urllib.request
from bs4 import BeautifulSoup
from tqdm import tqdm
import re
import requests
import pathlib
import os


def retrieve_episode_url(link):
    mp3_url = ""
    with urllib.request.urlopen(link) as episode:
        try:
            html = episode.read().decode("utf-8")
            match = re.findall("file: '(.*\.mp3)", html)
            if len(match) > 0:
                mp3_url = match[0]
                return mp3_url
        except:
            return None


def format_page_link(num):
    page_format = "http://www.europe1.fr/emissions/Au-coeur-de-l-histoire/"
    try:
        page_number = num
    except:
        return None
    return page_format + str(page_number)


def retrieve_episode_links(page_number):
    link = format_page_link(page_number)

    print(f"Fetching links for page {page_number}")
    with urllib.request.urlopen(link) as response:
        html = response.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find_all("a", "titre")
        episodes_url = list(
            map(lambda link: link.get("href"), links)
        )  # Does this return None ?
        return episodes_url


def fetch_title(episode_url):
    with urllib.request.urlopen(episode_url) as file:
        html = file.read().decode("utf-8")
        title_mix = episode_url.split("/")[-1]
        return title_mix


def download_url(dest_path, mp3_url, episode_url):
    response = requests.get(mp3_url, stream=True)
    size = int(response.headers["Content-Length"]) / 1024 / 1024

    title = fetch_title(episode_url)
    filename = dest_path + "/" + title + ".mp3"

    my_file = pathlib.Path(filename)

    if not my_file.exists():
        print(f"Downloading {filename} ({size} MB)")
        with open(filename + ".downloading", "wb") as file:
            for data in tqdm(response.iter_content()):
                file.write(data)
        os.rename(filename + ".downloading", filename)
