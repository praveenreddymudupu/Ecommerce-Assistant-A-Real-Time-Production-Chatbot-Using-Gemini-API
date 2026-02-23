# Ecommerce-Assistant-A-Real-Time-Production-Chatbot-Using-Gemini-API
# Smart Shopping Assistant
A Real-Time Production E-Commerce Chatbot using Gemini API
 # Project Overview
*  Smart Shopping Assistant is a production-ready, domain-specific E-Commerce chatbot built using Google Gemini API and Streamlit.
*  The chatbot provides intelligent product recommendations, comparisons, order tracking simulation, and store policy assistance through a clean conversational interface.
*  The project follows clean architecture principles and is deployed on AWS EC2 for real-time public access.
  
  # Key Features
*  Real-time AI-powered product recommendations
*  Multi-turn contextual conversation support
*  Structured and formatted product responses
*  Order tracking simulation
*  Store policy awareness
*  Modular backend architecture
*  Secure API key management using environment variables
*  Cloud deployment on AWS EC2
*  Production-ready project structure

# Tech Stack
**Frontend/UI:** Streamlit

**LLM:** Google Gemini API

**Backend:** Python

**Cloud Deployment:** AWS EC2

**Environment Management:** python-dotenv

**Version Control:** Git & GitHub

# System Architecture

User

  ↓
Streamlit UI

  ↓
Backend Service Layer

  ↓
Prompt Engineering Module

  ↓
Gemini API

  ↓
Response Processing

  ↓
UI Rendering

# Project Structure

ecommerce-genai-chatbot/

│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── backend/
│   ├── gemini_client.py
│   ├── prompt_manager.py
│   ├── memory_manager.py
│   └── product_context.py
│
├── utils/
│   └── logger.py
│
└── logs/

# Environment Variables
Create a .env file in the root directory:
GEMINI_API_KEY=your_api_key_here

# Installation (Local Setup)
**1.Clone Repository:**
git clone https://github.com/yourusername/ecommerce-genai-chatbot.git
cd ecommerce-genai-chatbot

**2.Create Virtual Environment:**
python -m venv my_env
source my_env/bin/activate   # Mac/Linux
my_env\Scripts\activate      # Windows

**3.Install Dependencies:**
pip install -r requirements.txt

**4.Run Application:**
streamlit run app.py

App will run on:
http://localhost:8501

# AWS EC2 Deployment Steps
**1.Launch EC2 Instance:**
Ubuntu
Open port 8501 in Security Group

**2.Upload Project:**
scp -r -i "your-key.pem" ecommerce-genai-chatbot ubuntu@your-ec2-ip:~

**3.SSH into EC2:**
ssh -i "your-key.pem" ubuntu@your-ec2-ip

**4.Install Dependencies:**
pip install -r requirements.txt

**5.Set Environment Variable:**
export GEMINI_API_KEY="your_api_key"

**6.Run in Background:**
nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &

**Access:**
http://your-ec2-ip:8501

# Prompt Engineering Strategy
The chatbot uses structured system prompts to:
*  Restrict responses to E-Commerce domain
*  Enforce consistent Markdown formatting
*  Limit to maximum 3 product recommendations
*  Provide Pros & Cons analysis
*  Handle store policies and order tracking.

# Example Queries
*  “Suggest best camera phones under ₹25,000.”
*  “Compare Vivo Y200 and Samsung Galaxy M34.”
*  “Track order ID ORD123.”
*  “What is your return policy?”

# Resume Description
  Developed and deployed a production-ready E-Commerce chatbot using Google Gemini API with modular backend architecture, structured prompt engineering, session-based memory, and AWS EC2 cloud deployment.
  
# Author
Praveen Reddy
