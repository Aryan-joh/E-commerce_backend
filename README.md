# 🛒 FastAPI E-commerce Backend API with MongoDB

This project is a sample backend application built with **FastAPI** and **MongoDB** using **Motor** (an async MongoDB driver). It supports product listing, order placement, user-based order retrieval, and includes features like pagination and filtering.

---

## 🚀 Features

- 📦 Product Management (CRUD)
- 🧾 Order Management (Place & List Orders)
- 🔍 Pagination, Filtering (limit, offset)
- 🧑‍💻 User-based Order Listing
- ⚡️ FastAPI with asynchronous I/O
- 🌐 Swagger UI for testing

---

## 📁 Project Structure

project/
│
├── app/
│ ├── routes/
│ │ ├── product_routes.py
│ │ └── order_routes.py
│ ├── models/
│ │ ├── product_model.py
│ │ └── order_model.py
│ ├── schemas/
│ │ ├── product_schema.py
│ │ └── order_schema.py
│ └── database.py
│
├── .env
├── main.py
├── requirements.txt
├── README.md
└── .gitignore


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-ecommerce-backend.git
cd fastapi-ecommerce-backend


2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate        # On Linux/Mac
venv\Scripts\activate           # On Windows


pip install -r requirements.txt


🗄️ Environment Configuration

MONGODB_URI=mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/<database-name>?retryWrites=true&w=majority

DATABASE_NAME=ecommerce


🛠️ Run the FastAPI App
uvicorn main:app --reload
