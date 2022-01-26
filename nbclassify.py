import numpy as np
import sys
import json
from collections import Counter

from utils import get_test_paths, read_sentence_from_file, text_preprocess, tokenize
from configs import config


def main(test_folder_path):
    with open('nbmodel.txt', 'r') as model_file:
        model = json.load(model_file)
        model_file.close()
    vocabulary, prior, conditional_prob = model['vocabulary'], model['prior'], model['conditional_prob']

    test_paths = get_test_paths(test_folder_path)
    N = len(test_paths)

    if config.classfication_method == 'two-binary':
        classification_a = ['truthful', 'deceptive']
        score_a = np.zeros((N,2))
        classification_b = ['positive', 'negative']
        score_b = np.zeros((N,2))
        for c in range(2):
            c_a = classification_a[c]
            c_b = classification_b[c]
            score_a[:, c] = [np.log(prior[c_a])] * N
            score_b[:, c] = [np.log(prior[c_b])] * N
            for n in range(N):
                file_path = test_paths[n]
                if config.count_method == 'appear':
                    count_word_in_file = Counter(set(tokenize(text_preprocess(read_sentence_from_file(file_path)))))
                elif config.count_method == 'sum':
                    count_word_in_file = Counter(tokenize(text_preprocess(read_sentence_from_file(file_path))))
                for word, count in count_word_in_file.items():
                    if word in vocabulary: # TODO: handle unknown words
                        score_a[n][c] += np.log(conditional_prob[word][c_a]) * count
                        score_b[n][c] += np.log(conditional_prob[word][c_b]) * count
        prediction_a = np.argmax(score_a, axis=1)
        prediction_b = np.argmax(score_b, axis=1)

        with open('./nboutput.txt', 'w') as output_file:
            for n in range(N):
                output_file.write(' '.join([classification_a[prediction_a[n]], classification_b[prediction_b[n]], test_paths[n], '\n']))
            output_file.close()
    elif config.classfication_method == 'one-multi':
        classification = ['truthful positive', 'truthful negative', 'deceptive positive', 'deceptive negative']
        score = np.zeros((N, 4))
        for c in range(4):
            class_ = classification[c]
            score[:, c] = [np.log(prior[class_])] * N
        for n in range(N):
            file_path = test_paths[n]
            if config.count_method == 'appear':
                count_word_in_file = Counter(set(tokenize(text_preprocess(read_sentence_from_file(file_path)))))
            elif config.count_method == 'sum':
                count_word_in_file = Counter(tokenize(text_preprocess(read_sentence_from_file(file_path))))
            for word, count in count_word_in_file.items():
                for c in range(4):
                    class_ = classification[c]
                    if word in vocabulary:  # TODO: handle unknown words
                        score[n][c] += np.log(conditional_prob[word][class_]) * count
        predictions = np.argmax(score, axis=1)

        with open('./nboutput.txt', 'w') as output_file:
            for n in range(N):
                output_file.write(' '.join(
                    [classification[predictions[n]], test_paths[n], '\n']))
            output_file.close()


if __name__ == '__main__':
    test_folder_path = sys.argv[1]
    main(test_folder_path)