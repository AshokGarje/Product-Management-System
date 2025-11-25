# 📦 Product Management System

A full-stack web application built using **React (Frontend)** and
**FastAPI (Backend)** to manage product data with CRUD operations.

## 🚀 Tech Stack

### Frontend

-   React.js
-   CSS
-   Axios

### Backend

-   FastAPI
-   SQLAlchemy
-   MySQL
-   Python Dotenv

## 📁 Project Structure

    Product-Management-System/
    │
    ├── backend/
    │   ├── main.py
    │   ├── models/
    │   ├── routes/
    │   ├── database.py
    │   ├── .env
    │   ├── requirements.txt
    │
    ├── frontend/
    │   ├── src/
    │   ├── public/
    │   ├── package.json
    │
    └── .gitignore
    └── README.md

## ⚙️ Backend Setup (FastAPI)

### 1️⃣ Go to backend folder

    cd backend

### 2️⃣ Install dependencies

    pip install -r requirements.txt

### 3️⃣ Create `.env` file

    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=yourpassword
    DB_NAME=productdb

### 4️⃣ Run FastAPI server

    uvicorn main:app --reload

Backend URL: **http://localhost:8000**

## 🎨 Frontend Setup (React)

### 1️⃣ Go to frontend folder

    cd frontend

### 2️⃣ Install dependencies

    npm install

### 3️⃣ Start frontend

    npm start

Frontend URL: **http://localhost:3000**

## 🔗 API Base URL

    http://localhost:8000

Example:

``` js
axios.get("http://localhost:8000/products");
```

## ✨ Features

-   Add products
-   Edit products
-   Delete products
-   View all products
-   MySQL database integration
-   Fast REST APIs (FastAPI)
-   Clean UI (React)

## 📷 Screenshots

Add screenshots inside:

    /screenshots

## 📤 Deployment Options

-   Frontend: Netlify / Vercel
-   Backend: Render / Railway
-   Database: Railway / ClearDB

## 🤝 Contributing

Pull requests are welcome.

## 📝 License

MIT License
