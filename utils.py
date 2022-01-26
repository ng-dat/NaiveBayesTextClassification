import numpy as np
import os
import re

from configs import config


def extract_vocabulary(train_paths):
    if config.classfication_method == 'two-binary':
        file_paths = train_paths['positive'] + train_paths['negative']
    elif config.classfication_method == 'one-multi':
        file_paths = train_paths['positive truthful'] + train_paths['negative truthful'] \
                    + train_paths['positive deceptive'] + train_paths['negative deceptive']

    vocab = set()
    for file_path in file_paths:
        sample = read_sentence_from_file(file_path)
        sample = text_preprocess(sample)
        sample = tokenize(sample)
        for word in sample:
            if word not in vocab:
                vocab.add(word)
    return vocab


def get_train_paths(train_folder_path):
    if config.classfication_method == 'two-binary':
        file_paths = {'positive': [], 'negative':[], 'truthful': [], 'deceptive':[]}
        for root, dirs, files in os.walk(train_folder_path):
            for file_path in files:
                if file_path.endswith(".txt") and 'README' not in file_path:
                    full_file_path = os.path.join(root, file_path)
                    if 'positive' in full_file_path:
                        file_paths['positive'].append(full_file_path)
                    elif 'negative' in full_file_path:
                        file_paths['negative'].append(full_file_path)
                    if 'truthful' in full_file_path:
                        file_paths['truthful'].append(full_file_path)
                    elif 'deceptive' in full_file_path:
                        file_paths['deceptive'].append(full_file_path)
        return file_paths
    elif config.classfication_method == 'one-multi':
        file_paths = {'positive truthful': [], 'negative truthful': [], 'positive deceptive': [], 'negative deceptive': []}
        for root, dirs, files in os.walk(train_folder_path):
            for file_path in files:
                if file_path.endswith(".txt") and 'README' not in file_path:
                    full_file_path = os.path.join(root, file_path)
                    if 'positive' in full_file_path and 'truthful' in full_file_path:
                        file_paths['positive truthful'].append(full_file_path)
                    elif 'positive' in full_file_path and 'deceptive' in full_file_path:
                        file_paths['positive deceptive'].append(full_file_path)
                    elif 'negative' in full_file_path and 'truthful' in full_file_path:
                        file_paths['negative truthful'].append(full_file_path)
                    elif 'negative' in full_file_path and 'deceptive' in full_file_path:
                        file_paths['negative deceptive'].append(full_file_path)
        return file_paths


def get_test_paths(test_folder_path):
    file_paths = []
    for root, dirs, files in os.walk(test_folder_path):
        for file_path in files:
            if file_path.endswith(".txt") and 'README' not in file_path:
                full_file_path = os.path.join(root, file_path)
                file_paths.append(full_file_path)
    return file_paths


def text_preprocess(raw_text):
    # TODO: implement. Ex: what to replace by '', what to replace by ' '
    if config.remove_symbol:
        raw_text = re.sub('[^a-zA-Z0-9]', ' ', raw_text)
    if config.remove_digits:
        raw_text = re.sub('[0-9]', ' ', raw_text)
    if config.make_lower_case:
        raw_text = raw_text.lower()
    return raw_text


def tokenize(sample):
    # TODO: implement
    return sample.split()


def read_sentence_from_file(file_path):
    file = open(file_path, 'r')
    raw_text = '\n'.join(file.readlines()) # TODO: file.readlines()[0]
    return raw_text


def write_prediction_to_file():
    pass


def read_prediction_from_file():
    pass


def score_predictions_f1():
    pass


def score_predictions_f1_truthful():
    pass


def score_predictions_f1_deceptive():
    pass


def score_predictions_f1_positive():
    pass


def score_predictions_f1_negative():
    pass