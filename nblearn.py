import numpy as np
import sys
from collections import Counter
import json

from utils import extract_vocabulary, get_train_paths, read_sentence_from_file, text_preprocess, tokenize
from configs import config


def main(train_folder_path):
    train_paths = get_train_paths(train_folder_path)
    vocabulary = extract_vocabulary(train_paths)

    count_doc = dict()
    prior = dict()
    count_word = dict()
    conditional_prob = dict()

    if config.classfication_method == 'two-binary':
        classes = ['positive', 'negative', 'truthful', 'deceptive']
    elif config.classfication_method == 'one-multi':
        classes = ['truthful positive', 'truthful negative', 'deceptive positive', 'deceptive negative']

    for w in vocabulary:
        conditional_prob[w] = dict()
        for c in classes:
            conditional_prob[w][c] = 0

    for c in classes:
        count_doc[c] = len(train_paths[c]) # TODO
    if config.classfication_method == 'two-binary':
        count_doc['all'] = count_doc['positive'] + count_doc['negative']
    elif config.classfication_method == 'one-multi':
        count_doc['all'] = count_doc['truthful positive'] + count_doc['truthful negative'] \
                           + count_doc['deceptive positive'] + count_doc['deceptive negative']

    for c in classes:
        prior[c] = count_doc[c]/count_doc['all']

    for c in classes:
        count_word[c] = Counter()
        for file_path in train_paths[c]:
            if config.count_method == 'appear':
                count_word_in_file = Counter(set(tokenize(text_preprocess(read_sentence_from_file(file_path)))))
            elif config.count_method == 'sum':
                count_word_in_file = Counter(tokenize(text_preprocess(read_sentence_from_file(file_path))))
            count_word[c] += count_word_in_file

        total_count = np.sum(list(count_word[c].values()))
        V = len(vocabulary)
        for w in vocabulary:
            count_w_in_c = count_word[c][w]
            if config.smoothing_method == 'add_one':
                conditional_prob[w][c] = (count_w_in_c + 1) / (total_count + 1.0*config.add_one_scale)
            elif config.smoothing_method == 'laplace':
                conditional_prob[w][c] = (count_w_in_c + 1) / (total_count + V)

    model = {'prior': prior, 'conditional_prob': conditional_prob, 'vocabulary': list(vocabulary)}
    data = json.dumps(model, indent=1)
    with open('./nbmodel.txt', 'w') as model_file:
        model_file.write(data)
        model_file.close()

if __name__ == '__main__':
    train_folder_path = sys.argv[1]
    main(train_folder_path)