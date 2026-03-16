"use client"

import { useState } from "react"
import axios from "axios"

export default function Home() {

  const [file, setFile] = useState<File | null>(null)
  const [loading, setLoading] = useState(false)
  const [status, setStatus] = useState("")
  const [reportUrl, setReportUrl] = useState("")

  const uploadFile = async () => {

    if (!file) return

    const formData = new FormData()
    formData.append("file", file)

    setLoading(true)
    setStatus("Uploading dataset...")

    try {

      const res = await axios.post(
        "https://ai-data-analysis-agent-tgoc.onrender.com/analyze",
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      )

      setStatus("AI agent analyzing dataset...")
      
      setTimeout(() => {
        setLoading(false)
        setStatus("Report generated successfully 🎉")
        // setReportUrl("http://127.0.0.1:8000/reports/data_report.md")
         setReportUrl("https://ai-data-analysis-agent-tgoc.onrender.com/reports/data_report.md")
        

      }, 2000)

    } catch (error) {

      setLoading(false)
      setStatus("Error analyzing dataset")

    }

  }

  return (

    <main className="min-h-screen flex items-center justify-center bg-gray-100">

      <div className="bg-white shadow-xl rounded-xl p-10 w-[500px] text-center">

        <h1 className="text-3xl font-bold mb-2">
          AI Data Analysis Agent
        </h1>

        <p className="text-gray-500 mb-6">
          Upload a CSV dataset and let the AI analyze it
        </p>

        {/* File Upload */}
        <input
          type="file"
          accept=".csv"
          onChange={(e) => setFile(e.target.files?.[0] || null)}
          className="mb-4 w-full border p-2 rounded"
        />

        {/* Upload Button */}
        <button
          onClick={uploadFile}
          disabled={loading}
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition"
        >
          {loading ? "Analyzing Dataset..." : "Upload Dataset"}
        </button>

        {/* Loading Animation */}
        {loading && (
          <div className="mt-6 flex flex-col items-center">

            <div className="animate-spin rounded-full h-10 w-10 border-b-2 border-blue-600"></div>

            <p className="mt-3 text-gray-600">
              AI agent is analyzing your dataset...
            </p>

          </div>
        )}

        {/* Status */}
        {status && !loading && (
          <p className="mt-6 text-green-600 font-medium">
            {status}
          </p>
        )}

        {/* Download Report */}
        {reportUrl && (
          <div className="mt-6">

            <a
              href={reportUrl }
              // download
              target="_blank"
               rel="noopener noreferrer"
              className="bg-green-600 text-white px-6 py-2 rounded hover:bg-green-700 transition"
            >
              Download Report
            </a>

          </div>
        )}

      </div>

    </main>
  )
}
