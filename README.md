# 🧒 Missing Child Information Portal

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📌 Project Overview

The **Missing Child Information Portal** is a web-based platform designed to help users upload, search, and share information about missing children. The system allows individuals to report missing child cases and enables others to view and help by contacting the concerned person or authority.

This project is developed as a **demo awareness platform** demonstrating how modern web technologies can be applied to solve real-life social issues.

---

## 🚀 Features

### 🔐 Authentication & Security
- User Registration and Login
- Password Hashing using **bcrypt**
- Token-based Authentication using **PyJWT**
- Protected API Routes

### 👶 Missing Child Case Management
- Upload Missing Child Details
- Store Child Information with Image Support
- Browse and View Case Reports
- Contact Details for Reporting

### 🗄️ Database & Storage
- Case Data stored using **MongoDB**
- Image/File Storage handled using **Supabase**

### 🌐 User Interface
- Interactive and user-friendly UI using **Streamlit**
- RESTful Backend using **FastAPI**
- Request Validation using **Pydantic**

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- PyJWT
- bcrypt
- Pydantic

### Frontend
- Streamlit

### Storage
- MongoDB
- Supabase

### Deployment
- Backend → Render
- Frontend → Streamlit Cloud

---

## 📁 Project Structure

```
LITTLEHOPE/
│
├── backend/
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── password_hash.py      # Handles password hashing using bcrypt
│   │   ├── token_create.py       # JWT token creation and validation
│   │   └── user_valid.py         # Pydantic validation schemas
│   │
│   ├── main.py                   # FastAPI main backend application
│   ├── requirements.txt          # Backend dependencies
│
├── frontend/
│   ├── pages/
│   │   ├── childs_details.py     # Displays missing child details
│   │   ├── districts.py          # State & district selection data
│   │   ├── home.py               # Homepage UI
│   │   ├── login_reg.py          # User login and registration page
│   │   ├── report_child.py       # Upload missing child case
│   │   ├── setting.py            # User settings page
│   │   ├── terms_and_conditions.py # Terms & policies page
│   │   └── your_posts.py         # User uploaded posts
│   │
│   └── frontend_main.py          # Streamlit main entry file
│
├── .env                          # Environment variables (MongoDB, JWT, Supabase etc.)
├── .gitignore                    # Ignored files for Git
├── img.png                       # Project banner / UI screenshot
└── requirements.txt              # Frontend dependencies
```

---



---



## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/missing-child-portal.git
cd missing-child-portal
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment:

#### Windows
```bash
venv\Scripts\activate
```

#### Linux / Mac
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```
MONGO_URL=your_mongodb_connection
JWT_SECRET=your_secret_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

---

### 5️⃣ Run Backend Server

```bash
uvicorn backend.main:app --reload
```

Backend runs on:
```
http://127.0.0.1:8000
```

---

### 6️⃣ Run Frontend

```bash
streamlit run frontend/_frontend_main.py
```

---

## 📡 API Endpoints



## 🌍 Real Life Use Case

This system demonstrates how community-driven platforms can help spread awareness about missing children. Similar platforms can be extended to support:

- NGO collaborations
- Law enforcement reporting
- Public awareness campaigns
- Emergency response systems

---

## 🧪 Future Improvements(working..)

- AI-based Face Recognition
- Location-based Alerts
- Mobile App Integration
- Admin Verification System
- Email & SMS Notifications

---

## ⚠️ Disclaimer

This project is developed for **educational and demonstration purposes only**.  
Users should avoid uploading real personal or sensitive information.

---

## 🚀 Deployment

| Service | Platform |
|------------|----------------|
| Backend | Render |
| Frontend | Streamlit Cloud |
| Storage | mongodb atlas | Supabase |

---

## 🤝 Contribution Guidelines

Contributions are welcome!

### Steps:
1. Fork the repository
2. Create a new branch
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes
   ```bash
   git commit -m "Added new feature"
   ```
4. Push branch
   ```bash
   git push origin feature-name
   ```
5. Open Pull Request

---

## 🐛 Reporting Issues

If you find bugs or want to request a feature, open an issue in the repository.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Masud Mallik**

If you liked this project, consider giving it a ⭐ on GitHub!
