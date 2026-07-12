import React, { useState } from "react";
import { analyzeResume } from "../services/api";

const AnalysisSection = () => {
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    try {
      setLoading(true);
      const data = await analyzeResume();
      setAnalysis(data);
    } catch (error) {
      setAnalysis({
        error: error.response?.data?.detail || "Failed to analyze resume."
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Resume vs Job Description Analysis</h2>

      <button onClick={handleAnalyze} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>

      {analysis?.error && <p className="error-text">{analysis.error}</p>}

      {analysis && !analysis.error && (
        <div className="result-box">
          <div className="analysis-block">
            <h3>Matching Skills</h3>
            <ul>
              {(analysis.matching_skills || []).map((skill, idx) => (
                <li key={idx}>{skill}</li>
              ))}
            </ul>
          </div>

          <div className="analysis-block">
            <h3>Missing Skills</h3>
            <ul>
              {(analysis.missing_skills || []).map((skill, idx) => (
                <li key={idx}>{skill}</li>
              ))}
            </ul>
          </div>

          <div className="analysis-block">
            <h3>Resume Improvements</h3>
            <ul>
              {(analysis.resume_improvements || []).map((item, idx) => (
                <li key={idx}>{item}</li>
              ))}
            </ul>
          </div>

          <div className="analysis-block">
            <h3>Best Matching Projects</h3>
            <ul>
              {(analysis.best_matching_projects || []).map((project, idx) => (
                <li key={idx}>{project}</li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
};

export default AnalysisSection;