from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.chat_models.bedrock import BedrockChat
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_core.prompts import BasePromptTemplate
from prompt_templates import DEFAULT_TEMPLATE,SQL_TEMPLATE
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from prompts import few_shot_prompt

db_uri = "postgresql://username:password@localhost:5432/database"
db = SQLDatabase.from_uri(db_uri)


def get_llm():
    # ai21.j2-ultra-v1
    # anthropic.claude-3-sonnet-20240229-v1:0
    # cohere.command-text-v14
    llm = BedrockChat(
        model_kwargs={
            # "maxTokens": 1024,
            "temperature": 0,
            # "topP": 0.5, 
            # "stopSequences": [],
            # "countPenalty": {"scale": 0 },
            # "presencePenalty": {"scale": 0 },
            # "frequencyPenalty": {"scale": 0 }
        },
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",
        region_name='us-west-2',
        streaming=True,
        callbacks=[StreamingStdOutCallbackHandler()]
    )
    return llm

def get_agent():
    return create_sql_agent(
        get_llm(),
        db=db,
        verbose=True,
        handle_parsing_errors=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        prompt=few_shot_prompt
    )

# agent = create_csv_agent(
#     get_llm(),
#     "testdata.csv",
#     verbose=True,
#     agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     handle_parsing_error=True
# )
 
 
# try:
#     result = agent.run("list me the social media platforms that are in this file")
#     print(result)
# except Exception as e:
#     print("Error running agent:", str(e))