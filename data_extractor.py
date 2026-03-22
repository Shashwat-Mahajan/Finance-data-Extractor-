from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()
llm = ChatGroq(model_name="groq/compound")

def extract(text: str) -> dict:

    prompt = '''
    from the below news article, extract revenue ans eps in JSON format containing the following keys: 'revenue_expected','revenue_expected'
    ,'eps_actual','eps_expected'.
    
    Each value should have a unit such as million or billion.
    
    Only return the valid JSON, NO preamble.
    
    Article
    ========
    {article}   
    '''

    pt = PromptTemplate.from_template(prompt)

    global llm

    chain = pt | llm | StrOutputParser()
    response = chain.invoke({'article': text})
    parser = JsonOutputParser()
    res = parser.parse(response)

    return res
