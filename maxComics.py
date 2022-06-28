def finder():
    import requests

    higher = 10000
    lower = 0
    prevCenter = 0
    while True:
        center = (higher + lower) // 2
        response = requests.get("https://www.xkcd.com/" + str(center) + "/")
        r = str(response)[11:-2]
        if r == "200":
            lower = center
        elif r == "404":
            higher = center
        else:
            print("idk")
        if prevCenter == center:
            break
        else:
            prevCenter = center

    return center
