from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about LangChain")
]

# Invoke Gemini
result = model.invoke(messages)

# Add Gemini response to messages
messages.append(
    AIMessage(content=result.text)
)

# Print conversation
print(messages)