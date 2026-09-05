# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Create Gemini model
# model = ChatGoogleGenerativeAI(
#     model="gemini-3.6-flash"
# )

# # Chat history
# chat_history = [
#     SystemMessage(
#         content="You are a helpful AI assistant."
#     )
# ]

# print("Gemini Chatbot Started!")
# print("Type 'exit' to quit.\n")

# while True:

#     user_input = input("You: ")

#     # Exit chatbot
#     if user_input.lower() == "exit":
#         print("AI: Goodbye!")
#         break

#     # Add user message to chat history
#     chat_history.append(
#         HumanMessage(content=user_input)
#     )

#     # Send conversation to Gemini
#     result = model.invoke(chat_history)

#     # Get only text from Gemini response
#     response_text = result.text

#     # Add AI response to chat history
#     chat_history.append(
#         AIMessage(content=response_text)
#     )

#     # Display response
#     print("AI:", response_text)

# print("\nChat History:")
# for message in chat_history:
#     print(message)


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Create Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

# -----------------------------------
# Chat History
# -----------------------------------

chat_history = [
    SystemMessage(
        content="You are a helpful AI assistant. "
                "Remember the previous conversation and use it "
                "to answer the user's questions."
    )
]

# -----------------------------------
# Start Chatbot
# -----------------------------------

print("=" * 50)
print("       Gemini AI Chatbot")
print("=" * 50)
print("Type 'exit' to quit.")
print("Type 'history' to see chat history.")
print("Type 'clear' to clear chat history.")
print("=" * 50)

while True:

    # Get user input
    user_input = input("\nYou: ")

    # -----------------------------------
    # Exit
    # -----------------------------------

    if user_input.lower() == "exit":
        print("\nAI: Goodbye!")
        break

    # -----------------------------------
    # Show History
    # -----------------------------------

    if user_input.lower() == "history":

        print("\n========== CHAT HISTORY ==========")

        for message in chat_history:

            if isinstance(message, SystemMessage):
                print("SYSTEM:", message.content)

            elif isinstance(message, HumanMessage):
                print("You:", message.content)

            elif isinstance(message, AIMessage):
                print("AI:", message.content)

        print("==================================")

        continue

    # -----------------------------------
    # Clear History
    # -----------------------------------

    if user_input.lower() == "clear":

        chat_history = [
            SystemMessage(
                content="You are a helpful AI assistant. "
                        "Remember the previous conversation and use it "
                        "to answer the user's questions."
            )
        ]

        print("\nAI: Chat history has been cleared.")

        continue

    # -----------------------------------
    # Add User Message
    # -----------------------------------

    chat_history.append(
        HumanMessage(content=user_input)
    )

    # -----------------------------------
    # Send Complete History to Gemini
    # -----------------------------------

    result = model.invoke(chat_history)

    # Get clean text response
    response = result.text

    # -----------------------------------
    # Add AI Response to History
    # -----------------------------------

    chat_history.append(
        AIMessage(content=response)
    )

    # -----------------------------------
    # Display AI Response
    # -----------------------------------

    print("\nAI:", response)