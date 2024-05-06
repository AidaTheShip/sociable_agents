import networkx as nx
from pyvis.network import Network

# Defining the Social Network structure
import copy 
class SocialNetwork:
  def __init__(self, agents):
      self.participants = agents
      self.network = nx.Graph()
      self.history = [] # to store the changes in the network

  def update_connection(self, connection, strength):
    src, dst = connection
    strength_before = self.network[src][dst]['weight']
    self.network[src][dst]['weight'] = strength
    self.log_change(src, dst, strength_before, strength) # this is just for logging the change in strength

  def log_change(self, src, dst,before, weight):
    self.history.append((src, dst,before, weight))

  def snapshot(self):
    # Taking a snapshot of the ENTIRE NETWORK
    return copy.deepcopy(self.network)

  def visualize(self, spec=None):
    nt = Network(notebook=True)
    nt.from_nx(self.network)
    # Spec is in case we want to mass produce htmls lol
    if spec:
      nt.show(f"Network{spec}.html")
    else: 
      nt.show(f"Network.html")
      