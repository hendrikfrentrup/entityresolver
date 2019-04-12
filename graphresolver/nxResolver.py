import csv
import networkx as nx


class nxResolver:

    def __init__(self):
        self.G = nx.Graph()

    def get_graph_stats(self):
        n = self.G.number_of_nodes()
        e = self.G.number_of_edges()
        return n, e

    def create_nodes_from_dict(self, record_dict):
        n_nodes=0
        for i, record in record_dict.items():
            self.G.add_node(i,  ip=record['ip'], 
                                mac=record['mac'], 
                                hostname=record['hostname'], 
                                serial_no=record['serial_no'],
                                source=record['source']
                            )
            n_nodes+=1
        return f"{n_nodes} nodes added to graph."


    def generate_edges(self):
        # make sure there are nodes loaded
        g=self.G
        n_comparisons=0
        n_edges=0

        for i in g.nodes:
            # TODO: only need to count from r-t, halves the loop
            for j in g.nodes:
                n_comparisons+=1
                edge_flag=False
                if i!=j:
                    #TODO: iterate through columns to match
                    if (g.node[i]['ip']!='') & (g.node[i]['ip']==g.node[j]['ip']):
                        edge_flag=True
                    elif (g.node[i]['mac']!='') & (g.node[i]['mac']==g.node[j]['mac']):
                        edge_flag=True
                    elif (g.node[i]['hostname']!='') & (g.node[i]['hostname']==g.node[j]['hostname']):
                        edge_flag=True
                    elif (g.node[i]['serial_no']!='') & (g.node[i]['serial_no']==g.node[j]['serial_no']):
                        edge_flag=True
                        
                    if edge_flag:
                        n_edges+=1
                        g.add_edge(i,j)
                        # TODO: add an edge type, e.g. ip-match/mac-match
        return f"{n_edges} edges created, out of a possible {n_comparisons}"

    # def compute_connComponents(self):
        
    def generate_conncomp_as_dict(self):
        # with open('mycsvfile.csv', 'wb') as f:
        id=0
        for cc in nx.connected_components(self.G):
            for n in cc:
                print(id,self.G.node[n])
            id+=1


def csv2dict(csv_file):
    out_dict={}
    with open(csv_file) as csv_records:
        reader = csv.DictReader(csv_records)
        for i,row in enumerate(reader):
            out_dict[i]=row
    return out_dict

def dict2csv(out_dict, out_file="resolved_records.csv"):
    with open(out_file, 'w') as csv_file:
        fieldnames = out_dict[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

