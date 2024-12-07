import ollama

res = ollama.chat(
	model="llama3.2-vision", # "llava:7b",
	messages=[
		{
			'role': 'user',
			'content': 'What is text that you read:',
			'images': ['test.jpg']
		}
	]
)

print(res['message']['content'])