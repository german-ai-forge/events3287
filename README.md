# 🎟️ events3287 – Event Management System (MVP Architecture)

This project is a modular event management platform built using **Python (Flask)** and **MongoDB**, following the **Model-View-Presenter (MVP)** architecture. It supports user sessions, event creation, admin functionality, and a ticket purchasing flow.

---

## 🧱 Project Architecture: MVP

- **Models** → Handle database logic and structure
- **Views** → HTML responses and rendering (via Flask templates or endpoints)
- **Presenters (Controllers/Routes)** → Handle business logic and orchestrate between views and models

---

## 📁 Project Structure

events3287/
├── app/ # Flask app initialization
├── controllers/ # Core presenter logic for business flows
├── models/ # Database models and schemas
├── route/ # Route definitions and Flask endpoint bindings
├── script/ # Utility or automation scripts
├── views.py # View logic for rendering responses
├── home.py # Entry point for home route
├── about.py # Static route example
├── .config.py # Application configuration settings
├── README.md # Project description and usage
└── models.py # Additional models (legacy or shared logic)

yaml
Copy
Edit

---

## ✨ Features

- 👤 User login and session management
- 🎭 Event creation and editing by event owners
- 🛒 Ticket purchase/cart system
- 🛠 Admin tools for managing users/events
- 💾 MongoDB integration
- ⚙️ Modular architecture with clear separation of concerns

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/german-ai-forge/events3287.git
cd events3287

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python home.py
