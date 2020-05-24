#!/usr/bin/env python3
import sys

def listify(text):
    return [string.lower() for string in text.split(' ') if string.isalpha()]


def compile(raw_model):
    model = {}

    for portion in raw_model:
        text = listify(portion['text'])
        category = portion['language']
        for word in text:
            try:
                model[category].append(word)
            except:
                model[category] = [word]
            model[category].sort()

    return {'text': model}


class Classifier:
    def __init__(self, model, supress_uncompiled_model_warning=False):
        if type(model['text']) == dict:
            self.model = model
        else:
            self.model = compile(model)
            if not supress_uncompiled_model_warning:
                print('WARNING: model was not compiled', file=sys.stderr)
                print('In development, this is OK, but precompiling the model is preferred for production use.', file=sys.stderr)
        self.warn = supress_uncompiled_model_warning

    def check(self, text):
        model = self.model
        model = model['text']
        text = listify(text)
        probs = {}
        for word in text:
            for category in model.keys():
                for catword in model[category]:
                    if word == catword:
                        weight = 1 
                        try:
                            probs[category] += weight 
                        except:
                            probs[category] = weight
        most_likely = ['unknown', 0]
        for category in probs.keys():
            if probs[category] > most_likely[1]:
                most_likely = [category, probs[category]]
        return most_likely[0]
