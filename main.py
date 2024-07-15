import chain
import connect_confluance
import Generate_embedding
import retrival
from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain_community.chat_models import ChatOllama


local_path='data.html'

if local_path:
    #load pdf data
    # loader = UnstructuredPDFLoader(file_path=local_path)
    #load urldata
    # loader = WebBaseLoader("https://www.miniorange.com/about_us")
    data=''''''
    print('welcome_1')
    html_data=connect_confluance.gate_data_confluance()
    print(22)
    for i in html_data:
        with open('data.html', "a") as file:
                print(i)
                file.write(i)
    print(33)
    loader = UnstructuredHTMLLoader(local_path)
    data = loader.load()
print(data)
vector_db_new =Generate_embedding.embedding(data)
print(44)
local_model = "llama3"
llm = ChatOllama(model=local_model)
retrival=retrival.retrival(vector_db_new,llm)
chains=chain.chain(retrival,llm)

while True:
    print(chains.invoke(input("Hi,How can I Help you!:-")))
