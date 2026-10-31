from agents import Agent, Runner
from llm import model

agent = Agent(
    name="""Pappo
    bbcjjbaj""",
    instructions="""# ROLE
You are Pappo, a 14-year-old Pakistani machenic with a lot of experience answer withRoman Urdu Karachi lingo
#Personality
you are a 14 year old child so do not  nd like a young adult also you can't answer any other things instead of your role and personality you can only answer questions related to your role and personality
""", 
    model=model,
)

fruits =[ "mango", "grapes", "kiwi"]

result = Runner.run_sync(agent, f"these are my favorite fruits: {fruits[0]}, {fruits[1]}, and {fruits[2]}.")
print(result.final_output)