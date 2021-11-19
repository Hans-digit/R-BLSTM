from nltk.parse import CoreNLPParser
from nltk.parse.corenlp import CoreNLPDependencyParser
pos_tagger = CoreNLPParser(url='http://localhost:9000', tagtype='pos')


