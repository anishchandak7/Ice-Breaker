"""
This module contains function to scrap and preprocess linkedin data using Proxycurl API
and returns the JSON response.
"""
import os
import requests

def scrape_linkedin_profile(linkedin_profile_url:str, mock:bool=False):
    """
    The function `scrape_linkedin_profile` retrieves LinkedIn profile data either from a specified URL
    or a mock URL if `mock` is set to `True`.
    
    :param linkedin_profile_url: The `linkedin_profile_url` parameter is a string that represents the
    URL of a LinkedIn profile that you want to scrape information from. This URL should point to the
    public LinkedIn profile of a user
    :type linkedin_profile_url: str
    :param mock: The `mock` parameter in the `scrape_linkedin_profile` function is a boolean flag that
    determines whether to use a mock LinkedIn profile URL for testing purposes. If `mock` is set to
    `True`, the function will use a predefined mock LinkedIn profile URL for testing. If `mock`,
    defaults to False
    :type mock: bool (optional)
    :return: The function `scrape_linkedin_profile` returns data extracted from a LinkedIn profile. The
    data is retrieved either by making a request to the specified LinkedIn profile URL directly or by
    using the ProxyCrawl API to scrape the LinkedIn profile data. The returned data is in JSON format.
    """
        
    if mock: # Scrap from github gist.
        linkedin_profile_url = 'https://gist.githubusercontent.com/anishchandak7/8b12f42aba201fbb0cfbe2bd11d4f7f3/raw/d5f9afa5b1f0614d44ffc91dfd75fbf292a20b76/anish-chandak.json'
        response = requests.get(linkedin_profile_url, timeout=10)
    else: # Scrap using proxycurl.
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        headers = {'Authorization': 'Bearer ' + os.environ.get('PROXYCURL_API_KEY')}
        params = {
            'linkedin_profile_url': linkedin_profile_url
        }
        response = requests.get(
            api_endpoint,
            params=params,
            headers=headers,
            timeout=10
        )
    # Convert to JSON/Dict type.
    data = response.json()
    # Clean the data.
    data = {key:val for key, val in data.items() if (val not in ([], ""," ",None)) and key not in ["people_also_viewed"]}
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data
