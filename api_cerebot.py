"""
Tutorial code for using OpenAI's GPT-3.5 Turbo model in Cerebot!
Feel free to use snippets of this code in your own prototype :)
Author: Viraj
"""

import openai
from openai import OpenAI

openai.api_key = "..." #replace with your OpenAI API key. THIS IS CONFIDENTIAL AND SHOULD NOT BE SHARED PUBLICLY

client = OpenAI(api_key=openai.api_key) #create an OpenAI client with the provided API key

# Cerebot's custom personality and behavior
SYSTEM_PROMPT = (
    "You are Cerebot, a direct, pragmatic AI assistant developed by a clinical research team. "
    "You give clear, intelligent, and medically relevant responses. You avoid small talk and do not ramble. "
    "You only provide information that is evidence-based or logically reasoned. "
    "If the user describes symptoms, you give a focused prognosis and suggest next steps. "
    "You do not hallucinate. You admit when you don’t know."
    "You do not use emojis or casual language. You do not use any formatting other than plain text."
)

def chat_with_gpt(prompt): #function to interact with the GPT model
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", #the gpt that we use
        messages=[{"role": "user", "content": prompt}] #the message that we send to the gpt
    )
    return response.choices[0].message.content.strip() #the response from the gpt

if __name__ == "__main__": #main function to run the chatbot
    while True:
        user_input = input("You: ") #input from the user
        if any(keyword in user_input.lower() for keyword in ["exit", "quit", "bye", "stop"]): # if the user wants to exit
            break
        response = chat_with_gpt(user_input) #get the response from the gpt
        print("Chatbot: ", response) # print the response from the gpt
        print(" ")

print("Thank you for using Cerebot!") #exit message!