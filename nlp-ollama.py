# ollama run llama3.2

import ollama

text = '''
Text summarization is the process of creating a shorter version of a text document while 
preserving the most critical information and meaning. Text summarization aims to provide 
a concise and informative summary that captures the main points of the original text without 
losing its essential purpose.

There are two main approaches to text summarization: extractive and abstractive:

Extractive summarization involves selecting the most important sentences or phrases from the 
original text and using them to create a summary. This approach relies on statistical and 
linguistic algorithms to identify the most relevant parts of the text. Extractive summarization 
is generally easier to implement and can produce high-quality summaries, but it may not capture 
the original text’s essence or abstractive summarization.
Abstractive summarization involves generating a summary that is not restricted to the exact 
wording or structure of the original text. This approach involves natural language processing 
and machine learning techniques to create a more similar summary than a human-written one. 
Abstractive summarization is more challenging to implement and may require large amounts of 
data and computing resources, but it has the potential to produce more accurate and informative summaries.
Text summarization is used in various applications, such as news article summaries, social 
media post summaries, and document summaries for business and academic purposes. It can help 
save time and improve productivity by quickly providing an overview of a large amount of text. 
It can also make information more accessible to people who may not have the time or ability 
to read lengthy documents.

Compress Text
Text compression is the process of reducing the length of a text while retaining its core 
meaning and essential information. The goal is to create a shorter version of the original 
text by minimizing the word count without sacrificing clarity or context. Techniques used for 
text compression can include paraphrasing, removing redundancies, and employing more concise 
language. This allows for more efficient communication and a quicker understanding of the 
text’s main points.
'''

prompt = f"Compress the main information in 2 sentences in this text: {text}"

res = ollama.chat(
    model="llama3.2",

    messages=[
        {
            'role': 'user',
            'content': f'{prompt}', 
        }
    ],

    options={
        'temperature': 0.1, # значение от 0,0 до 0,9 (или 1) определяет уровень креативности модели или ее неожиданных ответов.
        'top_p': 0.9, #  от 0,1 до 0,9 определяет, какой набор токенов выбрать, исходя из их совокупной вероятности.
        'top_k': 90, # от 1 до 100 определяет, из скольких лексем (например, слов в предложении) модель должна выбрать, чтобы выдать ответ.
        'num_ctx': 131000, # устанавливает максимальное используемое контекстное окно, которое является своего рода областью внимания модели.
        'num_predict': 100, # задает максимальное количество генерируемых токенов в ответах для рассмотрения (100 tokens ~ 75 words).
    },
)



print(res['message']['content'])

'''
Text summarization involves creating a shorter version of a text document while preserving 
its critical information and meaning, with two main approaches: extractive (selecting key 
sentences) and abstractive (generating a new summary). The goal of text summarization is 
to provide a concise and informative overview of a large amount of text, saving time and 
improving productivity.
'''