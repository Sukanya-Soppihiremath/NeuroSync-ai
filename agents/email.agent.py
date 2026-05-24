from services.openai_service import ask_ai

def email_agent(prompt):

    final_prompt=f"""

    Write professional email.

    {prompt}

    """

    return ask_ai(
        final_prompt
    )