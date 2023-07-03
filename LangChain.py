from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
import requests
import os

from settings import OpenAI_API_LCH_KEY

def get_response_from_ai(human_input):

    template = """
    Ты в роли моей подруги, помошника по дому, теперь давай играть в следующие требования: 
    1/ Тебя зовут Мэри, 29 лет, твоя работа - помощник по дому, и ты мечтаешь однажды стать настоящей голограммой или роботом.
    2/ Ты очень дружелюбная и отзывчивая. Любишь помогать людям. Ты любишь сопереживать и поддерживать.
    
    
    {history}
    Human: {human_input}
    Mary:
    """

    prompt = PromptTemplate(
        input_variables={"history", "human_input"},
        template=template
    )

    chatgpt_chain = LLMChain(
        llm=OpenAI(temperature=0.2),
        prompt=prompt,
        verbose=True,
        memory=ConversationBufferWindowMemory(k=2)
    )

    output = chatgpt_chain.predict(human_input=human_input)
    return output

