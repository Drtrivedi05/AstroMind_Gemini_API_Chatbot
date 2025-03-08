import google.generativeai as genai

# Configure Gemini API with your key
genai.configure(api_key="YOUR_GEMINI_API_KEY")  # Replace with your actual API key

# Function to get a response from Gemini AI
def ask_astromind(question):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Updated model name
        response = model.generate_content(question)

        # Format response: Replace * with - for better bullet points
        formatted_response = response.text.replace("* **", "-").strip()
        formatted_response = response.text.replace("**", "").strip()
        
        return formatted_response if formatted_response else "I couldn't find an answer. Try asking in a different way!"
    except Exception as e:
        return f"Error: {str(e)}"

# Chatbot loop
def chat():
    print("\n🤖 AstroMind: Ask me anything! (Type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("AstroMind: Thanks for chatting! Goodbye! 👋")
            break
        response = ask_astromind(user_input)
        print(f"\nAstroMind:\n{response}\n")

# Run chatbot
if __name__ == "__main__":
    chat()
