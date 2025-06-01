from fastapi import FastAPI, Request    
from pydantic import BaseModel
import sqlite3
import aiohttp
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = FastAPI()
# origins = ["http://localhost:3000"]
app.add_middleware(CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows all origins
    allow_credentials=True,  # Allows cookies to be included in requests
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
    



class QueryRequest(BaseModel):
    query: str
    
@app.post("/query")
async def process_query(request:QueryRequest):
    user_input= request.query
    
    prompt= f"You are a SQL expert. Convert this to SQLite SQL: {user_input}"  
    headers={
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    body = {
        "model": "llama-3.1-8b-instant",
        "messages":[
            {"role": "system", "content": """You are a data assistant. 
             Convert user queries into accurate SQL for a SQLite3 database.
             Do not include explanations, just the SQL query."""},
            {"role": "user", "content":prompt }
        ] 
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=body) as response:
                data = await response.json()
                sql_query = data['choices'][0]['message']['content'].strip("\n")
    except Exception as e:
        return{"error":f"failed to call LLM : {str(e)}"}
    
    try:
        conn = sqlite3.connect('chatbot.db')
        cursor = conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        conn.close()
        return {"sql": sql_query, "columns": columns, "rows": rows}
    except Exception as e:
        return {"sql": sql_query, "result": {"error": str(e)}}