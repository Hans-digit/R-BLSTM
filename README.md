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


