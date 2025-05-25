import os
from dotenv import load_dotenv
from langchain_community.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

# Load .env file
load_dotenv()

# Read Azure credentials from environment
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

def create_qa_chain(full_text):
    return {"context": full_text}

def ask_question(chain, question):
    full_text = chain["context"]
    prompt = (
        "Answer the question based on the following content:\n\n"
        f"{full_text}\n\n"
        f"Question: {question}\nAnswer:"
    )

    llm = AzureChatOpenAI(
        openai_api_key=api_key,
        azure_endpoint=endpoint,
        deployment_name=deployment,
        openai_api_version=api_version,
        temperature=0,
    )

    response = llm([HumanMessage(content=prompt)])
    return response.content
