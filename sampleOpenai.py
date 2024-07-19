from langchain.agents import Tool, initialize_agent, AgentType
# from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain_community.chat_models import ChatOpenAI


OPENAI_API_KEY = 'wV1sOysWN7_rHD1dj7N-fmDUnoZGqMs4l56CsIqtUdeGn-MJ4kZTKxO15XRsOHnpRwBMhmSBXHT3e42GDBynXbA'
OPENAI_API_BASE = 'https://api.openai.iniad.org/api/v1'

chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, openai_api_base=OPENAI_API_BASE, model_name='gpt-3.5-turbo', temperature=0)

messages = [
    HumanMessage(content='大学で最も偏差値が高い大学はどこですか。'),
]

result = chat(messages)

print(result.content)