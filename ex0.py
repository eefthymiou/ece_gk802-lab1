import requests  # εισαγωγή της βιβλιοθήκης
import datetime


def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


url = 'https://www.youtube.com/'  # προσδιορισμός του url

try:
    with requests.get(url) as response:
        for header in response.headers:
            print(header + response.headers[header])
        print("\n")

        server_header = response.headers.get('Server')
        print("software:",server_header,end="\n")
        

        if response.cookies:
            print("The web server uses cookies\n")
            for cookie in response.cookies:
                print("cookie name:",cookie.name)
                if cookie.expires:
                    print("expiration time:",datetime.datetime.fromtimestamp(cookie.expires) - datetime.datetime.now())
                else:
                    print("expiration time not found")
                print("\n")
        else:
            print("The web server does not use cookies")
    
except Exception as e:
    print("error")

