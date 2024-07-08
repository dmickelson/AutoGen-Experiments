# AutoGen Experiments

AutoGen is a framework that enables the development of LLM applications using multiple agents that can converse with each other to solve tasks.

Examples of using AutoGen agents!

![autogen_agentchat](Autogen.png)

## File Overview

1. agentchat_human_feedback.py: Demonstrates a chat environment with human feedback and conversation logging.
2. agentchat_simple_function_call.py: Shows how to set up function calling capabilities, specifically for mathematical queries using Wolfram Alpha.
3. agentchat_simple_local_function_call.py: Illustrates how to integrate custom local functions into the chat environment.
4. basic.py: Provides a basic setup for an AutoGen chat environment, focusing on stock price charting.
5. basic_loop.py: Sets up a looping chat environment, allowing for continuous interaction between the assistant and user.
6. basic2.py: Demonstrates a more advanced setup, including a follow-up question and chart generation for stock prices.

## How to Run

To run these AutoGen scripts, follow these general steps:

1. Ensure you have Python installed on your system.
2. Install the required dependencies:

```
pip install autogen python-dotenv openai
```

3. Set up your environment variables:

- Create a `.env` file in the project root.
- Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

4. Create an `OAI_CONFIG_LIST` file with your API configuration.
5. Run any of the scripts using Python:

```
python script_name.py
```

Replace `script_name.py` with the name of the script you want to run (e.g., `basic.py`, `agentchat_human_feedback.py`, etc.).

6. Follow any prompts or instructions provided by the script.

Note: Some scripts may require additional setup or dependencies. Refer to the docstrings in each file for specific requirements.

## Contributing

Feel free to experiment with these scripts and contribute your own examples of using AutoGen agents!
