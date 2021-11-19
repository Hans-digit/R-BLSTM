import torch
import time
import torch.nn.functional as F
import numpy as np

class BLSTM(torch.nn.Module):
    def __init__(self, config):
        super(BLSTM, self).__init__()
        self.config = config
        max_sentence_len = None
        pos_len = None
        ner_len = None
        wnsyn_len = None
        dep_len = None
        relative_dep_len1 = None
        relative_dep_len2 = None
        relative_dep_len3 = None

        #pf embedding
        self.embedding_pf1 = torch.nn.Embedding(max_sentence_len, 5)
        self.embedding_pf2 = torch.nn.Embedding(max_sentence_len, 5)
        #pos embedding
        self.embedding_pos = torch.nn.Embedding(pos_len, 20)
        #ner embedding
        self.embedding_ner = torch.nn.Embedding(ner_len, 20)
        #wnsyn embedding
        self.embedding_wnsyn = torch.nn.Embedding(wnsyn_len, 20)
        #dep embedding
        self.embedding_dep = torch.nn.Embedding(dep_len, 20)
        #relative dep embedding
        self.embedding_rel_dep1 = torch.nn.Embedding(relative_dep_len1, 10)
        self.embedding_rel_dep2 = torch.nn.Embedding(relative_dep_len2, 10)
        self.embedding_rel_dep3 = torch.nn.Embedding(relative_dep_len3, 10)

        '''
        The BLSTM layer contains 400 units for each
        direction, and MLP layer contains 1000 units.
        
        BLSTM layer depth unknown 
        '''
        input_size_len = None # text 길이 ; not in the paper
        hidden_size_unit = 400 # BLSTM layer unit 개수 ; in the paper
        num_layers = None # depth ; not in the paper
        self.BI_LSTM = torch.nn.LSTM(input_size = input_size_len,
                                     hidden_size = hidden_size_unit,
                                     num_layers = num_layers,
                                     bidrectional = True)

        #sentence 길이 짧을때 메꾸는법

        #이미 학습된 embedding 가중치 변화 없게

        #max pool 구현

        #max pool layer
        self.max_pool =

    def forward(self, context):
        # context.size = [sentence 개수, sentence 내부 단어 길이, word embedding 크기]





