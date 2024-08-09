import gradio as gr
import os

from langchain_google_genai import GoogleGenerativeAI
from langchain import LLMChain
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import SystemMessage

google_api_key = os.getenv("google_api_key")

llm = GoogleGenerativeAI(model='gemini-1.5-pro', google_api_key=google_api_key)

messages = [
    SystemMessage(content="You are an expert at extracting entities from text."),
    HumanMessagePromptTemplate.from_template("{text}")
]

chat_prompt = ChatPromptTemplate.from_messages(messages)

chain = LLMChain(llm=llm, prompt=chat_prompt)

def extract_entities(text):
    result = chain.run(text)
    return result


iface = gr.Interface(
    fn=extract_entities,
    inputs=gr.Textbox(label="Enter your text",lines=10),
    outputs=gr.Markdown(label="Extracted Entities"),
    title="Entity Extraction Tool for Email!",
    description="Extract entities from Email using Gemini 1.5 Pro."
)


iface.launch()

