import csv
import argparse, configparser
import os
from PARSER import stanford_parser
from nltk import sent_tokenize, word_tokenize
from nltk.tokenize import MWETokenizer

mwe_tokenizer = MWETokenizer()
mwe_tokenizer.add_mwe(('<', 'e1', '>'))
mwe_tokenizer.add_mwe(('<', '/e1', '>'))
mwe_tokenizer.add_mwe(('<', 'e2', '>'))
mwe_tokenizer.add_mwe(('<', '/e2', '>'))


class RelExtractor():

    # def __init__(self):
    @staticmethod
    def read_train_data():
        with open('./data/train/dataset_csv.csv', 'r', newline='\n') as sentence_csv:
            csv_reader = csv.reader(sentence_csv, delimiter='|')
            sentence_list_train = [i[0].lower() for i in csv_reader]
            ans_list_train = [i[1] for i in csv_reader]
        return sentence_list_train, ans_list_train

    @staticmethod
    def read_test_data():
        with open('./data/test/dataset_csv.csv', 'r', newline='\n') as sentence_csv:
            csv_reader = csv.reader(sentence_csv, delimiter='|')
            sentence_list_test = [i[0].lower() for i in csv_reader]
            ans_list_test = [i[1] for i in csv_reader]
        return sentence_list_test, ans_list_test

    @staticmethod
    def make_w_i_dictionary():
        with open('./word/word_list.csv', 'r', newline='\n') as word_csv:
            csv_reader = csv.reader(word_csv)
            word_list = [i[0] for i in csv_reader]
        word_to_index = {w: idx for idx, w in enumerate(word_list)}
        index_to_word = {idx: w for idx, w in enumerate(word_list)}
        return word_to_index, index_to_word

    @staticmethod
    def setence_to_list(sentence, word_to_index, max_sentence_len):
        result_sentence = [word_to_index[i] for i in sentence]
        result_sentence = result_sentence + [len(word_to_index)] * (max_sentence_len - len(result_sentence))
        return result_sentence

    @staticmethod
    def preprocess_sentence_data(sentence):
        sentence = word_tokenize(sentence)
        sentence = mwe_tokenizer.tokenize(sentence)
        e1_start, e1_end, e2_start, e2_end = sentence.index('<_e1_>'), sentence.index('<_/e1_>'), sentence.index(
            '<_e2_>'), sentence.index('<_/e2_>')
        sentence.remove('<_e1_>')
        sentence.remove('<_/e1_>')
        sentence.remove('<_e2_>')
        sentence.remove('<_/e2_>')
        e1_start, e1_end, e2_start, e2_end = e1_start , e1_end - 1, e2_start - 2, e2_end - 3
        return sentence, [e1_start, e1_end, e2_start, e2_end]


def main():
    # load sentence list
    rel_extractor = RelExtractor()
    dep_parser = stanford_parser.StanfordDependencyParser()
    sentence_list_train, ans_list_train = rel_extractor.read_train_data()
    word_to_index, index_to_word = rel_extractor.make_w_i_dictionary()
    sentence_list_train_idx = []
    entity_loc_list = []

    for sentence_train in sentence_list_train:
        print(sentence_train)
        sentence, entity_loc = rel_extractor.preprocess_sentence_data(sentence_train)
        print(entity_loc)
        print(sentence)
        print(sentence[entity_loc[0]], sentence[entity_loc[2]])
        print(dep_parser.get_relationship_feature(sentence, sentence[entity_loc[0]],sentence[entity_loc[2]]))
        result_sentence = rel_extractor.setence_to_list(sentence, word_to_index, 85)
        print(result_sentence)
        sentence_list_train_idx.append(result_sentence)
        entity_loc_list.append(entity_loc)

    # print(sentence_list_train_idx)
    # print(entity_loc_list)

    # make w to i, i to w

    # make every sentences to 3d array [[[], [], [], ... ], [[],[],...[]], ..] -> 1 * sentence * word
    # ( use the maximum len, if it is shorter than the maximum len, it should use the len of word list )
    # anyway it should contain the entity location data how ? idk

    #

    #


if __name__ == '__main__':
    main()
    # PARSER = argparse.ArgumentParser(description='real-time us price crawler')
    # PARSER.add_argument('-c', '--cfg', required=True, default='', metavar='CFG', help='set config file')
    #
    # args = PARSER.parse_args()
    # config = configparser.ConfigParser(os.environ)
    # config.read(args.cfg)
    # main(args)
