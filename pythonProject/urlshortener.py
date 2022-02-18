import pyshorteners


def urlshortnerM(url):
    shortener = pyshorteners.Shortener()
    x = shortener.tinyurl.short(url)
    return x
