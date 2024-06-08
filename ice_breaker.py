"""
The function loads environment variables, defines a template for generating a summary and
interesting facts, and uses OpenAI's GPT-3.5-turbo model to create content based on the provided
information.
"""
import os
from typing import Tuple
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup
from output_parser import summary_parser, Summary

def ice_break_with(name:str)-> Tuple[Summary, str]:   
    """
    This Python function loads environment variables, prompts for information, and
    generates a short summary and two interesting facts using the OpenAI GPT-3.5 Turbo model.
    """
    # 1. Load the environment variables.
    load_dotenv()
    # 2. Declare the prompt template.
    summary_template = """given the Linkedin information {information} about a person from I want you to create:
    1. A short summary
    2. two interesting facts about them
    \n{format_instructions}
    """
    # 3. Create a prompt template reference.
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )
    # 4. Connect with ChatOpenAI using API key. 
    llm = ChatOpenAI(api_key=os.environ.get("OPENAI_API_KEY"), model="gpt-3.5-turbo")
    # 5. Chain the prompt template with llm model.
    chain = summary_prompt_template|llm|summary_parser
    
    # 6. Search for linkedin profile url for the given name.
    linkedin_profile_url = lookup(name=name)
    
    # 7. Scrap data from provided linkedin profile.
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url,
        mock=True)
    # 8. Invoke the chain.
    result:Summary = chain.invoke(input={'information': linkedin_data})
    return result, linkedin_data.get("profile_pic_url")

    