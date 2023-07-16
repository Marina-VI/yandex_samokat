import requests
import configuration as conf

def create_order(data):
    url = conf.URL_SERVICE + conf.CREATE_ORDER
    return requests.post(url, json=data)

def currently_track(response):
    return response.json()["track"]

def order_info(track):
    url = conf.URL_SERVICE + conf.GET_INFO_ABOUT_ORDER + f'?t={track}'
    return requests.get(url)
