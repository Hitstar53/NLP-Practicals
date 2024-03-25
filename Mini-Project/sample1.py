import os
from openai import OpenAI

# Initialize OpenAI client with your API key
client = OpenAI(api_key="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")

# Initialize conversation history
conversation_history = []


# Function to generate text based on conversation history and current input
def generate_story(user_input):
    global conversation_history

    # Construct prompt from conversation history
    prompt = ""
    for item in conversation_history:
        prompt += f"User: {item['user_input']}\nBot: {item['bot_output']}\n"

    # Add current user input to prompt
    prompt += f"User: {user_input}\n"

    # Generate text using GPT-3.5 Turbo model via OpenAI's API
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}], model="gpt-3.5-turbo"
    )

    # Extract bot response from the completion
    bot_output = chat_completion.choices[0].message["content"]

    # Append current input and bot output to conversation history
    conversation_history.append({"user_input": user_input, "bot_output": bot_output})

    return bot_output


# Interactive storytelling loop
print("Welcome to Interactive Storytelling Bot!")
print("Enter your first sentence to start the story or type 'exit' to quit.")

user_input = input("> ")

while user_input.lower() != "exit":
    bot_output = generate_story(user_input)
    print("Bot:", bot_output)

    user_input = input("> ")

print("Goodbye!")
