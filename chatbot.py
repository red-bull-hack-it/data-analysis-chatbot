from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_community.llms import Bedrock
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
 
 
def get_llm():
    model_kwargs = { 
        "maxTokens": 1024, 
        "temperature": 0, 
        "topP": 0.5, 
        "stopSequences": [], 
        "countPenalty": {"scale": 0 }, 
        "presencePenalty": {"scale": 0 }, 
        "frequencyPenalty": {"scale": 0 } 
    }
    # ai21.j2-ultra-v1
    # anthropic.claude-3-sonnet-20240229-v1:0
    # cohere.command-text-v14
    llm = Bedrock(
        model_id="amazon.titan-text-express-v1",
        region_name='us-west-2',
        streaming=True,
        callbacks=[StreamingStdOutCallbackHandler()],
    )
    return llm
 
 
agent = create_csv_agent(
    get_llm(),
    "testdata.csv",
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_error=True
)
 
 
try:
    result = agent.run("list me the social media platforms that are in this file")
    print(result)
except Exception as e:
    print("Error running agent:", str(e))