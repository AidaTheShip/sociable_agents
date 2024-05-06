import networkx as nx

class SocialNetwork:
    def __init__(self, agents):
        self.participants = agents
        self.network = nx.Graph()
        for src in self.participants:
            for dst in self.participants:
                if src != dst:
                    self.network.add_edge(src, dst, weight=0)

    def update_connection(self, connection, strength):
        src, dst = connection
        self.network[src][dst]['weight'] = strength