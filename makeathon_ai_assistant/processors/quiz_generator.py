import openai
import os

# Ρυθμίσεις για Azure OpenAI
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_version = "2023-05-15"

def generate_quiz(text):
    prompt = (
        "Με βάση το παρακάτω ελληνικό κείμενο, γράψε 3 ερωτήσεις πολλαπλής επιλογής με 4 επιλογές η καθεμία και σωστή απάντηση:\n\n"
        + text[:3000]
    )

    response = openai.ChatCompletion.create(
        engine="gpt-4.1",  # ⚠️ Βάλε εδώ το deployment name σου
        messages=[
            {"role": "system", "content": "Είσαι εκπαιδευτικός βοηθός που δημιουργεί κουίζ στα ελληνικά."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
    )

    return response["choices"][0]["message"]["content"]
