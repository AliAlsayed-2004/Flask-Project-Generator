import os

def create_flask_project(base_dir):
    structure = {
        "app": {
            "__init__.py": "from flask import Flask\n\ndef create_app():\n    app = Flask(__name__)\n    app.config.from_object('config.Config')\n\n    # Register blueprints here\n\n    return app\n",
            "database": {},
            "extentions": {
                "forms.py": "# Add your form classes here\n",
            },
            "models": {
                "__init__.py": "# Add your model imports here\n",
            },
            "routes": {
                "__init__.py": "# Add your route imports here\n",
            },
            "static": {
                "assets": {},
                "bootstrap" : {},
                "css": {"style.css": "/* Your own style */ /n"},
                "js": {"script.js": "// Your Own Script /n"},
            },
            "seeds":{},
            "templates": {
                "layout.html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <title>Flask App</title>\n</head>\n<body>\n    {% block content %}{% endblock %}\n</body>\n</html>",
            },
        },
        "config.py": "import os\n\nBASE_DIR = os.path.abspath(os.path.dirname(__file__))\nDB_DIR = os.path.join(BASE_DIR, 'app', 'database')\nos.makedirs(DB_DIR, exist_ok=True)\n\nDB_PATH = os.path.join(DB_DIR, 'default.db')\n\nclass Config:\n    SQLALCHEMY_DATABASE_URI = f\"sqlite:///{DB_PATH}\"\n    SQLALCHEMY_TRACK_MODIFICATIONS = False\n    SECRET_KEY = 'your-secret-key'",
        "requirements.txt": "Flask\nFlask-SQLAlchemy\npython-dotenv",
        "run.py": "from app import create_app\n\napp = create_app()\n\nif __name__ == '__main__':\n    app.run(debug=True)",
        ".gitignore": "__pycache__/\n*.py[cod]\nvenv/\n.env\napp/database/*.db\n.vscode/\n.idea/\n*.sublime-*\n*.swp\n.DS_Store",
    }

    def create_structure(base, structure):
        for name, content in structure.items():
            path = os.path.join(base, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_structure(path, content)
            else:
                with open(path, "w") as f:
                    f.write(content)

    create_structure(base_dir, structure)

if __name__ == "__main__":
    project_dir = input("[?] Enter the path for the new Flask project: ")
    create_flask_project(project_dir)
    print(f"[*] Flask project structure created at {project_dir}")
    input("[?] Press Enter to exit...")