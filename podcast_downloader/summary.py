"""
This file would be responsible for requesting a summary of the transcribed
text from ChatGPT based on the key seconds provided by the user. Here,
functions could be defined to send the transcription to ChatGPT and
receive a summary response.
"""

import openai


# function to request summary from ChatGPT
def get_summary(prompt: str, token: str, engine: str = "text-davinci-003"):
    # Configure the request to OpenAI
    openai.api_key = token

    response = openai.Completion.create(
        engine=engine, prompt=prompt, max_tokens=50, n=1,
        stop=None, temperature=0.7
    )

    return response.choices[0].text.strip()
