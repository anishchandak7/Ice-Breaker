"""
The function loads environment variables, defines a template for generating a summary and
interesting facts, and uses OpenAI's GPT-3.5-turbo model to create content based on the provided
information.
"""
import os
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

INFORMATION = """Suits is an American legal drama television series created and written by Aaron Korsh.
Produced by Universal Content Productions, it premiered on USA Network on June 23, 2011.

Set in a fictional New York City corporate law firm, the series follows Mike Ross (Patrick J. Adams),
a college dropout with a photographic memory, as he works as an associate for the successful and
charismatic attorney, Harvey Specter (Gabriel Macht).[1] Suits focuses on Harvey and Mike winning
lawsuits and closing cases, while at the same time hiding Mike's secret of never having attended
law school.[2] It also features Rick Hoffman as Louis Litt, a neurotic, manipulative and
unscrupulous financial-law partner; Meghan Markle as the ambitious, talented paralegal Rachel
Zane; Sarah Rafferty as Harvey's legal secretary and confidante Donna Paulsen; and Gina Torres as
the firm's profit-above-all managing partner, Jessica Pearson.

On January 30, 2018, the series was renewed for an eighth season, but Torres, Adams, and Markle
left the show.[3] Katherine Heigl joined the cast as Samantha Wheeler. Recurring characters Alex
Williams (Dulé Hill) and Katrina Bennett (Amanda Schull) were promoted to series regulars.[4]
The show was renewed for a 10-episode ninth and final season on January 23, 2019, which premiered
on July 17, 2019.[5][6]"""


def main():   
    """
    This Python function loads environment variables, prompts for information, and
    generates a short summary and two interesting facts using the OpenAI GPT-3.5 Turbo model.
    """
    # 1. Load the environment variables.
    load_dotenv()
    
    # 2. Declare the prompt template.
    summary_template = """given the information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them.
    """
    
    # 3. Create a prompt template reference.
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    
    # 4. Connect with ChatOpenAI using API key. 
    llm = ChatOpenAI(api_key=os.environ.get("OPENAI_API_KEY"), model="gpt-3.5-turbo")
    
    # 5. Chain the prompt template with llm model.
    chain = summary_prompt_template|llm
    
    # 6. Invoke the chain.
    result = chain.invoke(input={'information': INFORMATION})
    
    # 7. Display the results.
    print(result)

if __name__ == "__main__":
    main()