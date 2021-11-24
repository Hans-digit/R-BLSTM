import csv
import argparse, configparser
import os
from PARSER import stanford_parser

class RelExtractor():

    # def __init__(self):
    @staticmethod
    def read_train_data():
        with open('./data/train/dataset_csv.csv', 'r', newline='\n') as sentence_csv:
            csv_reader = csv.reader(sentence_csv, delimiter='|')
            sentence_list_train = [i[0] for i in csv_reader]
            ans_list_train = [i[1] for i in csv_reader]
        return sentence_list_train, ans_list_train

    @staticmethod
    def read_test_data():
        with open('./data/test/dataset_csv.csv', 'r', newline='\n') as sentence_csv:
            csv_reader = csv.reader(sentence_csv, delimiter='|')
            sentence_list_test = [i[0] for i in csv_reader]
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
        result_sentence = result_sentence + [len(word_to_index)] * (len(max_sentence_len) - len(result_sentence))
        return result_sentence







def main(args):
    # load sentence list
    rel_exctractor = RelExtractor()
    sentence_list_train, ans_list_train = rel_exctractor.read_train_data()
    word_to_index, index_to_word = rel_exctractor.make_w_i_dictionary()
    sentence_list_train_idx = []
    for sentence_train in sentence_list_train:
        result_sentence = rel_exctractor.setence_to_list(sentence_train, word_to_index, 85)
        print(result_sentence)



    # make w to i, i to w

    # make every sentences to 3d array [[[], [], [], ... ], [[],[],...[]], ..] -> 1 * sentence * word
    # ( use the maximum len, if it is shorter than the maximum len, it should use the len of word list )
    # anyway it should contain the entity location data how ? idk

    #


    #





if __name__ == '__main__':
    print(1)
    # PARSER = argparse.ArgumentParser(description='real-time us price crawler')
    # PARSER.add_argument('-c', '--cfg', required=True, default='', metavar='CFG', help='set config file')
    #
    # args = PARSER.parse_args()
    # config = configparser.ConfigParser(os.environ)
    # config.read(args.cfg)
    # main(args)
