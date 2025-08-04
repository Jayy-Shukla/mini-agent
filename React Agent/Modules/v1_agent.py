import os
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import Tool
from dotenv import load_dotenv
from langchain.agents.react.base import DOC_PROMPT

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    openai_api_key=api_key
)

def interpret_response(input: str) -> str:
    if "yes" in input.lower():
        return "Positive response"
    elif "no" in input.lower():
        return "Negative response"
    return "Ambiguous"

tool = Tool.from_function(
    func=interpret_response,
    name="InterpretResponse",
    description="Classifies a patient response as positive, negative, or ambiguous."
)

agent = create_react_agent(llm=llm, tools=[tool], prompt=DOC_PROMPT)
executor = AgentExecutor(agent=agent, tools=[tool], verbose=True)
