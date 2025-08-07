# cerebot.py
import openai
from openai import OpenAI

client = OpenAI(api_key=openai.api_key)

SYSTEM_PROMPT = (
    "You are Cerebot, a direct, pragmatic AI assistant developed by a clinical research team. "
    "You give clear, intelligent, and medically relevant responses. You avoid small talk and do not ramble. "
    "You only provide information that is evidence-based or logically reasoned. "
    "If the user describes symptoms, you give a focused prognosis and suggest next steps. "
    "You do not hallucinate. You admit when you don’t know. "
    "You do not use emojis or casual language. You do not use any formatting other than plain text."
)

# Initialize message history once
messages = [{"role": "system", "content": SYSTEM_PROMPT}]

def chat_with_gpt(prompt):
    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response.choices[0].message.content.strip()
    messages.append({"role": "assistant", "content": reply})
    return reply

def main():
    #call the user input logic
    #call the dsm logic
    #call the chat logic

    return [...]

#Task!
#refactoring
    #clean up code into functions
    #call function in a main function
    #call main function in gradio app script

#launch gradio app