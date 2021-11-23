import csv
import argparse, configparser
import os


sentence_list = []
with open('./data/train/dataset_csv.csv', 'r', newline = '\n') as sentence_csv:
    csv_reader = csv.reader(sentence_csv, delimiter = '|')
    sentence_list_train = [i[0] for i in csv_reader]

class RelExtractor






def main(args)
    config = configparser.ConfigParser(os.environ)
    config.read(args.cfg)

    # load sentence list

    # make w to i, i to w

    # make every sentences to 3d array [[[], [], [], ... ], [[],[],...[]], ..] -> 1 * sentence * word
    # ( use the maximum len, if it is shorter than the maximum len, it should use the len of word list )
    # anyway it should contain the entity location data how ? idk

    #


    #





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='real-time us price crawler')
    parser.add_argument('-c', '--cfg', required=True, default='', metavar='CFG', help='set config file')

    args = parser.parse_args()
    config = configparser.ConfigParser(os.environ)
    config.read(args.cfg)
    main(args)
