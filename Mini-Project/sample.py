import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
model = GPT2LMHeadModel.from_pretrained("gpt2-medium")

# Set the device to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Function to generate text based on user input
def generate_story(user_input, max_length=50):
    # Encode user input
    input_ids = tokenizer.encode(user_input, return_tensors="pt").to(device)
    # Generate text based on user input
    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        # temperature=0.7,
        top_k=50,
        # top_p=0.95,
        repetition_penalty=1.0,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
    )
    # Decode generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text


# Interactive storytelling loop
print("Welcome to Interactive Storytelling Bot!")
print("Enter your first sentence to start the story or type 'exit' to quit.")

user_input = input("> ")

while user_input.lower() != "exit":
    generated_text = generate_story(user_input)
    print("Bot:", generated_text)
    user_input = input("> ")
print("Goodbye!")
exit()