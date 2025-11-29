import os
from openai import OpenAI

# 1. Initialize the OpenAI Client
# The client automatically looks for the OPENAI_API_KEY environment variable.
try:
    client = OpenAI()
except Exception as e:
    print("Error initializing OpenAI client. Make sure your API key is set.")
    print(f"Details: {e}")
    exit()

# 2. Initialize Conversation History
# The 'messages' list keeps track of the conversation so the model has context.
conversation_history = [
    {"role": "system", "content": "You are a helpful and concise AI assistant named Gemini, built by Google. Keep your answers brief and to the point."},
]

def get_chat_response(user_input):
    """
    Sends the conversation history and new user input to the OpenAI API 
    and returns the model's response.
    """
    # Append the user's message to the history
    conversation_history.append({"role": "user", "content": user_input})
    
    try:
        # Call the Chat Completions API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # A fast and capable model for chat
            messages=conversation_history
        )
        
        # Extract the model's response text
        assistant_response = response.choices[0].message.content
        
        # Append the assistant's response to the history for future turns
        conversation_history.append({"role": "assistant", "content": assistant_response})
        
        return assistant_response

    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """Main function to run the chat loop."""
    print("🤖 Welcome to the Gemini Chat App! (Powered by OpenAI's GPT-3.5-Turbo)")
    print("Type 'quit' or 'exit' to end the session.")
    print("-" * 40)
    
    while True:
        user_input = input("You: ")
        
        # Check for exit commands
        if user_input.lower() in ["quit", "exit"]:
            print("👋 Goodbye!")
            break
        
        if not user_input.strip():
            continue # Skip empty input

        # Get and print the response
        response = get_chat_response(user_input)
        print(f"Gemini: {response}\n")

if __name__ == "__main__":
    main()