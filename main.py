


from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

load_dotenv()


tavily = TavilyClient()




@tool # that's how we convert into a tool
def search(query: str) -> str:
    '''
    Tool that searches over interent
    Args:
        query: The query to search for 
    Returns:
        The Search Result
    '''
    
    print(f"Searching for {query}")
    return tavily.search(query = query)

llm = ChatOpenAI()
tools = [search]
agent = create_agent(model=llm,tools=tools)

def main():
    print("Hello World from langchain-course")
    result = agent.invoke({"messages":HumanMessage(content="Search for 3 job postings for an ai engineer using langchain on linkedln and list their detials")})
    print(result)



if __name__ == "__main__":
    main()
