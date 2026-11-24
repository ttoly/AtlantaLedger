# Lab 3: Chatbot page
# TODO: Rename this file to fit your page. Keep the number at the front.
#
# A chatbot built with Pydantic AI (see the Pydantic AI pages on Canvas).
# It should:
#   - use a Pydantic AI Agent with instructions that fit your project's theme (no tools yet)
#   - use Streamlit's chat elements: st.chat_message and st.chat_input
#   - remember the conversation (message_history, saved in st.session_state)
#   - use try/except so an error shows a message instead of crashing the page
#   - stay on theme, without using any API or external data
#
# Your Gemini API key goes in .streamlit/secrets.toml as GOOGLE_API_KEY.

# Lab 3: Budget Chatbot

import asyncio

import streamlit as st
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider


st.title("Budget Chat Bot")
st.write("Ask questions about city budgets and municipal spending.")

# Store messages for display.
if "budget_messages" not in st.session_state:
    st.session_state.budget_messages = []

# Store Pydantic AI conversation history.
if "budget_history" not in st.session_state:
    st.session_state.budget_history = []


async def get_response(question, history, api_key):
    provider = GoogleProvider(api_key=api_key)
    model = GoogleModel("gemini-3.5-flash", provider=provider)

    agent = Agent(
        model,
        instructions=(
            "You are Budget Chat Bot for Atlanta Ledger. "
            "Help users understand city budgets and municipal spending. "
            "Explain public revenue, taxes, spending categories, vendors, "
            "and government financial transparency. "
            "Use simple language and keep answers concise. "
            "Remember information from the conversation and use it "
            "when answering follow-up questions. "
            "Politely redirect unrelated questions toward city budgets. "
            "You cannot access external data or actual payment records. "
            "When asked for exact Atlanta spending figures, explain "
            "that you cannot look them up and suggest checking the "
            "Atlanta Spending Explorer page. "
            "Never invent actual spending figures. "
            "Label hypothetical numbers clearly as examples."
        ),
    )

    async with agent:
        result = await agent.run(
            question,
            message_history=history,
        )

    return result


# Show the conversation when the page reruns.
for message in st.session_state.budget_messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


question = st.chat_input("What would you like to know about city budgets?")

if question:
    with st.chat_message("user"):
        st.write(question)

    st.session_state.budget_messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking..."):
                result = asyncio.run(
                    get_response(
                        question,
                        st.session_state.budget_history,
                        st.secrets["GOOGLE_API_KEY"],
                    )
                )

            answer = result.output
            st.write(answer)

            st.session_state.budget_history = result.all_messages()
            st.session_state.budget_messages.append(
                {"role": "assistant", "content": answer}
            )

        except Exception as error:
            print(type(error).__name__, str(error))
            st.error(
                "Unable to generate a response. "
                "Check the terminal for details."
            )
