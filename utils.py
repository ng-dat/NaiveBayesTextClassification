import numpy as np
import os


def extract_vocabulary(train_paths):
    # file_paths = train_paths['positive'] + train_paths['negative']
    # vocab = set()
    # for file_path in file_paths:
    #     sample = read_sentence_from_file(file_path)
    #     sample = text_preprocess(sample)
    #     sample = tokenize(sample)
    #     for word in sample:
    #         if word not in vocab:
    #             vocab.add(word)
    # return vocab
    pass


def get_train_paths(train_folder_path):
    file_paths = {'positive': [], 'negative':[], 'truthful': [], 'deceptive':[]}
    for root, dirs, files in os.walk(train_folder_path):
        for file_path in files:
            # append the file name to the list
            if file_path.endswith(".txt"):
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


def get_test_paths():
    pass


def text_preprocess(raw_text):
    # TODO: implement
    return raw_text


def tokenize(sample):
    # TODO: implement
    return sample.split(' ')


def read_sentence_from_file(file_path):
    file = open(file_path, 'r')
    raw_text = '\n'.join(file.readlines()) # TODO: file.readlines()[0]
    return raw_text

def read_model_from_file():
    pass


def write_model_to_file():
    pass


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