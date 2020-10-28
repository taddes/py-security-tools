"""
https://httpbin.org/
For testing purposes
"""
import requests
import webbrowser
import json


def main():
    data = dict(username="Pep")
    headers = {'Content-Type': 'application/json'}
    response = requests.get('https://httpbin.org/get')
    # print(response.status_code)
    # print(response.json())
    # webbrowser.open(response.json()['url'])

    response2 = requests.post('https://httpbin.org/post', 
                    json.dumps(data), headers=headers)
    print(response2.json())

if __name__ == "__main__":
    main()