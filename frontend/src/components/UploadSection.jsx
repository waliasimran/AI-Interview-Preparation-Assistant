import React, { useState } from "react";
import { uploadDocuments } from "../services/api";

const UploadSection = ({ onUploadSuccess }) => {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState(null);
  const [loading, setLoading] = useState(false);
  const [uploadMessage, setUploadMessage] = useState("");

  const handleUpload = async () => {
    if (!resume || !jobDescription) {
      setUploadMessage("Please upload both resume and job description.");
      return;
    }

    try {
      setLoading(true);
      setUploadMessage("");
      const data = await uploadDocuments(resume, jobDescription);
      setUploadMessage(data.message || "Documents uploaded successfully.");
      onUploadSuccess();
    } catch (error) {
      setUploadMessage(
        error.response?.data?.detail || "Failed to upload documents."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Upload Resume & Job Description</h2>

      <div className="upload-group">
        <label>Resume</label>
        <input
          type="file"
          accept=".pdf,.txt"
          onChange={(e) => setResume(e.target.files[0])}
        />
      </div>

      <div className="upload-group">
        <label>Job Description</label>
        <input
          type="file"
          accept=".pdf,.txt"
          onChange={(e) => setJobDescription(e.target.files[0])}
        />
      </div>

      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Uploading..." : "Upload Documents"}
      </button>

      {uploadMessage && <p className="status-text">{uploadMessage}</p>}
    </div>
  );
};

export default UploadSection;