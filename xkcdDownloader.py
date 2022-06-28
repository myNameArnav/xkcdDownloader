def downloader():
    import requests
    from bs4 import BeautifulSoup
    import wget
    from maxComics import finder
    import logging

    logging.basicConfig(filename="xkcdDownloadLog.log", level=logging.INFO, filemode="w")
    logger = logging.getLogger()
    counter = finder()
    for i in range(1, counter):
        temp = str(i)
        url = "https://www.xkcd.com/" + temp + "/"
        logger.info(url)
        r = requests.get(url)
        temp_r = str(r)

        if temp_r != "200":
            logger.info("> Status code is good...")
        else:
            logger.info("> Houston, we have a problem!")

        html_content = r.text

        soup = BeautifulSoup(html_content, "html.parser")

        div = soup.find(id="comic")
        logger.info("> found div")
        img = div.find("img")
        logger.info("> found image")
        temp_title = img["title"]

        title = temp_title.replace("/", ",")

        img_src = img["src"]

        if img_src[:1] == "/":
            image = "https://www.xkcd.com" + img_src
            logger.info("> link is now complete")
        else:
            image = img_src
            logger.info("> link was already complete")

        if len(title) > 250:
            title = str(title[0:250])
            logger.info("> length was shortened to..." + title)
        else:
            logger.info("> length was not shortened")

        fileName = str(title) + ".png"
        logger.info("> file name has no problem")
        logger.info("> Starting download...")
        try:
            wget.download(image, fileName)
        except:
            logger.info("Download had a problem, skipping to the next image")
        logger.info("\n> Image number " + temp + " is downloaded...")
        logger.info(" ")
        i = i + 1

    print(">>> EVERY THING IS DOWNLOADED <<<")
