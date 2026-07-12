import React, { useState } from "react";
import ReactMarkdown from "react-markdown";
import { askQuestion } from "../services/api";

const ChatSection = () => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;

    try {
      setLoading(true);
      setAnswer("");
      setSources([]);

      const data = await askQuestion(question);
      setAnswer(data.answer || "No answer returned.");
      setSources(data.sources || []);
    } catch (error) {
      setAnswer(error.response?.data?.detail || "Failed to get answer.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Ask Questions</h2>

      <textarea
        rows="4"
        placeholder="Ask something like: What skills are missing in my resume for this role?"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={handleAsk} disabled={loading}>
        {loading ? "Generating..." : "Ask"}
      </button>

      {answer && (
        <div className="result-box">
          <h3>Answer</h3>
          <div className="markdown-answer">
            <ReactMarkdown>{answer}</ReactMarkdown>
          </div>
        </div>
      )}

      {sources.length > 0 && (
        <div className="result-box">
          <h3>Sources</h3>
          {sources.map((source, index) => (
            <div key={index} className="source-card">
              <p><strong>Document Type:</strong> {source.document_type || "N/A"}</p>
              <p><strong>Page:</strong> {source.page || "N/A"}</p>
              <p>{source.text}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ChatSection;