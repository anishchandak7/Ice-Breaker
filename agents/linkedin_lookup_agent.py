import os

from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI

from tools.tools import get_profile_url_tavily


def lookup(name: str) -> str:
    """
    The `lookup` function uses OpenAI's ChatOpenAI model to generate a prompt for finding a LinkedIn
    profile URL based on a given full name.
    
    :param name: The `lookup` function you provided seems to be using OpenAI's ChatGPT model to generate
    a LinkedIn profile URL based on a given full name. It uses a template and a tool to crawl Google for
    the LinkedIn profile page. The function creates a React agent and executes it to get the LinkedIn
    :type name: str
    :return: The function `lookup` is returning the LinkedIn profile URL of a person based on their full
    name.
    """
    # load the environment variables from .env file.
    load_dotenv()
    # Create ChatOpenAI reference.
    llm = ChatOpenAI(
        temperature=0,
        model='gpt-3.5-turbo',
        api_key=os.environ.get('OPENAI_API_KEY')
    )
    # Declare the prompt template
    template = """given the full name {name_of_person} I want you to get me a link to their linkedin profile page.
                                Your answer should contain only a URL"""
    prompt_template = PromptTemplate(template=template,
        input_variables=['name_of_person']
    )
    # Define the tools for the agent.
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page.",
            func=get_profile_url_tavily,
            description="useful for when you need to get the Linkedin Page URL."
        )
    ]
    # Fetch react prompt using langchain hub.
    react_prompt = hub.pull('hwchase17/react')
    # Create a react agent.
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    # Create a react executor.
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    # Invoke the agent using provided name.
    result = agent_executor.invoke(input={"input": prompt_template.format_prompt(name_of_person=name)})
    # Fetch the linkedin profile URL from the result.
    linkedin_profile_url = result['output']
    # Return the linkedin profile URL.
    return linkedin_profile_url    