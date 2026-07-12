import React, { useState } from "react";
import { generateInterviewQuestions } from "../services/api";

const InterviewSection = () => {
  const [questions, setQuestions] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleGenerateQuestions = async () => {
    try {
      setLoading(true);
      const data = await generateInterviewQuestions();
      setQuestions(data);
    } catch (error) {
      setQuestions({
        error:
          error.response?.data?.detail ||
          "Failed to generate interview questions."
      });
    } finally {
      setLoading(false);
    }
  };

  const renderList = (title, items) => (
    <div className="analysis-block">
      <h3>{title}</h3>
      <ul>
        {(items || []).map((item, idx) => (
          <li key={idx}>{item}</li>
        ))}
      </ul>
    </div>
  );

  return (
    <div className="card">
      <h2>Interview Questions</h2>

      <button onClick={handleGenerateQuestions} disabled={loading}>
        {loading ? "Generating..." : "Generate Interview Questions"}
      </button>

      {questions?.error && <p className="error-text">{questions.error}</p>}

      {questions && !questions.error && (
        <div className="result-box">
          {renderList("Technical Questions", questions.technical_questions)}
          {renderList("HR Questions", questions.hr_questions)}
          {renderList("Project Questions", questions.project_questions)}
          {renderList("Follow-up Questions", questions.follow_up_questions)}
        </div>
      )}
    </div>
  );
};

export default InterviewSection;