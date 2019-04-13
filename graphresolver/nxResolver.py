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

    @staticmethod
    def tag_node_as_dict(entity_id, node_dict):
        res={'entity_id':entity_id }
        for k in node_dict.keys():
            res[k]=node_dict[k]
        return res

    def generate_conncomponents(self):
        self.tagged_records=[]
        entity_id=0
        for cc in nx.connected_components(self.G):
            for n in cc:
                self.tagged_records.append(self.tag_node_as_dict(entity_id,self.G.node[n]))
            entity_id+=1
        return f"{len(self.tagged_records)} records tagged with {entity_id-1} entities"

    # a lot of repeated code, should be consolidated
    def merge_records(self):
        self.consolidated_entities=[]
        entity_id=0
        keys=self.G.node[0].keys()
        for cc in nx.connected_components(self.G):
            merge={"entity_id":entity_id}
            for k in keys:
                merge[k]=",".join([self.G.node[n][k] for n in cc])

            self.consolidated_entities.append(self.tag_node_as_dict(entity_id, merge))
            entity_id+=1
        return f"merged {self.G.number_of_nodes()} records into {len(self.consolidated_entities)} merged entities"        


# to be deleted as in Data_CSV
def csv2dict(csv_file):
    out_dict={}
    with open(csv_file) as csv_records:
        reader = csv.DictReader(csv_records)
        for i,row in enumerate(reader):
            out_dict[i]=row
    return out_dict

# to be moved to Data_CSV
def records2csv(records, out_file="resolved_records.csv"):
    with open(out_file, 'w') as csv_file:
        fieldnames = records[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for r in records:
            writer.writerow(r)

