import React, { useState } from "react";
import { generateTellMe } from "../services/api";

const TellMeSection = () => {
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    try {
      setLoading(true);
      const data = await generateTellMe();
      setAnswer(data.answer || "No response generated.");
    } catch (error) {
      setAnswer(
        error.response?.data?.detail ||
          "Failed to generate 'Tell me about yourself'."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Tell Me About Yourself</h2>

      <button onClick={handleGenerate} disabled={loading}>
        {loading ? "Generating..." : "Generate Answer"}
      </button>

      {answer && (
        <div className="result-box">
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
};

export default TellMeSection;