from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_qdrant import QdrantVectorStore
# from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os


load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") # type: ignore

# Load and split the PDF
pdf_path = Path(__file__).parent / "sample.pdf"
loader = PyPDFLoader(str(pdf_path))
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# Embedding and Vector DB setup
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vector_store = QdrantVectorStore.from_documents(
    texts,
    embedding=embeddings,
    collection_name="learning langchain",
    url="http://localhost:6333"
)

retriever = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="learning langchain",
    url="http://localhost:6333"
)

# Define prompt template
prompt = PromptTemplate(
    template="""
You are a helpful assistant. You will be given a question and you will answer the question based on the context provided. If you don't know the answer, just say that you don't know. Do not try to make up an answer.

Context:
{context}

Question:
{question}

Answer:""",
    input_variables=["context", "question"]
)

llm = ChatOpenAI(model="gpt-4o", temperature=0.0)
chain = prompt | llm

# === 🔁 Loop to Ask Questions ===
while True:
    user_query = input("Ask your question (or type 'exit' to quit): ").strip()
    if user_query.lower() == "exit":
        break

    # Step 1: Retrieve relevant documents
    retrieved_docs = retriever.similarity_search(user_query)

    # Step 2: Combine content into a single string for context
    context = "\n\n".join(doc.page_content for doc in retrieved_docs)

    # Step 3: Ask LLM
    response = chain.invoke({
        "context": context,
        "question": user_query
    })

    # If using RunnableSequence, response is a string, not a dict
    print("\n💬 LLM Answer:\n", response.content)
    print("=" * 80)
    