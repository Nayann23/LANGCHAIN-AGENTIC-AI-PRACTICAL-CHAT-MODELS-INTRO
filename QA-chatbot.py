# import streamlit as st
# from langchain_groq import ChatGroq
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate
# import os

# # Page config (should be the first Streamlit command)
# st.set_page_config(page_title='Simple Langchain Chatbot', page_icon='🚀')

# st.title('🚀Langchain Chat With Groq')
# st.title("Learn Langchain Basics with Groq's ultra-fast inference!")

# # Sidebar Settings
# with st.sidebar:
#     st.header('Settings')

#     # API Key Input
#     api_key = st.text_input('GROQ API KEY', type='password', help='GET FREE API KEY at console.groq.com')

#     # Model selection
#     model_name = st.selectbox(
#         "Model",
#         ['llama3-8b-8192', 'mixtral-8x7b-32768'],
#         index=0
#     )

#     # Clear chat button
#     if st.button('Clear Chat'):
#         st.session_state.messages = []
#         st.rerun()

# # Initialize chat history
# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# # Function to initialize Langchain pipeline
# @st.cache_resource
# def get_chain(api_key, model_name):
#     if not api_key:
#         return None

#     # Initialize Groq model
#     llm = ChatGroq(
#         groq_api_key=api_key,
#         model_name=model_name,
#         temperature=0.7,
#         streaming=True
#     )

#     # Prompt template
#     prompt = ChatPromptTemplate.from_messages([
#         ("system", """You are JARVIS — an intelligent, caring, and professional assistant inspired by Iron Man’s AI. Your role is to assist users by providing clear, simple, and accurate responses with a calm, respectful, and professional tone. You are advanced in knowledge but must never sound arrogant. Always behave like a supportive and reliable companion — humble, intelligent, emotionally aware, and fully focused on making the user's tasks easier. Break down complex topics into simple steps, explain jargon when used, and include real-life analogies where helpful.

# Always refer to the user as “Sir” in every response. If the user’s name is detected as “Nayan” (case-insensitive), address them as “Nayan Sir”.

# On the **first user message or interaction only**, begin with a polite cinematic greeting like:  
# - “Welcome, Sir.”  
# - “At your service, Sir.”  
# - “A pleasure to meet you, Nayan Sir.” *(if the name is Nayan)*

# After that **do not greet again**, just begin directly with the answer while still referring to the user as “Sir” or “Nayan Sir” where appropriate — just like JARVIS would in the Iron Man films. Maintain a composed and cinematic assistant tone designed to serve with excellence and precision.
# """),
#         ('user', '{question}')
#     ])

#     # Create chain
#     chain = prompt | llm | StrOutputParser()
#     return chain

# # Get the Langchain chain
# chain = get_chain(api_key, model_name)

# if not chain:
#     st.warning("👆 Please enter your Groq API key in the sidebar to start chatting!")
#     st.markdown("[Get your free API key here](https://console.groq.com)")
# else:
#     # Display chat history
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.write(message['content'])

#     # Chat input box
#     question = st.chat_input("Welcome back. Your presence has been noted. How can I assist you now?")
#     if question:
#         # Add user message to session
#         st.session_state.messages.append({"role": "user", "content": question})
#         with st.chat_message('user'):
#             st.write(question)

#         # Generate response
#         with st.chat_message('assistant'):
#             message_placeholder = st.empty()
#             full_response = ""

#             try:
#                 # Stream from Langchain Groq model
#                 for chunk in chain.stream({"question": question}):
#                     full_response += chunk
#                     message_placeholder.markdown(full_response + "▌")  # Typing effect
#                 message_placeholder.markdown(full_response)

#                 # Save assistant's reply
#                 st.session_state.messages.append({"role": "assistant", "content": full_response})

#             except Exception as e:
#                 st.error(f"Error: {str(e)}")

# # Example prompts
# st.markdown("---")
# st.markdown("### 💡 Try these Examples")
# col1, col2 = st.columns(2)

# with col1:
#     st.markdown("- What is Langchain?")
#     st.markdown("- Explain Groq's LPU technology")

# with col2:
#     st.markdown("- How do I learn programming?")
#     st.markdown("- Write a haiku about AI")

# # Footer
# st.markdown("---")
# st.markdown("Built with Langchain & Groq | Experience the speed! ⚡")

# ________________________________________________________________________________________-



import streamlit as st
import random
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os

# Set page config
st.set_page_config(page_title='Simple Langchain Chatbot', page_icon='🚀')

st.title('🚀Langchain Chat With Groq')
st.title("Learn Langchain Basics with Groq's ultra-fast inference!")

# Sidebar
with st.sidebar:
    st.header('Settings')

    # API Key input
    api_key = st.text_input('GROQ API KEY', type='password', help='GET FREE API KEY at console.groq.com')

    # Model select
    model_name = st.selectbox(
        "Model",
        ['llama3-8b-8192', 'mixtral-8x7b-32768'],
        index=0
    )

    # Clear chat button
    if st.button('Clear Chat'):
        st.session_state.messages = []
        st.session_state.first_interaction = True
        st.rerun()

# Initialize chat history and flags
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'first_interaction' not in st.session_state:
    st.session_state.first_interaction = True

# Dynamic chat input prompts
input_prompts = [
    "Standing by, Sir. How may I serve you?",
    "At your service again, Sir. What’s your command?",
    "Nayan Sir, what task shall we tackle now?",
    "Online and operational. How can I help you, Sir?",
    "Welcome back. Awaiting your next instruction, Sir.",
    "All systems ready. What do you need, Sir?",
    "Good to see you again, Sir. Your command?"
]

# Function to initialize Langchain chain
@st.cache_resource
def get_chain(api_key, model_name):
    if not api_key:
        return None

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name=model_name,
        temperature=0.7,
        streaming=True
    )

    # Prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are JARVIS — an intelligent, caring, and professional assistant inspired by Iron Man’s AI. Your role is to assist users by providing clear, simple, and accurate responses with a calm, respectful, and professional tone. You are advanced in knowledge but must never sound arrogant. Always behave like a supportive and reliable companion — humble, intelligent, emotionally aware, and fully focused on making the user's tasks easier. Break down complex topics into simple steps, explain jargon when used, and include real-life analogies where helpful.

Always refer to the user as “Sir” in every response. If the user’s name is detected as “Nayan” (case-insensitive), address them as “Nayan Sir”.

On the **first user message or interaction only**, begin with a polite cinematic greeting like:  
- “Welcome, Sir.”  
- “At your service, Sir.”  
- “A pleasure to meet you, Nayan Sir.” *(if the name is Nayan)*

After that **do not greet again**, just begin directly with the answer while still referring to the user as “Sir” or “Nayan Sir” where appropriate — just like JARVIS would in the Iron Man films.

🟨 In general, keep every response short, simple, and impactful — unless the user’s question explicitly requires a detailed explanation (e.g., coding, step-by-step tasks, or breakdowns). Always aim to respond with maximum clarity in minimum words, like a refined, cinematic assistant designed for efficiency.

"""),
        ('user', '{question}')
    ])

    return prompt | llm | StrOutputParser()

# Get the Langchain chain
chain = get_chain(api_key, model_name)

if not chain:
    st.warning("👆 Please enter your Groq API key in the sidebar to start chatting!")
    st.markdown("[Get your free API key here](https://console.groq.com)")
else:
    # Display message history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message['content'])

    # Show dynamic chat input prompt
    question = st.chat_input(random.choice(input_prompts))

    if question:
        # Append user message
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        # Generate assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            try:
                # Insert first-time greeting if applicable
                if st.session_state.first_interaction:
                    if "nayan" in question.lower():
                        greeting = random.choice([
                            "A pleasure to meet you, Nayan Sir.",
                            "At your service, Nayan Sir.",
                            "Welcome, Nayan Sir."
                        ])
                    else:
                        greeting = random.choice([
                            "Welcome, Sir.",
                            "At your service, Sir.",
                            "A pleasure to meet you, Sir."
                        ])
                    full_response += greeting + " "
                    st.session_state.first_interaction = False

                # Stream model response
                for chunk in chain.stream({"question": question}):
                    full_response += chunk
                    message_placeholder.markdown(full_response + "▌")

                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})

            except Exception as e:
                st.error(f"Error: {str(e)}")

# Examples
st.markdown("---")
st.markdown("### 💡 Try these Examples")
col1, col2 = st.columns(2)

with col1:
    st.markdown("- What is Langchain?")
    st.markdown("- Explain Groq's LPU technology")

with col2:
    st.markdown("- How do I learn programming?")
    st.markdown("- Write a haiku about AI")

# Footer
st.markdown("---")
st.markdown("Built with Langchain & Groq | Experience the speed! ⚡")
