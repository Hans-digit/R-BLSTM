from nltk.parse import CoreNLPParser
from nltk.parse.corenlp import CoreNLPDependencyParser
dep_parser = CoreNLPDependencyParser(url = 'http://localhost:9000')

class StanfordDependencyParser():
    def get_relationship_feature(self, sentence, e1, e2):
        parses = dep_parser.parse(sentence.split())
        dic = [parse for parse in parses][0]
        nodes = dic.nodes
        print(nodes)
        feature_list = self._relationship_feature(nodes, e1, e2)
        return feature_list

    def _relationship_feature(self, nodes, e1, e2):
        relative_root = self._relative_root(nodes)
        relative_e1_feature = self._relative_feature(nodes, e1, 'e1')
        relative_e2_feature = self._relative_feature(nodes, e2, 'e2')
        dep_feature = self._dep_feature(nodes)
        pf_feature_1 = self._pf_feature(nodes, e1)
        pf_feature_2 = self._pf_feature(nodes, e2)

        return [relative_root, relative_e1_feature, relative_e2_feature, dep_feature,
                pf_feature_1, pf_feature_2]

    def _relative_root(self, nodes):
        for node_index in range(len(nodes)):
            node = nodes[node_index]
            if node['rel'] == 'ROOT':
                root = node
                break
        relative_root_list = []
        for node_index in range(len(nodes)):
            node = nodes[node_index]
            if node_index == 0:
                pass
            elif node['head'] == root['address']:
                relative_root_list.append('r_c')
            elif node['rel'] == 'ROOT':
                relative_root_list.append('r_r')
            else:
                relative_root_list.append('r_o')

        return relative_root_list


    def _relative_feature(self, nodes, e1, feature_name):
        for node_index in range(len(nodes)):
            node = nodes[node_index]
            if node['word'] == e1:
                feature_node = node
                break
        relative_feature_list = []
        for node_index in range(len(nodes)):
            node = nodes[node_index]
            if node_index == 0:
                pass
            elif node['head'] == feature_node['address']:
                relative_feature_list.append(f'{feature_name}_c')
            elif node['address'] == feature_node['address']:
                relative_feature_list.append(f'{feature_name}_e')
            elif feature_node['head'] == node['address']:
                relative_feature_list.append(f'{feature_name}_p')
            else:
                relative_feature_list.append(f'{feature_name}_o')
        return relative_feature_list


    def _dep_feature(self, nodes):
        dep_list = []
        for node_index in range(len(nodes)):
            node = nodes[node_index]
            if node_index == 0:
                pass
            else:
                dep_list.append(node['rel'])
        return dep_list

    def _pf_feature(self, nodes, e1):
        for node_index in range(len(nodes)):
            node = nodes[node_index]
            if node['word'] == e1:
                e1_index = node_index - 1
                break
        pf_list = [i - e1_index for i in range(len(nodes) - 1)]
        return pf_list

if __name__=="__main__":
    sdp = StanfordDependencyParser()
    parsed_list = sdp.get_relationship_feature('The cat sat on the mat', 'cat','mat')
    print(parsed_list)
    parsed_list = sdp.get_relationship_feature('''Bell, based in Los Angeles, makes and distributes electronic, computer and building products.''', 'computer','building')
    print(parsed_list)