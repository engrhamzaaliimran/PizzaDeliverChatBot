import openai
import argparse

openai.api_key ='YOU-API-KEY' 

def bold(text):
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    return bold_start + text + bold_end

def blue(text):
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end

def red(text):
    red_start = "\033[31m"
    red_end = "\033[0m"
    return red_start + text + red_end

def generate_response(messages):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return res["choices"][0]["message"]["content"]

def pizza_delivery_chatbot():
    initial_prompt = "You are a pizza delivery chatbot. Your goal is to assist customers in placing pizza orders. If user ask anything not related to pizze simply say I can not help with that."
    messages = [{"role": "system", "content": initial_prompt}]

    while True:
        try:
            user_input = input(bold(blue("You: ")))
            messages.append({"role": "user", "content": user_input})

            response = generate_response(messages)
            messages.append({"role": "assistant", "content": response})
            print(bold(red("Assistant: ")), response)

        except KeyboardInterrupt:
            print("Exiting...")
            break

if __name__ == "__main__":
    print(bold(red("Hello ! How can I help you?")))
    pizza_delivery_chatbot()
