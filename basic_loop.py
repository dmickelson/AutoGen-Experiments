"""
This script sets up a looping chat environment in AutoGen, allowing for continuous interaction
between an assistant and a user proxy.

The script does the following:
1. Configures an AssistantAgent with specific LLM settings.
2. Sets up a UserProxyAgent with specific settings for human input and code execution.
3. Initiates a continuous chat loop, allowing for ongoing interaction.

Dependencies:
    - autogen
    - os
    - dotenv
    - openai

Environment Variables:
    - OPENAI_API_KEY: Your OpenAI API key

Output:
    - Initiates an interactive, continuous chat session between the user and the assistant.
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
    system_message="A Human input",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get(
        "content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "coding",
        "use_docker": True
    }
)

# Start a loop for chat
first_message = True
while True:
    if first_message:
        user_input = input("Enter your message: ")
        user_proxy.initiate_chat(
            recipient=assistant,
            message=f"""{user_input}"""
        )
        first_message = False
    else:
        user_input = input("Enter your message: ")
        user_proxy.send(
            recipient=assistant,
            message=f"""{user_input}"""
        )
