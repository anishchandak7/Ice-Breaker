"""Module which contain functionality to fetch linkedin url using Tavily Search."""
from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name:str):
    """
    This Python function takes a name as input, searches for it using TavilySearchResults, and returns
    the URL of the first search result.
    
    :param name: The function `get_profile_url_tavily` takes a `name` as input, which is a string
    representing the name of a person. The function then performs a search using the
    `TavilySearchResults` class and returns the URL of the first search result related to the input name
    :type name: str
    :return: The function `get_profile_url_tavily` is returning the URL of the profile associated with
    the name provided as input.
    """
    # Create a TavilySearchResults reference. 
    search = TavilySearchResults()
    # Look for profile with given name.
    res = search.run(f"{name}")
    # Return the URL of searched profile.
    return res[0]['url']