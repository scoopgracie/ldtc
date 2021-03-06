#!/usr/bin/env python3
import argparse
import json
import sys

parser = argparse.ArgumentParser(description="Language-Detecting Text Classifier")
parser.add_argument('model', help='model to use')
parser.add_argument('-c', '--compile', help='compile raw model model to outfile', metavar='outfile')
args = parser.parse_args()

import ldtc # PEP 8 violation, but don't fix it
# Way better for performance of argparse checking

with open(args.model, 'r') as f:
    raw_model = json.load(f)
if args.compile:
    with open(args.compile, 'w+') as f:
        json.dump(ldtc.compile(raw_model), f)
else:
    classifier = ldtc.Classifier(raw_model)
    if sys.stdin.isatty():
        text = input('Text to analyse: ')
    else:
        text = sys.stdin.read()
    print(classifier.check(text))
