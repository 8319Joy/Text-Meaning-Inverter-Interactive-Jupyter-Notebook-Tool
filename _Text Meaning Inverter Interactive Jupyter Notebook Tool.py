#!/usr/bin/env python
# coding: utf-8

# # Text Meaning Inverter Interactive Jupyter Notebook Tool
Below is a Python program designed to invert the meaning of any set of paragraphs and integrate this functionality into a Jupyter Notebook interface with a clickable button. This program uses ipywidgets for the interactive button and nltk for natural language processing to generate opposite meanings by applying negations.
# In[1]:


import ipywidgets as widgets
from IPython.display import display, Markdown
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet


# In[2]:


# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')


# In[3]:


def negate_sentence(sentence):
    """
    Negate a given sentence by inserting 'not' or similar negations.
    """
    words = word_tokenize(sentence)
    inverted_sentence = []
    negated = False

    for word in words:
        if word.lower() in ["is", "are", "was", "were", "am", "be"]:
            inverted_sentence.append(word)
            inverted_sentence.append("not")
            negated = True
        else:
            inverted_sentence.append(word)

    # If no negation was applied, prepend with "Not" for default negation
    if not negated:
        inverted_sentence.insert(0, "Not")
    
    return " ".join(inverted_sentence)

def invert_paragraph(paragraph):
    """
    Process a paragraph, inverting the meaning of each sentence.
    """
    sentences = sent_tokenize(paragraph)
    inverted_sentences = [negate_sentence(sentence) for sentence in sentences]
    return " ".join(inverted_sentences)

def on_button_click(change):
    """
    Callback function for the button click.
    """
    original_text = text_area.value
    inverted_text = invert_paragraph(original_text)
    output_display.clear_output()
    with output_display:
        display(Markdown(f"**Inverted Text:**\n\n{inverted_text}"))

# UI elements
text_area = widgets.Textarea(
    value="Enter your paragraphs here...",
    placeholder="Type something",
    description="Input:",
    layout=widgets.Layout(width="90%", height="150px")
)
invert_button = widgets.Button(
    description="Invert Meaning",
    button_style="info"
)
output_display = widgets.Output()

# Button click event
invert_button.on_click(on_button_click)

# Display the interactive elements
display(text_area, invert_button, output_display)


# In[ ]:




