import React, { useState } from "react";
import UploadSection from "./components/UploadSection";
import ChatSection from "./components/ChatSection";
import AnalysisSection from "./components/AnalysisSection";
import InterviewSection from "./components/InterviewSection";
import TellMeSection from "./components/TellMeSection";

function App() {
  const [isUploaded, setIsUploaded] = useState(false);

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>AI Interview Prep Assistant</h1>
        <p>
          Upload your resume and a job description, then analyze fit, ask
          questions, generate interview questions, and prepare your introduction.
        </p>
      </header>

      <UploadSection onUploadSuccess={() => setIsUploaded(true)} />

      {isUploaded && (
        <>
          <ChatSection />
          <AnalysisSection />
          <InterviewSection />
          <TellMeSection />
        </>
      )}
    </div>
  );
}

export default App;