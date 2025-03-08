# AstroMind - AI Chatbot using Gemini API

AstroMind is an AI-powered chatbot that leverages Google's Gemini API to provide intelligent answers to user queries. It supports dynamic question answering with structured bullet-point formatting for better readability.

---

 Features 🚀
✅ Uses Gemini API (gemini-1.5-pro) for generating AI-powered responses  
✅ Bullet-point formatting for structured answers  
✅ Loop-based chatbot interaction with an exit command  
✅ Error handling for API failures  

---

 Installation & Setup ⚙️

# 1️⃣ Install Dependencies
Before running the chatbot, install the required package:
```bash
pip install google-generativeai
```

# 2️⃣ Get a Gemini API Key
1. Go to [Google AI Studio](https://ai.google.dev/)
2. Sign in with your Google account
3. Navigate to API Keys and create a new key
4. Copy the key for later use

# 3️⃣ Enable API Access in Google Cloud Console
1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Ensure your project is selected
3. Search for Generative Language API
4. Enable the API for your project

# 4️⃣ Update the API Key in `astromind_chatbot.py`
Replace `YOUR_GEMINI_API_KEY` with your actual key in the following line:
```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

---

 Running AstroMind 💡
Once everything is set up, run the chatbot with:
```bash
python astromind_chatbot.py
```

It will start a conversation where you can ask any question, and AstroMind will provide a structured response.

# Example Interaction:
```
🤖 AstroMind: Ask me anything! (Type 'exit' to quit)

You: What is AI?
AstroMind:
- AI, or Artificial Intelligence, is a broad field aiming to create machines capable of performing tasks that require human intelligence.
- Key areas include machine learning, problem-solving, and natural language processing.
```

---

 Troubleshooting 🛠️

# Issue: Invalid API Key (Error 400)
✅ Double-check that you've copied the correct API key from Google AI Studio.
✅ Ensure there are no extra spaces before/after the key.
✅ Verify that the Generative Language API is enabled in Google Cloud Console.

# Issue: Model Not Found (Error 404)
✅ Update the model name from `gemini-pro` to `gemini-1.5-pro` in your code.
✅ Upgrade the `google-generativeai` library:
```bash
pip install --upgrade google-generativeai
```
✅ Restart your chatbot.

---

 Future Improvements 🚀
🔹 Add a GUI interface using Flask or Tkinter  
🔹 Implement voice input and output for better interaction  
🔹 Store chat history for contextual conversations  

---

 Contributors 👨‍💻
Developed by Dhrumil Trivedi

Feel free to contribute by improving the chatbot or adding new features! 🎯

