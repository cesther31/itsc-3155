import requests


def indeed_request():
    # TODO 2: Put the code from the Postman steps of the lab here.
    # - Make sure you used the correct URL
    # - Also, erase any unnecessary code like the import statement
    import requests

    url = "https://www.indeed.com/jobs?q=Software Engineer&l=Charlotte"

    payload = {}
    headers = {
    'Cookie': '__cf_bm=X2H3X4wdWY2CLhUdaAY8BY8H7.gTUFS5Gln4pavItd8-1687553641-0-AXXriHcmiPJlHDSoebqZ17xocFF1jsf5yQCjO4S8XRXHtHM80xWCqW3+Em695FAS4IcsLWCo2lcUbCqTEevgoog='
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


    


if __name__ == '__main__':
    indeed_request()
