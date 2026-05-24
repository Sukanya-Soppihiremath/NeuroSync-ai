from services.openai_service import ask_ai

def coding_agent(prompt):

    final_prompt=f"""

    Solve coding task:

    {prompt}

    """

    return ask_ai(
        final_prompt
    )