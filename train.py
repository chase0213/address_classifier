#!/usr/bin/env python
# coding: utf-8

host = '127.0.0.1'
port = 9199
name = '住所detecter'
tnum = 100000

import sys
import json
import random

import jubatus
from jubatus.common import Datum

def train(client):
    # prepare training data
    # predict the last ones (that are commented out)
    train_data = []
    counter = 0
    for line in open('data/zenkoku_utf-8.csv'):
        line = line.replace('"','')
        adrs_cd, pref_cd, city_cd, town_cd, pn, of, df, pref, pref_ph, city, city_ph, town, town_ph, town_ai, kyoto_ave, aza, aza_ph, ai, of_name, of_ph, oa, new_acd = line.split(',')
        train_data.append((pref, Datum({'name': city})))
        if counter < tnum:
            counter += 1
        else:
            break

    # training data must be shuffled on online learning!
    random.shuffle(train_data)

    # run train
    client.train(train_data)

if __name__ == '__main__':
    # connect to the jubatus
    client = jubatus.Classifier(host, port, name)
    # run example
    train(client)

