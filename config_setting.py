from train import RelExtractor
from PARSER.stanford_parser import StanfordDependencyParser
from tqdm import tqdm

sentence_train, ans_train = RelExtractor.read_train_data()
sentence_test, ans_test = RelExtractor.read_test_data()
# sentence_train = [i.replace('<e1>',' ').replace('</e1>',' ').replace('<e2>',' ').replace('</e2>',' ') for i in sentence_train]
# sentence_test = [i.replace('<e1>',' ').replace('</e1>',' ').replace('<e2>',' ').replace('</e2>',' ') for i in sentence_test]

sentence_list = sentence_train + sentence_test
dep_parser = StanfordDependencyParser()
dep_set = set()
for sentence in tqdm(sentence_list):
    word_list, entity_loc = RelExtractor.preprocess_sentence_data(sentence)
    [r_rel, e1_rel, r2_rel, dep_rel, pf1, pf2] = dep_parser.get_relationship_feature(word_list, word_list[entity_loc[0]], word_list[entity_loc[2]])
    dep_set = dep_set.union(set(dep_rel))

print(dep_set)



