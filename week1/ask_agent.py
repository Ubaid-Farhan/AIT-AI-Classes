from agents import Agent, Runner
from llm import model


def ask_agent(prompt, role='helpful assistant'):
    agent = Agent(
        name='Helper 3',
        instructions=f'You are a {role}. Answer in 3 short lines.',
        model=model,
    )
    result = Runner.run_sync(agent, prompt)
    return result.final_output


prompt = input('Sawal: ')


print(ask_agent(prompt))
print('---')
print(ask_agent(prompt, role='strict teacher'))