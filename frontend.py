import streamlit as st
from langchain.callbacks.base import BaseCallbackHandler
from prompt_templates import DEFAULT_TEMPLATE,SQL_TEMPLATE

from chatbot import get_agent
st.title("🤖 Chat with AIuda")
st.subheader("Example Questions:")
st.markdown("- How many assets do we have for the project_group Red Bull Cerro Abajo?")
st.markdown("- From how many platforms do we have data? I am only interested in Assets that containt Red Bull Cerro Abajo projects?")
st.markdown("- What was the asset with the most views? Return the me the VIN, views, platform and project title")
st.markdown("- Wich platform has the most views? Tell me how many views the platform got")

INIT_MESSAGE = {"role": "assistant",
                "content": "Hi! I'm AIuda on Bedrock. How may I help you?"}

class StreamHandler(BaseCallbackHandler):
    def __init__(self, container):
        self.container = container
        self.text = ""

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)


def init_conversationchain():
    conversation = get_agent()

    # Store LLM generated responses

    if "messages" not in st.session_state.keys():
        st.session_state.messages = [INIT_MESSAGE]

    return conversation

def generate_response(conversation, input_text):
    return conversation.run(input=input_text, callbacks=[StreamHandler(st.empty())])

# Re-initialize the chat
def new_chat() -> None:
    st.session_state["messages"] = [INIT_MESSAGE]
    st.session_state["langchain_messages"] = []
    conv_chain = init_conversationchain()


# Initialize the chat
conv_chain = init_conversationchain()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User-provided prompt
prompt = st.chat_input()

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        # print(st.session_state.messages)
        response = generate_response(conv_chain, prompt)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)