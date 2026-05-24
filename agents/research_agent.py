from services.openai_service import ask_ai

def research_agent(prompt):

    final_prompt=f"""

    Research this:

    {prompt}

    """

    return ask_ai(
        final_prompt
    )