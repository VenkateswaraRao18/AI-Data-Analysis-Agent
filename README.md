# AI Data Analysis Agent

An intelligent **AI-powered data analysis platform** that automatically explores datasets, generates visualizations, trains machine learning models, and produces a professional analytical report with AI-generated insights.

This system acts as an **autonomous data scientist**, capable of understanding datasets and producing meaningful insights with minimal user interaction.

---

# Project Overview

This project demonstrates how an **AI Agent architecture** can orchestrate multiple data science tools to perform automated data analysis.

The AI agent performs the following tasks automatically:

1. Dataset ingestion
2. Exploratory Data Analysis (EDA)
3. Visualization generation
4. Machine learning model training
5. Model evaluation
6. AI-powered insight generation
7. Professional analytical report creation

The final output is a **fully generated AI data analysis report** summarizing patterns in the data and model performance.

---

# Key Features

• Automated dataset analysis  
• AI-driven exploratory data analysis  
• Intelligent visualization generation  
• Machine learning model training and comparison  
• Automatic best model detection  
• AI-generated analytical insights  
• Downloadable analytical report  
• Interactive frontend dashboard  
• Modular AI agent architecture  

---

# System Architecture


Frontend (Next.js)
│
│ Upload dataset
▼
FastAPI Backend
│
│ AI Agent Controller
▼
Agent Planner
│
├── Data Loader
├── EDA Tool
├── Visualization Tool
├── Machine Learning Tool
└── Report Generator
│
▼
AI Insights (LLM)
│
▼
Generated Data Analysis Report



---

# AI Agent Workflow

When a dataset is uploaded:

1. AI agent loads the dataset
2. Performs exploratory data analysis
3. Generates correlation heatmaps and distributions
4. Identifies relationships between variables
5. Trains multiple machine learning models
6. Evaluates model performance
7. Selects the best performing model
8. Generates AI insights using LLM
9. Produces a professional analytical report

---

# Example Output

The generated report includes:

• Executive Summary  
• Dataset Overview  
• Feature Relationships  
• Model Performance  
• Key Predictive Factors  
• Conclusions  

---

# Technologies Used

## Backend

Python  
FastAPI  
Scikit-learn  
Pandas  
Matplotlib  
Seaborn  
Hugging Face Transformers  

## Frontend

Next.js  
React  
TailwindCSS  
Axios  

## AI Models

The system supports:

• Hugging Face open-source models  
• Gemini API (used for demo deployment)

---

# AI Model Strategy

Originally this project was designed to run **fully local AI models using Hugging Face Transformers** such as:

• TinyLlama  
• Mistral  
• Other open-source LLMs  

Running large models locally or in the cloud requires significant compute resources.

Therefore **for demo and deployment purposes**, this version uses an **API-based LLM** so that the system can be easily tested and demonstrated.

The architecture remains fully compatible with **local Hugging Face models**, and switching between models only requires modifying the LLM module.

---

# Installation

## Clone the repository

---

# AI Agent Workflow

When a dataset is uploaded:

1. AI agent loads the dataset
2. Performs exploratory data analysis
3. Generates correlation heatmaps and distributions
4. Identifies relationships between variables
5. Trains multiple machine learning models
6. Evaluates model performance
7. Selects the best performing model
8. Generates AI insights using LLM
9. Produces a professional analytical report

---

# Example Output

The generated report includes:

• Executive Summary  
• Dataset Overview  
• Feature Relationships  
• Model Performance  
• Key Predictive Factors  
• Conclusions  

---

# Technologies Used

## Backend

Python  
FastAPI  
Scikit-learn  
Pandas  
Matplotlib  
Seaborn  
Hugging Face Transformers  

## Frontend

Next.js  
React  
TailwindCSS  
Axios  

## AI Models

The system supports:

• Hugging Face open-source models  
• Gemini API (used for demo deployment)

---

# AI Model Strategy

Originally this project was designed to run **fully local AI models using Hugging Face Transformers** such as:

• TinyLlama  
• Mistral  
• Other open-source LLMs  

Running large models locally or in the cloud requires significant compute resources.

Therefore **for demo and deployment purposes**, this version uses an **API-based LLM** so that the system can be easily tested and demonstrated.

The architecture remains fully compatible with **local Hugging Face models**, and switching between models only requires modifying the LLM module.

---

# Installation

## Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-data-analysis-agent.git

cd ai-data-analysis-agent


---

# Backend Setup

Navigate to backend folder:

cd backend


Create virtual environment:


python -m venv venv


Activate environment

Windows:


venv\Scripts\activate


Install dependencies:


pip install -r requirements.txt


Run backend server:


uvicorn api.main:app --reload


Backend will run at:


http://localhost:8000


---

# Frontend Setup

Navigate to frontend folder:


cd frontend


Install dependencies:


npm install


Run frontend:


npm run dev


Frontend runs at:


http://localhost:3000


---

# Using the Application

1. Open the frontend interface
2. Upload a CSV dataset
3. The AI agent automatically analyzes the dataset
4. Visualizations and models are generated
5. AI insights are created
6. Download the generated report

---

# API Endpoint

Upload dataset:


POST /analyze


Example request:


curl -X POST -F "file=@dataset.csv" http://localhost:8000/analyze


---

# Project Structure


backend
│
├── agent
│ ├── brain.py
│ ├── planner.py
│ ├── agent_controller.py
│ └── executor.py
│
├── tools
│ ├── data_loader.py
│ ├── eda_tool.py
│ ├── visualization_tool.py
│ ├── ml_tool.py
│ ├── text_tool.py
│ └── report_tool.py
│
├── api
│ └── main.py
│
├── reports
│
└── uploaded_datasets
│
frontend
│
└── Next.js UI


---

# Demo Notes

For demonstration purposes:

• API-based LLM calls are used for stable execution  
• This allows the project to run without requiring expensive compute resources  

However the system architecture supports:

• Fully local Hugging Face models  
• Cloud GPU models  
• API-based models  

---

# Future Improvements

Planned enhancements:

• PDF report generation  
• Interactive visualization dashboard  
• Support for larger local models (Mistral, Llama)  
• Streaming AI reasoning  
• Cloud deployment support  
• Multi-dataset comparison  
• AutoML model selection  

---

# Screenshots

(Add screenshots of your UI here after deployment)

Example sections:


Upload Dataset Interface
Generated Report
Visualization Dashboard
Model Performance Table


---

# Author

Venkateswararao Jannegorla  

Graduate Student  
Machine Learning / Data Science  

---

# License

MIT License
