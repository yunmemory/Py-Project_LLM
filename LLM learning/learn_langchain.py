# 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

import openai
import os

# Set the openai api key
openai.api_key = "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"


# chatgpt
def get_completion(prompt, model="gpt-4-0613"):
    message = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=message,
        temperature=0

    )
    return response.choices[0].message["content"]


# # prompt - 1: Use delimiters to clearly indicate distinct parts of the input
# text = f"""
# You should express what you want a model to do by \
# providing instructions that are as clear and \
# specific as you can possibly make them. \
# This will guide the model towards the desired output, \
# and reduce the chances of receiving irrelevant \
# or incorrect responses. Don't confuse writing a \
# clear prompt with writing a short prompt. \
# In many cases, longer prompts provide more clarity \
# and context for the model, which can lead to \
# more detailed and relevant outputs.
# """
# prompt = f"""
# Summarize the text delimited by triple backticks \
# into a single sentence.
# ```{text}```
# """

# # prompt - 2: Ask for a structured output
# prompt = f"""
# Generate a list of three made-up book titles along \
# with their authors and genres.
# Provide them in JSON format with the following keys:
# book_id, title, author, genre.
# """

# # prompt - 3: Ask the model to check whether conditions are satisfied
# text_1 = f"""
# Making a cup of tea is easy! First, you need to get some \
# water boiling. While that's happening, \
# grab a cup and put a tea bag in it. Once the water is \
# hot enough, just pour it over the tea bag. \
# Let it sit for a bit so the tea can steep. After a \
# few minutes, take out the tea bag. If you \
# like, you can add some sugar or milk to taste. \
# And that's it! You've got yourself a delicious \
# cup of tea to enjoy.
# """
# text_2 = f"""
# The sun is shining brightly today, and the birds are \
# singing. It's a beautiful day to go for a \
# walk in the park. The flowers are blooming, and the \
# trees are swaying gently in the breeze. People \
# are out and about, enjoying the lovely weather. \
# Some are having picnics, while others are playing \
# games or simply relaxing on the grass. It's a \
# perfect day to spend time outdoors and appreciate the \
# beauty of nature."""
#
# prompt = f"""
# You will be provided with text delimited by triple quotes.
# If it contains a sequence of instructions, \
# re-write those instructions in the following format:
#
# Step 1 - ...
# Step 2 - …
# …
# Step N - …
#
# If the text does not contain a sequence of instructions, \
# then simply write \"No steps provided.\"
#
# \\\{text_2}\\\
# """

# # prompt - 4 - few shot prompting
# prompt = f"""
# Your task is to answer in a consistent style.
#
# <child>: Teach me about patience.
#
# <grandparent>: The river that carves the deepest \
# valley flows from a modest spring; the \
# grandest symphony originates from a single note; \
# the most intricate tapestry begins with a solitary thread.
#
# <child>: Teach me about resilience.
# """

# prompt - 5: Specify the steps required to complete the task
text = f"""
In a charming village, siblings Jack and Jill set out on \ 
a quest to fetch water from a hilltop \ 
well. As they climbed, singing joyfully, misfortune \ 
struck—Jack tripped on a stone and tumbled \ 
down the hill, with Jill following suit. \ 
Though slightly battered, the pair returned home to \ 
comforting embraces. Despite the mishap, \ 
their adventurous spirits remained undimmed, and they \ 
continued exploring with delight.
"""
# example 1
prompt = f"""
Perform the following actions: 
1 - Summarize the following text delimited by triple \
backticks with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the following \
keys: french_summary, num_names.

Separate your answers with line breaks.

Text:
```{text}```
"""

# prompt - 6: Ask for output in a specified format
prompt_2 = f"""
Your task is to perform the following actions: 
1 - Summarize the following text delimited by 
  <> with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the 
  following keys: french_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in Italian summary>
Output JSON: <json with summary and num_names>

Text: <{text}>
"""

response = get_completion(prompt)
print(response)

