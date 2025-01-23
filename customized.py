# Import necessary packages
import os
import pickle
from omegaconf import OmegaConf

from google.auth.transport.requests import Request

from google_auth_oauthlib.flow import InstalledAppFlow
from llama_index.core import VectorStoreIndex, download_loader
from llama_index.readers.google import GoogleDocsReader


def authorize_gdocs():
    google_oauth2_scopes = [
        "https://www.googleapis.com/auth/documents.readonly"
    ]
    cred = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", 'rb') as token:
            cred = pickle.load(token)
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", google_oauth2_scopes)
            cred = flow.run_local_server(port=0)
        with open("token.pickle", 'wb') as token:
            pickle.dump(cred, token)

if __name__ == "__main__":
    conf = OmegaConf.load('config.yml')
    os.environ['OPENAI_API_KEY'] = conf.API_KEY
    # function to authorize or download latest credentials 
    authorize_gdocs()

    # initialize `LLamaIndex` google doc reader 
    # GoogleDocsReader = download_loader('GoogleDocsReader')

    # list of google docs we want to index 
    gdoc_ids = ['your_google_doc_ids']

    loader = GoogleDocsReader()

    # load gdocs and index them 
    documents = loader.load_data(document_ids=gdoc_ids)
    index = VectorStoreIndex.from_documents(documents)

    # Save your index to a index.json file
    # index.save_to_disk('index.json')
    # # Load the index from your saved index.json file
    # index = VectorStoreIndex.load_from_disk('index.json')

    # Querying the index
    while True:
        chat_input = input("User message: ") # Sample question: "Có bao nhiêu nhóm giấy tờ cần cung cấp trong hồ sơ ứng tuyển"
        query_engine = index.as_query_engine()
        response = query_engine.query(chat_input)
        print(f"System response: {response}")


        