import os
from dotenv import load_dotenv
if __name__=='__main__':
    print("Hello")
    load_dotenv()
    print(os.environ.get('OPENAI_API_KEY'))