from agentdesign import Agent
from agentsetup import agent_creation
from autogen import GroupChat, GroupChatManager
import numpy as np
import os
from api_keys import open_ai_key
os.environ['OPENAI_API_KEY'] = open_ai_key

# ---------- SETTING VARIABLES ---------- 

# description_themes = "" # we can automate the description that we get through chatGPT
agents = {}
num_agents = 10
max_rounds = 10
context = f"""
You are all friends and know each other already. 
The purpose of this conversation is for you to talk about your movie preferences and pick one of the available movies. Everyone has their own preference. 
There is {max_rounds} turns of talking. Your goal is to make a decision. 
If you make a decision, the last speaker finishes with: dec is: __decision___. 
"""

# ------- INITIAL SETUP --------

agents = agent_creation(agent_number=num_agents) 

# Manager Creation 
manager = Agent("Manager")

# ----------------- CUSTOM SPEAKER FUNCTION / SPEAKING ORDER -----------------------
# Custom selecting next speaker function! 
# def test(last_speaker: Agent, selector: ConversableAgent) -> Agent:
#     return last_speaker

# ----------------- (TEST) INITIATING CONVERSATION ---------------------
def communication(agents): # This mgiht heave to be integrated into the environment? What is the action space of the environment?
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
    print(chat_result) # this is going to print out the groupchat.
    print(chat_result.summary) # prints the summary of the chat
    
    return chat_result.summary