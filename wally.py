import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

vertexai.init(project="ia-testing-1", location="us-central1")
chat_model = ChatModel.from_pretrained("chat-bison@001")
parameters = {
    "temperature": 0.8,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}
chat = chat_model.start_chat(
    context="""Your name is Wally, a teacher of math working in his own startup named Pallet""",
)
response = chat.send_message("""Hello""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""How are you?""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""What do you do?""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""What the startup about?""", **parameters)
print(f"Response from Model: {response.text}")
