import autogen

import os
from dotenv import load_dotenv
import openai

load_dotenv()

def sky_color(color: str) -> str:
    return "The sky color is rainbow"

# Import the openai api key
config_list = autogen.config_list_from_models(model_list=["gpt-4", "gpt-3.5-turbo"])
openai.api_key = os.getenv("OPENAI_API_KEY")

llm_config={
    "functions": [
        {
            "name": "query_color_sky",
            "description": "Return the API query result from the function. The return value is a string.",
            "parameters": {
                "type": "object",
                "properties": {
                    "color": {
                        "type": "string",
                        "description": "The magical color of the sky.",
                    }
                },
                "required": ["query"],
            },
        }
    ],
    "seed": 44,
    "request_timeout": 120,
    "config_list": config_list,
    "temperature":0
}

chatbot = autogen.AssistantAgent(
    name="chatbot",
    system_message="Only use the functions you have been provided with. Do not ask user to perform other actions than executing the functions. Reply TERMINATE when the task is done.",
    llm_config=llm_config,
)

# the key in `function_map` should match the function name in "functions" above
# we register a class instance method directly
user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    max_consecutive_auto_reply=3,
    human_input_mode="NEVER",
    function_map={"query_color_sky": sky_color}, 
)

# start the conversation
user_proxy.initiate_chat(
    chatbot,
    message="Problem: Is the sky blue?",
)