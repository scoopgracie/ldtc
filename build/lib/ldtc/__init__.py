#!/usr/bin/env python3
import sys

def listify(text):
    return [string.lower() for string in text.split(' ') if string.isalpha()]


def compile(raw_model):
    model = {}

    for portion in raw_model:
        text = listify(portion['text'])
        category = portion['language']
        total_words = len(text)
        for word in text:
            weight = 1/total_words
            try:
                model[category][word] += weight
            except:
                try:
                    model[category][word] = weight
                except KeyError:
                    model[category] = { word: weight }

    return model


class Classifier:
    def __init__(self, model, supress_uncompiled_model_warning=False):
        if type(model) == dict:
            self.model = model
        else:
            self.model = compile(model)
            if not supress_uncompiled_model_warning:
                print('WARNING: model was not compiled', file=sys.stderr)
                print('In development, this is OK, but precompiling the model is preferred for production use.', file=sys.stderr)
        self.warn = supress_uncompiled_model_warning

    def check(self, text):
        model = self.model
        text = listify(text)
        probs = {}
        for word in text:
            for category in model.keys():
                try:
                    num = model[category][word]
                except KeyError:
                    num = 0
                weight = 1 
                try:
                    probs[category] += weight * num
                except:
                    probs[category] = weight * num
        most_likely = ['unknown', 0]
        for category in probs.keys():
            if probs[category] > most_likely[1]:
                most_likely = [category, probs[category]]
        return most_likely[0]
