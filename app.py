from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool
import os
from dotenv import load_dotenv

load_dotenv()

model_id = "meta-llama/Llama-3.3-70B-Instruct"
model = HfApiModel(model_id=model_id, token=os.getenv(
    "HUGGINGFACEHUB_API_TOKEN"))
print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
agent = CodeAgent(tools=[DuckDuckGoSearchTool],
                  model=model)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)
