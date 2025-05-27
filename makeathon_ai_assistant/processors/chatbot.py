import openai
import os

def create_qa_chain(full_text):
    return {"context": full_text}

def ask_question(chain, question):
    full_text = chain["context"]
    prompt = (
        "Answer the question based on the following content:\n\n"
        f"{full_text}\n\n"
        f"Question: {question}\nAnswer:"
    )

    # Azure OpenAI environment config (global for openai==0.27.0)
    openai.api_type = "azure"
    openai.api_key = os.getenv("AZURE_OPENAI_KEY")
    openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
    openai.api_version = "2023-05-15"  # adjust to match your deployment

    deployment_name = "gpt-4.1"  # your Azure deployment name

    if not all([openai.api_key, openai.api_base, deployment_name]):
        raise EnvironmentError("❌ Missing Azure OpenAI environment variables.")

    response = openai.ChatCompletion.create(
        engine=deployment_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
    )

    return response["choices"][0]["message"]["content"]
