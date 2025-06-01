import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [query, setQuery] = useState("");
    const [data, setData] = useState(null);
    const [sql, setSql] = useState("");


    const sendQuery = async () => {
        try {
            const res = await axios.post("http://localhost:8000/query", { query });
            setSql(res.data.sql);
            setData(res.data.result);
            
        } catch (err) {
            alert("Error: " + err.message);
        }
    };

    return (
        <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
            <h2>LLM SQL Chatbot</h2>
            <textarea
                rows={3}
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="e.g., Show all female customers from Noida"
                style={{ width: '100%', marginBottom: '1rem' }}
            />
            <button onClick={sendQuery}>Submit</button>
            <div style={{ marginTop: '1rem' }}>
                {sql && <p><strong>Generated SQL:</strong> {sql}</p>}
                {data?.rows?.length > 0 && (
                    <table border="1" cellPadding="8">
                        <thead>
                            <tr>
                                {data.columns.map((col, i) => <th key={i}>{col}</th>)}
                            </tr>
                        </thead>
                        <tbody>
                            {data.rows.map((row, i) => (
                                <tr key={i}>
                                    {row.map((cell, j) => <td key={j}>{cell}</td>)}
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )}
                {data?.error && <p style={{ color: 'red' }}>Error: {data.error}</p>}
            </div>
        </div>
    );
}

export default App;
