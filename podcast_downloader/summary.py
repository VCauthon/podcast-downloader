"""
This file would be responsible for requesting a summary of the transcribed
text from ChatGPT based on the key seconds provided by the user. Here,
functions could be defined to send the transcription to ChatGPT and
receive a summary response.
"""
import requests


# function to request summary from ChatGPT
def get_summary(text):
    # send the text to ChatGPT API and receive summary response
    response = requests.post(url="CHATGPT_API_URL", data={"text": text})
    summary = response.text
    return summary
