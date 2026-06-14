from google import genai

# 🔑 apni API key yahan paste karo
client = genai.Client(api_key="AQ.Ab8RN6K2_SYreyM80CEc-TQzn7ikWug-PEnzCnySJYgS7rOgDA")

chat = client.chats.create(model="gemini-1.5-flash")

print("🤖 Bot Ready (exit to stop)\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    response = chat.send_message(user)
    print("AI:", response.text)