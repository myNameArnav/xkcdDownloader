import requests


def finder():
    higher = 10000
    lower = 0
    prevCenter = 0
    # magicNumber = 2893
    while True:
        center = (higher + lower) // 2
        response = requests.get("https://www.xkcd.com/" + str(center) + "/")
        r = str(response)[11:-2]
        if r == "200":
            lower = center
            # print("lower = " + str(lower))
        elif r == "404":
            higher = center
            # print("higher = " + str(higher))
        else:
            print("idk")
        if prevCenter == center:
            print(center)
            break
        else:
            prevCenter = center

    return center
