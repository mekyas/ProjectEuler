import pafy

def url_exist(url):
    try:
        video = pafy.new(url)
        result = True
    except OSError:
        result = False
    return result
url1 = 'https://youtu.be/2TPvbnJwhfw'
url2 = 'https://youtu.be/2TPvbnJwhfk'
print(url_exist(url1))
print(url_exist(url2))