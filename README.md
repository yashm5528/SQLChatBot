# SQLChatBot

## About this repository
This project aims to provide a simple way to run a Text-to-SQL like chatbot.

You can use this project and with minor adjustments, create your own Text-to-SQL application for your database.


## Project specifications

1. **Python 3.8 / 3.9 / 3.10 / 3.11** is required to run the code.

2. **VS Code**: I have used VS Code as an IDE to develop and run this project. Any IDE such as PyCharm would work as well.

3. **ChatGPT API Key**: For this project ChatGPT API is called to generate response. It is necessary to get an API Key from OpenAI (https://platform.openai.com/docs/overview)  


## How to run the code
1. Clone the repository to you local machine.
2. Replace GeoQuery database with your own database in backend folder
3. Open gpt.py and do the following changes:
   - Add OpenAI API Key.
   - Replace the GeoQuery database path with your own database path.
   - Update the prompts/queries as per your database.
