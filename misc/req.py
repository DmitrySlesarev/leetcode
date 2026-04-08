""" requests quickstart"""
import requests
from icecream import ic

if __name__ == "__main__":
    # r = requests.get('https://api.github.com/events')
    # print(r)
    # print(r.json())
    # r = requests.post('https://httpbin.org/post', data={'key': 'value'})
    # ic(r)
    # ic(r.json())

    r = requests.put('https://httpbin.org/put', data={'key':'value'})
    ic(r)
    ic(r.json())