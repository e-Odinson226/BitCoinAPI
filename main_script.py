import requests
try:
    url = 'https://api.lyrics.ovh/v1/%s/%s'
    key = False
    while key == False:
        artist = input("Artist\t : ")
        title = input("Title\t : ")
        response = requests.get( url % (artist, title))
        if (response.json()['lyrics']):
            print (response.json()['lyrics'])
            key = True
        else:
            print("Not found")
except:
    raise Exception("error")