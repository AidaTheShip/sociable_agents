# Sociable Agents
The goal of this project is to train Artificial Intelligence Agents to solve problems, particularly system problems. 
Modeling human-like interactions between agents in multiagent systems is emerging as a popular application for Large Language Models (LLM) and Artificial Intelligence (AI). As we are moving towards simulating human behavior in simulations with the help of generative artificial intelligence (genAI), one application is using these simulations to mimic human behavior but training agents to learn in a low-risk environment.  This project focuses primarily on the question whether generative multiagent systems can achieve a level of self-organization that solves problems in stagnating human-like systems, pulling wisdom from concepts in systems theory, reinforcement learning (RL), machine learning (ML), linguistics, psychology, and network science. Our hypothesis is that smart multiagent systems can simulate human-like scenarios and can find human-like or more optimal solutions than humans have found for the problems or dilemmas they will encounter.

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

## Well-Being 
For simplicity, we are going to encode the well-being of each agent as a vector, giving us a metric for their emotional well-being. This will generally be about how well they are feeling about their **social circumstances**, **self/personal circumstances**, and **situational/future circumstances/purpose**. (the latter one I'm not entirely sure yet)

### Social Well-being
Social well-being will be encoded mathematically based on the characteristics of the agent. This means that having a large network of friends and high-frequency interactions with them will generally make agents with higher extroversion more content. On the other hand if you have an agent high on introversion, too much interaction with their network compared to time spend alone, will make them less content. 

Additionally, we will also encode the level of "deepness" as a weight between the agents' relationships with each other. Depth of relationships generally increases the well-being of agents. 

## The Science behind Networks
Networks and Graphs' goals is to understand complex systems through mapping the interactions between components.
> A network is a catalog of a system's components often called nodes or vertices and the direct interactions between them, called link or edges. - Networkscience Book (Barabasi)
In our networks, we'll have two main parameters: 
- Number of nodes (N) (Graph Theory: Vertex) representing the # of components in the system. We call this the size of the network.
- Number of links (L) (Graph Theory: Edge) represent the total number of interactions between the nodes. These can be *directed* or *undirected*. 

For this project, we are interested in linking individuals (agents) with each other; a couple of specific examples include: organization/professional network, friendship network, sexual network, acquaintance network, etc.. Social networks will therefore be increasingly important.


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

## The simplest prototype
We are going to initiate N people. 
The actions the people can take is either a) talk to others or not talk to others. 
After each step, each agents gets an interaction score that will influence their social network + well-being. 
Based on the score it got, it will learn to optimize for well-being. 

---- This is not the final goal of the project but it is a first, tangible, and deliverable result. -----

Implementation Steps to take: 
1. Initialize Basic Environment with Action space. 
2. Create mapping between behavior and characteristics/needs. Pair social network to characteristics.
3. Run reinforcement learning algorithm. 


## Reinforcement Learning
We are going to start with a simpler version of the reinforcement learning algorithm, in which teh agents are not going to communicate through LLMs. 



### Policy Network 
There are different types of reinforcement learning. In our particular case, we are going to use a Policy based approach. This means that the policy determines the behavior of the agent. The agent learns the policy or more so learns the behavior that it is supposed to enact. It is a strategy that the agent follows to decide its actions at each state of the environment. Our neural network approximates this policy function. It maps observed states of the environment to actions that the agent should take. The goal is to learn a policy that maximizes the cumulative reward the agent receives over time.

How does it work? 
- Input: State of the environment, e.g. through a vector representing the current state of agent.
- Output: Direct action values, which can be real numbers. 
- Layers: several layers of neurons that help in extracting features and nonlinear relationships from the state inputs

During our reinforcement learning, we are going to train the policy network. 

So how do you train the policy network? 
These methods directly optimize the policy by calculating the gradient of the expected return (cumulative reward) with respect to the network parameters and then updating the parameters in the direction that maximizes the return.
