from agents.email_agent import email_agent

from agents.research_agent import research_agent

from agents.coding_agent import coding_agent


def coordinator(prompt):

    prompt=prompt.lower()

    if "email" in prompt:

        return email_agent(
            prompt
        )

    elif "code" in prompt:

        return coding_agent(
            prompt
        )

    else:

        return research_agent(
            prompt
        )