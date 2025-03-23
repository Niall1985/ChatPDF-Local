from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from llm_helper import llm

def truncate_text(text, max_tokens=5000):
    words = text.split()
    return " ".join(words[:max_tokens])

def generate_response(user_query, cleaned_text):
    cleaned_text = truncate_text(cleaned_text)

    prompt = """
        You are an AI assistant specializing in document analysis.
        Given the cleaned text from a PDF, extract the most relevant information to answer the user's query.

        ### Document Content:
        {cleaned_text}

        ### User Query:
        {user_query}

        ### Instructions:
        - Provide only the most relevant portion of the text.
        - Ensure factual accuracy.
        - If no relevant content is found, respond with: "No relevant information found."

        ### Return the extracted answer in a summarized form, and just return the content, don't return the meta-data like calls used etc:
    """
    
    pt = PromptTemplate.from_template(prompt)
    chain = pt | llm

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(cleaned_text)

    responses = []
    for chunk in chunks:
        response = chain.invoke(
            {"user_query": user_query, "cleaned_text": chunk},
            config={"max_tokens": 500} 
        )
        responses.append(response)
    
    return "\n".join(str(response) for response in responses)

