LLM-Powered Chatbot with FastAPI and SQL Integration

Overview

This project is a simple LLM-powered chatbot application built using Python (FastAPI) that allows users to input a free-text query. 
The system uses a Groq-hosted LLM endpoint to process the user's query and generate responses based on data stored in a SQL database.

Prerequisites

Python 3.8+

FastAPI

SQL database 

Groq API key

Setup

1.Clone the repository: git clone https://github.com/your-repo/llm-chatbot.git

2.Install dependencies: pip install -r requirements.txt

3.Create a .env file with the following variables:

    - GROQ_API_KEY: Your Groq API key
    
    - DATABASE_URL: Your SQL database URL
    
4.Initialize the database: python init_db.py

Run


1.Start the FastAPI server: uvicorn main:app --reload

2.Access the chatbot interface at http://localhost:8000

3.npm start

4.API Endpoints
/chat: Send a query to the chatbot and receive a response

Notes

Make sure to replace the GROQ_API_KEY and DATABASE_URL placeholders in the .env file with your actual credentials.




