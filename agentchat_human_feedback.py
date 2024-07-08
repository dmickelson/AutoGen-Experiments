"""
This script sets up an AutoGen chat environment with an assistant agent and a user proxy agent.
It demonstrates how to create a conversation with human feedback and log the conversation history.

The script does the following:
1. Configures an AssistantAgent with specific LLM settings.
2. Sets up a UserProxyAgent that always requires human input.
3. Initiates a chat to solve a given problem about planet temperatures.
4. Logs the conversation history to a JSON file.

Dependencies:
    - autogen
    - json

Output:
    - Initiates an interactive chat session.
    - Saves the conversation history to 'conversations.json'.
"""

import autogen
import json

config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST")


# Create assistant agent
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={
        "seed": 43,
        "config_list": config_list,
        "temperature": 0.1
    }
)

# Create user proxy agent
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    system_message="A Human input",
    human_input_mode="ALWAYS",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get(
        "content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "chat_dir",
        "use_docker": True
    }
)

# The purpose of the following line is to log the conversation history
autogen.ChatCompletion.start_logging()

problem_to_solve = """
Find the temperature of all of the planets of the solar system.
"""

user_proxy.initiate_chat(
    recipient=assistant,
    message=problem_to_solve
)
json.dump(autogen.ChatCompletion.logged_history,
          open("conversations.json", "w"), indent=4)
