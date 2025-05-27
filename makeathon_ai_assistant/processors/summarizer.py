import openai
import os

# Ρυθμίσεις για Azure OpenAI
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # π.χ. https://your-resource.openai.azure.com/
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_version = "2023-05-15"

def summarize_text(text):
    print("Azure OpenAI API Base:", openai.api_base)
    print("Azure OpenAI API Key:", openai.api_key)

    prompt = (
        "Δώσε μια σύντομη περίληψη στα ελληνικά του παρακάτω περιεχομένου:\n\n"
        + text[:4000]
    )

    response = openai.ChatCompletion.create(
        engine="gpt-4.1",  # ⚠️ Βάλε εδώ το deployment name σου από το Azure
        messages=[
            {"role": "system", "content": "Είσαι ένας ευγενικός βοηθός που συνοψίζει κείμενα στα ελληνικά."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    return response["choices"][0]["message"]["content"]
