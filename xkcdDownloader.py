import requests
import os
from bs4 import BeautifulSoup
import wget
import logging
from threading import Thread
from sanitize_filename import sanitize


def getMaxComicNumber():
    res = requests.get("https://xkcd.com/info.0.json").json()
    return res["num"]


def download_image(i, url, logger):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return 0

        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        div = soup.find(id="comic")
        img = div.find("img")
        temp_title = img["title"]

        title = temp_title.replace("/", ",")

        img_src = img["src"]

        if img_src.startswith("/"):
            image = f"https://www.xkcd.com{img_src}"
        else:
            image = img_src

        title = sanitize(f"{i}-{title}")

        if not os.path.exists("comics"):
            os.makedirs("comics")

        file_name = os.path.join("comics", f"{title}.png")
        try:
            wget.download(image, file_name)
        except Exception as e:
            logger.exception(f"An error occurred for image {url}: {e}")

        logger.info(f"\n> Image {url} is downloaded")

    except Exception as e:
        logger.exception(f"An error occurred for image {url}: {e}")


def downloader():
    logging.basicConfig(
        filename="xkcdDownloadLog.log", level=logging.INFO, filemode="w"
    )
    logger = logging.getLogger()
    counter = getMaxComicNumber()

    session = requests.Session()

    threads = []
    for i in range(1, counter + 1):
        url = f"https://www.xkcd.com/{i}/"

        thread = Thread(target=download_image, args=(i, url, logger))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\n>>> EVERY THING IS DOWNLOADED <<<")
