# 🛠️ CDP Chatbot  

This is a **CDP Chatbot** designed to process queries related to **Customer Data Platforms (CDPs)**. It extracts relevant information from **Segment, mParticle, Lytics, and Zeotap** documentation and returns answers based on user queries.  

📌 **Current Implementation:**  
✔ Backend API built with **Python (Flask/FastAPI)**  
✔ Query processing from **preloaded text files**  
✔ Tested using **Postman**  

---

## 🚀 Features  
✅ Extracts answers from CDP documentation  
✅ Supports natural language queries  
✅ Works as a **backend API** (tested via Postman)  
✅ Lightweight and easy to set up  

---

## 🏗️ Installation & Setup  

### **🔹 Prerequisites**  
Ensure you have the following installed:  
- 🐍 **Python 3.x**  
- 📦 **pip (Python package manager)**  

### **🔹 Steps to Set Up**  
1️⃣ **Clone the repository:**  
   ```sh
   git clone <your-github-repo-url>
   cd cdp_chatbot
```
2️⃣ **Create a virtual environment & activate it:**
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

```
3️⃣ **Install dependencies:**
```sh
pip install -r requirements.txt
```


# ⚡ Usage
## 🖥️ Running the Chatbot API
Start the chatbot server:
```sh
python app.py   # If using Flask
uvicorn app:app --reload  # If using FastAPI
```

# 📂 Project Structure
```sh
cdp_chatbot/
│── app.py                  # Main application file
│── requirements.txt         # Dependencies
│── README.md                # Project documentation
│── data/                    # Preloaded documentation files
│── tests/                   # Test cases (if applicable)
```
## 🔗 GitHub Repository  

# Visit the project repository here:
```sh
https://github.com/<your-github-username>/cdp_chatbot
```

# Clone the repository using:
```sh
git clone https://github.com/<your-github-username>/cdp_chatbot.git
```

