# app.py
import gradio as gr
from cerebot import chat_with_gpt

def respond(message, history=None):
    return chat_with_gpt(message)

iface = gr.ChatInterface(
    respond,
    title="Cerebot",
    theme="citrus",
    description="Talk to Cerebot!"
)

iface.launch()