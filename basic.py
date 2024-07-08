"""
This script provides a basic setup for an AutoGen chat environment.
It demonstrates how to create a simple conversation between an assistant and a user proxy.

The script does the following:
1. Configures an AssistantAgent with specific LLM settings.
2. Sets up a UserProxyAgent with code execution capabilities.
3. Initiates a chat with a specific task related to stock price charting.

Dependencies:
    - autogen
    - os
    - dotenv
    - openai

Environment Variables:
    - OPENAI_API_KEY: Your OpenAI API key

Output:
    - Initiates a chat session to plot a chart of specified stock prices.
"""
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import os
from dotenv import load_dotenv
import openai

load_dotenv()

# Import the openai api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create assistant agent
assistant = AssistantAgent(
    name="assistant",
    llm_config={
        "seed": 42,
        "config_list": config_list,
        "temperature": 0
    }
)

# Create user proxy agent
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config={"work_dir": "coding",
                           "use_docker": True})

# Start the conversation
user_proxy.initiate_chat(
    assistant, message="Plot a chart of NVDA, AAPL and TESLA stock price change YTD.")
