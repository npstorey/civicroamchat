# civicroamchat

Civic Roam Chat is a document search and question-answering system that uses OpenAI's GPT-4 model for text embeddings and Pinecone for vector storage and similarity search.

The system is designed to help users search through documents relevant to civic functioning and governance.

Civic Raom extends the domain of specific civic information that can be queried with a LLM enabled Chatbot.

So far, Civic Roam is focused on New York City.

The current version of Civic Roam is a proof of concept that has only created embeddings based on 19 pdf documents from the NYC Department of Transportation published on the NYC Government Publications Portal (https://a860-gpp.nyc.gov/collections/zw12z528p?locale=en).

## Overview

This project includes the following steps:

1. Scrape html from public websites to collect a list of download links for reports.
2. Download documents.
3. Process and chunk the documents into manageable pieces.
4. Use OpenAI's GPT-4 model to generate embeddings for the chunks.
5. Store the embeddings in Pinecone for fast similarity search.
6. Use a pre-trained question-answering model to answer user queries based on the most relevant documents.

## Usage

To use Civic Roam Chat, follow these steps:

1. Set up a Pinecone account and obtain API keys for Pinecone and OpenAI.
2. Store the API keys in a `.env` file in the project directory.
3. Run the Jupyter Notebook to execute the steps outlined above.

## Example Questions

Here are some example questions you can ask the system:

- Can you summarize the main goals of Vision Zero?
- What specific actions has dot taken to reduce pedestrian crashes in bronx community board 6? For each action, mention the name of the report that it comes from.
- How many total citibike trips were there in december 2013?

While some of these questions can be answered by GPT-4 or another generally trained LLM, but adding embeddings from the NYC civic context creates better results for many questions.

## TO DOS

- Clean up and document existing code
- Extend the embeddings to all documents on the NYC Government Publications Portal
- Extend embeddings to The City Record Online (https://a856-cityrecord.nyc.gov/)
- Extend embeddings to NYC Charter (https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCcharter/0-0-0-1)
- Extend embeddings to NYC Administrative Code (https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-1)
- Extend embeddings to Rules of New York City (https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-1)
- Extend embeddings to New York City Council Legislation (https://legistar.council.nyc.gov/Legislation.aspx)
- Extend embeddings to NYC gov website (https://www.nyc.gov/)
- Extend embeddings to NYC Open Data (https://opendata.cityofnewyork.us/)
- Extend embeddings to We Gov website that aggregates data about NYC (https://wegov.nyc/)
- Extend embeddings to other sources
- Create a user interface where users can easily ask questions and receive responses from the chatbot
- Ongoing testing and refinement
- Deploy the Civic Roam chatbot and user interface to a production environment, making it accessible to users
- Ongoing maintenance and updates, including schedule for updating data

## Dependencies

The Doris Project requires the following Python packages:

- pinecone
- openai
- langchain
- python-dotenv
- tiktoken

## AI Ackowledgement

This project was created by Nathan Storey, in consultation with ChatGPT using the GPT-4 model.

## License

The Doris Project is released under the [MIT License](LICENSE).