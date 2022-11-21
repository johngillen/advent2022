#!/usr/bin/python3

from datetime import datetime, timezone, timedelta
from sys import argv
from bs4 import BeautifulSoup
import requests

year, day = datetime.now(timezone(timedelta(hours=-5))).year, \
            datetime.now(timezone(timedelta(hours=-5))).day

if len(argv) == 2:
    day = int(argv[1])
if len(argv) == 3:
    year, day = int(argv[1]), int(argv[2])

cookie = open('util/cookie.txt', 'r').readline().strip()
finput = open('input/day{:0>2}.txt'.format(day), 'w')
ftest = open('test/day{:0>2}.txt'.format(day), 'w')

input = 'https://adventofcode.com/{}/day/{}/input'.format(year, day)
input = requests.get(input, cookies={'session': cookie}).text
test = 'https://adventofcode.com/{}/day/{}'.format(year, day)
test = requests.get(test, cookies={'session': cookie}).text

try:
    soup = BeautifulSoup(test, 'html.parser')
    test = soup.article.pre.code.text
except AttributeError:
    test = ''

finput.write(input)
ftest.write(test)
