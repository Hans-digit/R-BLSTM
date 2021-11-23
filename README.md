## R-BLSTM
Unoffical implementation of "Bidirectional Long Short-Term Memory Networks for Relation Classification"(2015)

### How to use stanford parser 
ref: https://stackoverflow.com/questions/13883277/how-to-use-stanford-parser-in-nltk-using-python
1. update nltk (make sure >= 3.3)

```pip3 install -u nltk```

2. download necessary CoreNLP packages 

```
cd ~ 
wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip
unzip stanford-corenlp-full-2018-02-27.zip
cd stanford-corenlp-full-2018-02-27 
```

3. still in the stanford-corenlp-full-2018-02-27 directory, start the server 

```
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer \
-preload tokenize,ssplit,pos,lemma,ner,parse,depparse \
-status_port 9000 -port 9000 -timeout 15000 & 
```

4. then in the python, 

```
# Neural Dependency Parser 

from nltk.parse.corenlp import CoreNLPDependencyParser
dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')
parses = dep_parser.parse('What is the airspeed of an unladen swallow ?'.split())
[[(governor, dep, dependent) for governor, dep, dependent in parse.triples()] for parse in parses]
=> [[(('What', 'WP'), 'cop', ('is', 'VBZ')), (('What', 'WP'), 'nsubj', ('airspeed', 'NN')), (('airspeed', 'NN'), 'det', ('the', 'DT')), (('airspeed', 'NN'), 'nmod', ('swallow', 'VB')), (('swallow', 'VB'), 'case', ('of', 'IN')), (('swallow', 'VB'), 'det', ('an', 'DT')), (('swallow', 'VB'), 'amod', ('unladen', 'JJ')), (('What', 'WP'), 'punct', ('?', '.'))]]
```

we made stanford_parser python file, so 
1. turn on the server 
2. input (sentence, e1, e2)
3. output (relation feature, entity 1 feature, entity 2 feature, dep feature, pf feature)

result like
   
[['r_o', 'r_c', 'r_r', 'r_o', 'r_o', 'r_c'], ['e1_c', 'e1_e', 'e1_p', 'e1_o', 'e1_o', 'e1_o'], ['e2_o', 'e2_o', 'e2_p', 'e2_c', 'e2_c', 'e2_e'], ['det', 'nsubj', 'ROOT', 'case', 'det', 'nmod'], [-1, 0, 1, 2, 3, 4], [-5, -4, -3, -2, -1, 0]]

### word embedding 
all word embeddings include padding index at the last ( index number 23514 )

- Turian et al(2010) (dimension of word embedding is 50)
- Link : http://metaoptimize.s3.amazonaws.com/hlbl-embeddings-ACL2010/hlbl-embeddings-scaled.EMBEDDING_SIZE=50.txt.gz
- original embedding file is in './model/hlbl-embeddings-scaled.EMBEDDING_SIZE=50.txt'
- modified embedding layer binary is in './model/turian_50.bin'
  
- Jeffrey Pennington et al (2014) (dimension of word embedding is 100)
- Link : http://nlp.stanford.edu/data/glove.6B.zip
- original embedding file is in './model/glove.6B.100d.txt'
- modified embedding layer binary is in './model/pennington_100.bin'

### Dependecy parser 
Link 
- 1. https://downloads.cs.stanford.edu/nlp/software/dependencies_manual.pdf ( list of all dep ) 
- 2. https://universaldependencies.org/u/dep/
    
### Need data 
- wordnet hypernym data (WNSYN)
- NER ( use by ourself )
- POS ( use by ourself )
- PF 
- WF ( word ) 
- DEP ( dep ) 
- RELATIVE-DEP ( root relative data, relative entity1 feature, relatvie entity2 feature ) 

NOT USED DATA : root relative data, relative entity feature, 

### paper should be read 
MVRNN - socher et al (2012) ( link : https://aclanthology.org/D12-1110.pdf ) 
- Relation Classification via Convolutional Deep Neural Network. In Proceedings of the 25th International Conference on Computational Linguistics, Zeng et al (2014)
- Link : https://aclanthology.org/C14-1220.pdf



### Need to do 
1. check how many word hypernyms are in our word list ( ./word/word_list.csv )
   우리가 가진 단어들에서 얼마나 많은 상위어가 있는지 확인해보세요 
2. check how many pos tags are in our sentneces 
   우리가 가진 문장들에서 얼마나 많은 pos tagger가 나오는지 확인 해 보세요 
3. check how many dep tag list in our sentences 
   우리가 가진 문장들에서 얼마나 많은 dep tagger가 나오는지 확인 해 보세요 
4. find a nice ner tagger, if you can, make the tagger method 
좋은 ner 태거를 찾아보세요, 만약 당신이 할 수 있다면, 그것을 함수로 만들어서 우리가 잘 쓸수 있게 해주세요
   
이것을 하는 이유: 
우리가 임베딩 행렬을 만들기 위해서는, 단어들의 집합인 사전을 가지고 있어야 합니다. 
사전의 차원에 맞게 임베딩 행렬을 만들게 됩니다. 
이 모델에서는 상위어, pos, dep 가 마치 하나하나의 단어처럼 취급됩니다. 
따라서 얼마나 많은 상위어, pos, dep 가 있는지 확인하는 작업이 필요하다고 여겨집니다. 
   
