import utils
from utils import extract_vocabulary


tests = [2]
# Test 1: utils.get_train_paths
if 1 in tests:
    train_paths = utils.get_train_paths('./data/op_spam_training_data/unit_test')
    for key in train_paths:
        print(key, ':', train_paths[key], '\n')

# # Test 2: utils.extract_vocabulary
# if 2 in tests:
#     train_paths = utils.get_train_paths('./data/op_spam_training_data/unit_test')
#     vocab = utils.extract_vocabulary(train_paths)
#     print(vocab)