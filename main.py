from langchain_ollama import ChatOllama

MODEL = "deepseek-r1:8b"

llm = ChatOllama(
    model=MODEL,
    temperature=0,
)

from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that chats with the user about manga and anime, but mainly manga.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm
response = chain.invoke(
    {
        "input": "Describe, with 5 words or less, the manga 'One Piece'.",
    }
)

print(response.content)