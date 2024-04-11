# Sociable Agents
The goal of this project is to ultimately create sociable agents - that is agentive structures that can behave like humans. 
Modeling human-like interactions between agents in multiagent systems is emerging as a popular application for Large Language Models (LLM) and Artificial Intelligence (AI). As we are moving towards simulating human behavior in simulations with the help of generative artificial intelligence (genAI), we must consider key human and life-like factors into our modeling process. This project focuses primarily on the question whether generative multiagent systems can achieve a level of self-organization that solves problems in stagnating human-like systems, pulling wisdom from concepts in systems theory, reinforcement learning (RL), machine learning (ML), linguistics, psychology, and network science. Our hypothesis is that smart multiagent systems can simulate human-like scenarios and can find human-like or more optimal solutions than humans have found for the problems or dilemmas they will encounter.

## Systems Theory
Wherever we go, we are surrounded by systems. Systems Theory aims to describe how structures emerge, in which many people are at play to form structures larger than the individual parts. In this, interdisciplinary concepts are analyzed to understand synergy and emergent behavior.

Since we are exploring how certain system scenarios can be modeled through AI, we are going to go a bit more into the exploration of common systems theory concepts. 

### Methodologies
Systems Thinking aims at getting an overview of an issue through looking at it as an emergent phenomena that is based on the interconnections between its parts and the purpose of the system. It also models the dynamics of a system, i.e. how a system changes over time, to accommodate for it. The idea of feedback loops in systems is that they are generally time-invariant.

### Archetypes 
Here are the archetypes that we will attempt to fix through our simulation. 
1. Tragedy of Commons.
2. Fixes that fail.

There are two questions that we will explore here: Given our architecture, can we: a) end up in such a structure and b) if we do, escape it through reinforcement learning? What changed?

## The Environments/Scenarios
Eventually, we want the environments to be self-makeable, meaning that every person can make their own environment as they'd like to see how agents would perform with different characteristics.

### Tragedy of Commons
This will be one of the system archetypes we will explore.


### Fixes That Fail

## Characteristics of Agents
This is about modeling the characteristics of agents. 

We are looking at the different personality tests to synthesize the personality traits as well as some other sources that explain the interlink between traits and behaviors. 
Find one [here][https://opentextbc.ca/introductiontopsychology/chapter/11-1-personality-and-behavior-approaches-and-measurement/#:~:text=Personality%20traits%20such%20as%20introversion,report%20about%20their%20own%20characteristics.].

## The Science behind Networks
Networks and Graphs' goals is to understand complex systems through mapping the interactions between components.
> A network is a catalog of a system's components often called nodes or vertices and the direct interactions between them, called link or edges. - Networkscience Book (Barabasi)
In our networks, we'll have two main parameters: 
- Number of nodes (N) (Graph Theory: Vertex) representing the # of components in the system. We call this the size of the network.
- Number of links (L) (Graph Theory: Edge) represent the total number of interactions between the nodes. These can be *directed* or *undirected*. 

For this project, we are interested in linking individuals (agents) with each other; a couple of specific examples include: organization/professional network, friendship network, sexual network, acquaintance network, etc.


## Flask Server

To run your flask application, run the following commands in the terminal: 
```bash
export FLASK_APP=file_name
```
Then: 
```bash
export FLASK_ENV=development
```
and finally to run: 
```bash
flask run 
```