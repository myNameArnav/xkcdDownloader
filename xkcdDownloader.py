import requests
from bs4 import BeautifulSoup
import wget

for i in range(1, 2169):
    i = i + 1
    permanent = i
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
    temp_title = img['title']

    title = temp_title.replace("/", ",")

    img_src = img['src']

    if img_src[:1] == "/":
        image = "https://www.xkcd.com" + img_src
        print("> link is now complete")
    else:
        image = img_src
        print("> link was already complete")

    if len(title) > 200:
        title = str(title[0:200])
        print("> length was shoterned" + title)
    else:
        print("> length was not shoterned")

    fileName = "/Users/arnavjain/Documents/xkcd/Comics/" + \
        (str(title) + ".jpg")
    print("> file name has no problem")
    print("> Starting download...")
    wget.download(image, fileName)
    print("\n> Image number " + temp + " is downloaded...")
    print(" ")

print(">>>EVERY DAMN THING IS DOWNLOADED!!<<<")
print("**BE HAPPY**")
