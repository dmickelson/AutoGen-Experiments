"""
This script demonstrates how to set up an AutoGen chat environment with function calling capabilities,
specifically for solving mathematical problems using Wolfram Alpha.

The script does the following:
1. Configures an AssistantAgent with a function for querying Wolfram Alpha.
2. Sets up a UserProxyAgent with the ability to execute Wolfram Alpha queries.
3. Initiates a chat to solve a specific mathematical inequality problem.

Dependencies:
    - autogen
    - os
    - dotenv
    - openai
    - autogen.agentchat.contrib.math_user_proxy_agent.MathUserProxyAgent

Environment Variables:
    - OPENAI_API_KEY: Your OpenAI API key

Output:
    - Initiates a chat session to solve the given mathematical problem.
"""

import autogen
from autogen.agentchat.contrib.math_user_proxy_agent import MathUserProxyAgent

import os
from dotenv import load_dotenv
import openai

load_dotenv()

# Import the openai api key
config_list = autogen.config_list_from_models(
    model_list=["gpt-4", "gpt-3.5-turbo"])
openai.api_key = os.getenv("OPENAI_API_KEY")

llm_config = {
    "functions": [
        {
            "name": "query_wolfram",
            "description": "Return the API query result from the Wolfram Alpha. the ruturn is a tuple of (result, is_success).",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The Wolfram Alpha code to be executed.",
                    }
                },
                "required": ["query"],
            },
        }
    ],
    "seed": 44,
    "request_timeout": 120,
    "config_list": config_list,
    "temperature": 0
}

chatbot = autogen.AssistantAgent(
    name="chatbot",
    system_message="Only use the functions you have been provided with. Do not ask user to perform other actions than executing the functions. Reply TERMINATE when the task is done.",
    llm_config=llm_config,
)

# the key in `function_map` should match the function name in "functions" above
# we register a class instance method directly
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    max_consecutive_auto_reply=2,
    human_input_mode="NEVER",
    function_map={
        "query_wolfram": MathUserProxyAgent().execute_one_wolfram_query},
)

# start the conversation
user_proxy.initiate_chat(
    chatbot,
    message="Problem: Find all $x$ that satisfy the inequality $(2x+10)(x+3)<(3x+9)(x+8)$. Express your answer in interval notation.",
)
