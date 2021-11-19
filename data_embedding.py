import nltk
import csv
#%%
word_set = set()
with open('./data/train/dataset_csv.csv', 'r') as csv_file :
    reader = csv.reader(csv_file, delimiter = '|')
    for _ in reader:
        sentence = _[0].replace('<e1>','').replace('</e1>','').replace('<e2>','').replace('</e2>','').lower()
        word_set_temp = set(nltk.word_tokenize(sentence))
        word_set = word_set.union(word_set_temp)

with open('./data/test/dataset_csv.csv', 'r') as csv_file :
    reader = csv.reader(csv_file, delimiter = '|')
    for _ in reader:
        sentence = _[0].replace('<e1>','').replace('</e1>','').replace('<e2>','').replace('</e2>','').lower()
        word_set_temp = set(nltk.word_tokenize(sentence))
        word_set = word_set.union(word_set_temp)
#%%
print(word_set)
#%%
print(len(word_set))
#%%
from torch  import nn
#%%
rnn = nn.LSTM(10, 20, 2)
input = torch.randn(5, 3, 10)
# h0 = torch.randn(2, 3, 20)
# c0 = torch.randn(2, 3, 20)
output = rnn(input)
#%%
print(input)
#%%
print(output[0].size())
#%%

#%%
import bcolz
import numpy as np
import pickle
#%%
words = []
idx = 0
word2idx = {}
vectors = bcolz.carray(np.zeros(1), rootdir=f'./model/6B.100.dat', mode='w')

with open(f'./model/glove.6B.100d.txt', 'rb') as f:
    for l in f:
        line = l.decode().split()
        word = line[0]
        words.append(word)
        word2idx[word] = idx
        idx += 1
        vect = np.array(line[1:]).astype(np.float)
        vectors.append(vect)
#%%
print(len(vectors[1:]))
#%%
vectors = bcolz.carray(vectors[1:].reshape((400000, 100)), rootdir=f'./model/6B.100.dat', mode='w')
vectors.flush()
pickle.dump(words, open(f'./model/6B.100_words.pkl', 'wb'))
pickle.dump(word2idx, open(f'./model/6B.100_idx.pkl', 'wb'))
#%%
vectors = bcolz.carray(vectors[1:].reshape((246122, 50)), rootdir=f'./model/turian.50.dat', mode='w')
vectors.flush()
pickle.dump(words, open(f'./model/turian.50_words.pkl', 'wb'))
pickle.dump(word2idx, open(f'./model/turian.50_idx.pkl', 'wb'))
#%%
vectors = bcolz.open(f'./model/6B.100.dat')[:]
words = pickle.load(open(f'./model/6B.100_words.pkl', 'rb'))
word2idx = pickle.load(open(f'./model/6B.100_idx.pkl', 'rb'))
glove = {w: vectors[word2idx[w]] for w in words}
#%%
vectors = bcolz.open(f'./model/turian.50.dat')[:]
words = pickle.load(open(f'./model/turian.50_words.pkl', 'rb'))
word2idx = pickle.load(open(f'./model/turian.50_idx.pkl', 'rb'))
glove = {w: vectors[word2idx[w]] for w in words}
#%%
embedding_1 = torch.nn.Embedding(23514, 50)
#%%
embedding_1.load_state_dict(torch.load('./model/turian_50.bin'))
#%%
target_vocab = list(word_set)

#%%
matrix_len = len(target_vocab)
weights_matrix = np.zeros((matrix_len+1, 100))
words_found = 0

for i, word in enumerate(target_vocab):
    try:
        weights_matrix[i] = glove[word]
        words_found += 1
    except KeyError:
        weights_matrix[i] = glove['*UNKNOWN*']
#%%
matrix_len = len(target_vocab)
weights_matrix = np.zeros((matrix_len+1, 100))
words_found = 0

for i, word in enumerate(target_vocab):
    try:
        weights_matrix[i] = glove[word]
        words_found += 1
    except KeyError:
        weights_matrix[i] = np.random.normal(scale=0.6, size=(100, ))
#%%
weights_matrix[matrix_len] = [0]*100
#%%
weights_matrix = np.zeros((matrix_len, 50))
#%%
print(len(target_vocab))
#%%
print(weights_matrix)
#%%
print(weights_matrix.size)
#%%
def create_emb_layer(weights_matrix, non_trainable=False):
    num_embeddings, embedding_dim = weights_matrix.size()
    emb_layer = nn.Embedding(num_embeddings, embedding_dim)
    emb_layer.load_state_dict({'weight': weights_matrix})
    if non_trainable:
        emb_layer.weight.requires_grad = False

    return emb_layer, num_embeddings, embedding_dim
#%%
emb_layer = nn.Embedding(len(target_vocab)+1, 100)
#%%
print(emb_layer)
#%%
print(weights_matrix)
#%%
weights_matrix = torch.FloatTensor(weights_matrix)
#%%
print(emb_layer)
#%%
emb_layer.load_state_dict({'weight':weights_matrix})
#%%
print(emb_layer.weight[0])
#%%
torch.save(emb_layer.state_dict(), './model/pennington_100.bin')
#%%
with open('./word/word_list.csv', 'w') as word_csv:
    writer = csv.writer(word_csv, lineterminator = '\n')
    for word in target_vocab:
        writer.writerow([word])
#%%
print(emb_layer.weight[0][1])
#%%
import torch
#%%
embedding = torch.nn.Embedding(4,2, padding_idx = 3)
#%%
print(embedding.weight)
#%%
embedding = torch.nn.Embedding(len(target_vocab)+1, 100, padding_idx = len(target_vocab))
#%%
embedding.load_state_dict(torch.load('./model/pennington_100.bin'))
#%%
print(embedding.weight[23513])