import requests
from bs4 import BeautifulSoup
import wget
from maxComics import finder

counter = finder()

for i in range(1, counter):
    temp = str(i)
    url = "https://www.xkcd.com/" + temp + "/"
    print(url)
    r = requests.get(url)
    temp_r = str(r)

    if temp_r != "200":
        print("> Status code is good...")
    else:
        print("> Houston, we have a problem!")

    html_content = r.text

    soup = BeautifulSoup(html_content, "html.parser")

    div = soup.find(id="comic")
    print("> found div")
    img = div.find("img")
    print("> found image")
    temp_title = img["title"]

    title = temp_title.replace("/", ",")

    img_src = img["src"]

    if img_src[:1] == "/":
        image = "https://www.xkcd.com" + img_src
        print("> link is now complete")
    else:
        image = img_src
        print("> link was already complete")

    if len(title) > 250:
        title = str(title[0:250])
        print("> length was shortened to..." + title)
    else:
        print("> length was not shortened")

    fileName = str(title) + ".png"
    print("> file name has no problem")
    print("> Starting download...")
    try:
        wget.download(image, fileName)
    except:
        print("Download had a problem, skipping to the next image")
    print("\n> Image number " + temp + " is downloaded...")
    print(" ")
    i = i + 1

print(">>> EVERY THING IS DOWNLOADED <<<")
