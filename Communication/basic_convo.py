from agent_creation import Agent, generate_convo_context
from autogen import GroupChat, GroupChatManager
import numpy as np
import os
from LLM_setup import open_ai_key
os.environ['OPENAI_API_KEY'] = open_ai_key

# ---------- SETTING VARIABLES ---------- 
names = np.array(["Bob", "Alice", "Diana", "Frank"]) # three agents.
# description_themes = "" # we can automate the description that we get through chatGPT
agents = {}
max_rounds = 10
context = f"""
You are all friends and know each other already. 
The purpose of this conversation is for you to talk about your movie preferences and pick one of the available movies. Everyone has their own preference. 
There is {max_rounds} turns of talking. Your goal is to make a decision. 
If you make a decision, the last speaker finishes with: dec is: __decision___. 
"""

# ----------------------- CREATING AGENTS ---------------------------
def agent_creation(names=names):
# For loop for instantiating x people
    for name in names: 
        agents[name] = Agent(name)

# Creating instances of agents
agent_creation()

# Manager Creation 
manager = Agent("Manager")

# ----------------- CUSTOM SPEAKER FUNCTION / SPEAKING ORDER -----------------------
def select_next_speaker(current_speaker:Agent) -> Agent: 
    pass

# ----------------- (TEST) INITIATING CONVERSATION ---------------------
# Custom selecting next speaker function! 
# def test(last_speaker: Agent, selector: ConversableAgent) -> Agent:
#     return last_speaker

# print([agents[name].name for name in agents])
group_chat = GroupChat(
    agents= [agents[name].agent for name in agents],
    messages=[context],
    max_round=max_rounds,
    speaker_selection_method="random"
)


group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    system_message=context,
    llm_config={"config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]},
)

print(manager.agent.system_message)


# print(group_chat.agents)
# first_speaker = agents['Alice']
chat_result = manager.agent.initiate_chat(
    group_chat_manager,
    message=context,
    summary_method="reflection_with_llm",
)

# print(agents['Alice'].agent.chat_messages)

print(chat_result.summary)

# ------------- MDP / REINFORCEMENT LEARNING -------------------
# Initial parameters
lr = 0.1 
discount_factor = 0.99
epsilon = 0.1 # exploration rate
state_size = 10 # What are the states that you can be in? Think a bit more on this because I think it would be continuous in this particular scenario.
action_size = 5 # this is the action size -> discrete in this sense 
total_episodes = 100

def states(): 
    pass

def choose_action(): # this is selecting the next speaker? 
    pass
    
def reward():
    pass

# Simulation - ENV setup / structure
# for episode in range(total_episodes):
    
#     # [...] Something has to go here.
#     done = False
#     while not done: 
#         action = choose_action()
#         next_state, reward, done = _ 
#         # best_next_action = np.argmax()
#         state = next_state 
        
#         # have to figure out the state space, action space, and so on. 
        
        