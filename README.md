# 🚀 Flask Project Generator

Welcome to the Flask Project Generator! This tool helps you quickly scaffold a brand new Flask web application with a clean, modular structure. It sets up everything you need to start building your next Python web project, including database integration, routing, templating, and more. 🌟

---

## 📦 What Does This Tool Do?

- 📁 **Creates a new Flask project** with best practices
- 🗂️ **Organizes your code** into blueprints, models, routes, and static files
- 🗄️ **Sets up SQLite database integration**
- 📝 **Provides a ready-to-use configuration**
- 🧩 **Prepares your project for easy extension**

---

## 📂 Project Structure

```
├── config.py                # Configuration file for the application
├── requirements.txt         # Python dependencies
├── run.py                   # Entry point to start the application
├── app/                     # Main application folder
│   ├── __init__.py          # Application factory
│   ├── database/            # Database-related files
│   ├── extentions/          # Extensions like forms
│   ├── models/              # Database models
│   ├── routes/              # Application routes
│   ├── static/              # Static files (CSS, JS, etc.)
│   └── templates/           # HTML templates
```

---

## 🛠️ Installation

Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   python create_flask_project.py
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚦 Usage

1. Run the application:
   ```bash
   cd your_project_name
   python run.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## ⚙️ Configuration

The application uses SQLite as its database. You can find the database file in:
```
app/database/default.db
```

To change the configuration, edit the `config.py` file:
```python
class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///path-to-your-database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "your-secret-key"
```

---

## 🌟 Features

- **Flask Framework**: Lightweight and easy-to-use web framework.
- **SQLite Database**: Integrated database for storing data.
- **Modular Design**: Organized structure for scalability.
- **Templating**: HTML templates for dynamic content.
- **Static Files**: CSS and JavaScript support.

---

## 🤝 Contributing

We welcome contributions! Feel free to submit issues or pull requests to improve the project.

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 💬 Contact

For any questions or feedback, reach out to me at:
- **Email**: alialasyed.business@gmail.com
- **GitHub**: [GitHub](https://github.com/AliAlsayed-2004)
- **Linkedin**: [LinkedIn](www.linkedin.com/in/ali-alsayed-cse)

---

Happy coding! 🎉
