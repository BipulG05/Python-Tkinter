from urllib.request import urlopen
image_formats = ("image/png", "image/jpeg", "image/gif")
url = "http://Millie_Bobby_Brown.png"
site = urlopen(url)
meta = site.info()  # get header of the http request
if meta["content-type"] in image_formats:  # check if the content-type is a image
    print("it is an image")