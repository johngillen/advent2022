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
    test = soup.select('article > pre > code')

    # simple character analysis on candidates for test inputs. works maybe 90%
    # of the time. if it doesn't work, manually find the test input

    bestcase = [test[0].text, 0, 0]
    for case in test:
        case, forwards, backwards = case.text, 0, 0
        for c in case:
            forwards += 1 if c in input else 0
        for i in range(min(len(input), 1000)):
            backwards += 1 if input[i] in case else 0

        bestcase = [case, forwards, backwards] if backwards > bestcase[2] else bestcase
    
    test = bestcase[0]
    bestcase[1] /= len(bestcase[0])
    bestcase[2] /= min(len(input), 1000)

    if (abs(bestcase[1] - bestcase[2]) > 0.3):
        print('test input may not be valid. check manually')
        print(f'https://adventofcode.com/{year}/day/{day}')

except IndexError:
    print('test input is not valid. check manually')
    print(f'https://adventofcode.com/{year}/day/{day}')
    test = ''

finput.write(input)
ftest.write(test)
