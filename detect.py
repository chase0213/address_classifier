#!/usr/bin/env python
# coding: utf-8

host = '127.0.0.1'
port = 9199
name = '住所detecter'

import sys
import json
import random

import jubatus
from jubatus.common import Datum

def predict(client):
    # predict the last shogun
    data = [
        Datum({'name': u'伊勢崎'}),
        Datum({'name': u'高崎'}),
        Datum({'name': u'鎌倉'}),
    ]
    for d in data:
        res = client.classify([d])
        # get the predicted shogun name
        sys.stdout.write(max(res[0], key=lambda x: x.score).label)
        sys.stdout.write(' ')
        sys.stdout.write(d.string_values[0][1].encode('utf-8'))
        sys.stdout.write('\n')


if __name__ == '__main__':
    # connect to the jubatus
    client = jubatus.Classifier(host, port, name)
    # run example
    predict(client)

