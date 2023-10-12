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
        "temperature":0
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