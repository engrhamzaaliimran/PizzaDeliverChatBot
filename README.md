# Pizza Delivery Chatbot

This Python script implements a pizza delivery chatbot using OpenAI's GPT-3.5 Turbo. The chatbot is designed to assist customers in placing pizza orders and responds to user queries related to pizza orders. If the user asks anything not related to pizza, the chatbot politely informs them that it cannot help with that.

## Getting Started

To use this chatbot, you need an OpenAI API key. If you don't have one, sign up for an API key on the [OpenAI platform](https://beta.openai.com/signup/).

Replace `'YOUR-API-KEY'` in the code with your actual API key.

```python
import openai
import argparse

openai.api_key ='YOUR-API-KEY'
```

## Usage

1. Install the required Python packages:

   ```bash
   pip install openai
   ```

2. Run the script:

   ```bash
   python bot.py
   ```

3. Interact with the chatbot by entering messages when prompted.

## Features

- **Chatbot Initialization**: The chatbot starts with an initial prompt defining its role and goal.

- **User Interaction**: Users can interact with the chatbot by entering messages.

- **GPT-3.5 Turbo Integration**: The script uses OpenAI's GPT-3.5 Turbo to generate responses based on user input.

- **Interrupt Handling**: The script gracefully handles keyboard interruptions, allowing for a smooth exit.

## Customization

Feel free to customize the `initial_prompt` and modify the chatbot's behavior to suit your specific use case.

```python
initial_prompt = "You are a pizza delivery chatbot. Your goal is to assist customers in placing pizza orders. If the user asks anything not related to pizza, simply say I cannot help with that."
```

## Note

Ensure compliance with OpenAI's usage policies and guidelines when using the GPT-3.5 Turbo model.

**Disclaimer:** This script is a basic example and may require additional refinement for production use.
