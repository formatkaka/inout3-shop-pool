import geocoder
# from bs4 import BeautifulSoup
# import urllib2
# # import gpxpy
# import codecs
from math import sin, cos, sqrt, atan2, radians

from flask_restful import abort

pool_addresses = []
pool_cordinates = []
longs = []
lats = []
prices = []

import os

print os.getcwd()

with open('app/static/pool.txt', "r") as text_file:
    ll_lines = text_file.read().splitlines()
    pool_addresses = [l for l in ll_lines if l]

with open('app/static/latitude.txt', "r") as text_file:
    ll_lines = text_file.read().splitlines()
    lats = [l for l in ll_lines if l]

with open('app/static/longitude.txt', "r") as text_file:
    ll_lines = text_file.read().splitlines()
    longs = [l for l in ll_lines if l]

with open('app/static/prices.txt', "r") as text_file:
    ll_lines = text_file.read().splitlines()
    prices = [l for l in ll_lines if l]


# response = urllib2.urlopen('https://www.flipkart.com/top-notch-men-s-solid-casual-white-black-dark-blue-shirt/p/itmebfhh5jwhhbqc?pid=SHTEBFHHQGZX3BUP&otracker=hp_omu_Deals%20of%20the%20Day_2_f26c2441-7f78-44fe-b7ef-8411fcc9fc73_0&st=size&sattr=size')
# content = response.read()
# soup = BeautifulSoup(content)
# with open("./data.html",'r') as file:
# 	content = file.read()
# soup = BeautifulSoup(content)
# a = soup.find_all("div", {"class": "_1vC4OE_37U4_g"}).get_text()
# print a
def get_longlat(address):
    g = geocoder.google(address)
    cordinates = g.latlng
    # print cordinates
    return cordinates


def get_pool_cordinates():
    for add in pool_addresses:
        pool_cordinates = get_longlat(add)
        lats.append(pool_cordinates[0])
        longs.append(pool_cordinates[1])


# get_longlat('parle point surat')
def distance(latitude1, longitude1, latitude2, longitude2):
    R = 6373.0
    lat1 = radians(float(latitude1))
    lon1 = radians(float(longitude1))
    lat2 = radians(float(latitude2))
    lon2 = radians(float(longitude2))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


# def distance(latitude1,longitude1,latitude2,longitude2):
# 	dist = gpxpy.geo.haversine_distance(latitude1,longitude1,latitude2,longitude2)
# 	return dist

def get_distance(address, price):
    min_dist = 1000000
    min_price = 0

    global pool_addresses
    global prices
    global longs
    global lats
    global pool_cordinates

    length = len(pool_addresses)

    if length:
        user_cordinates = []
        for i in range(0, len(pool_addresses)):
            user_cordinates = get_longlat(address)
            dist = distance(lats[i], longs[i], user_cordinates[0], user_cordinates[1])

            if (dist <= min_dist and int(prices[i]) > min_price):
                min_dist = dist
                min_price = prices[i]
                rem_index = i

        if min_dist > 5:
            lats.append(user_cordinates[0])
            longs.append(user_cordinates[1])
            pool_addresses.append(address)
            prices.append(price)
            return None,None,None


        else:
            a, b, c = min_dist, pool_addresses[rem_index], prices[rem_index]
            prices.remove(prices[rem_index])
            lats.remove(lats[rem_index])
            longs.remove(longs[rem_index])
            pool_addresses.remove(pool_addresses[rem_index])
            do_it()
            return a, b, c

    else:
        pool_addresses.append(address)
        prices.append(price)
        get_pool_cordinates()
        return None, None, None

    do_it()


def do_it():
    with open('app/static/pool.txt', "w") as text_file:
        for add in pool_addresses:
            text_file.write('{0}\n'.format(str(add)))
    with open('app/static/latitude.txt', "w") as text_file:
        for add in lats:
            text_file.write('{0}\n'.format(str(add)))
    with open('app/static/longitude.txt', "w") as text_file:
        for add in longs:
            text_file.write('{0}\n'.format(str(add)))
    with open('app/static/prices.txt', "w") as text_file:
        for add in prices:
            text_file.write('{0}\n'.format(str(add)))


# get_distance('parle point surat, india', 20)
# get_distance('svnit surat, india', 20)
# print pool_addresses, longs, prices, lats


# get_longlat(pool_addresses[0])
# get_longlat(pool_addresses[1])
