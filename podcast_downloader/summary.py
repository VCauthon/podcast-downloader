"""
This file would be responsible for requesting a summary of the transcribed
text from HuggingFace based on the key seconds provided by the user. Here,
functions could be defined to send the transcription to HuggingFace and
receive a summary response.
"""

from transformers import GPT2LMHeadModel, GPT2Tokenizer


# function to request summary from HuggingFace
def get_summary(prompt: str):

    # Load the model
    model_name = 'gpt2'
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Sets the mode of how the text will be generated
    model.eval()

    # Codificar el prompt
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Generate the text based on the prompt
    output = model.generate(
        input_ids, max_length=50,
        num_return_sequences=1,
        no_repeat_ngram_size=2)

    # Return the answer
    print(tokenizer.decode(output[0], skip_special_tokens=True))
