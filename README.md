<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>

<h1 align="center">
OpenAI Python Wrapper
</h1>
<h4 align="center">A Python backend service for seamless OpenAI API integration.</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Framework-FastAPI-blue" alt="Framework used">
  <img src="https://img.shields.io/badge/Language-Python-red" alt="Programming Language">
  <img src="https://img.shields.io/badge/Database-PostgreSQL-blue" alt="Database used">
  <img src="https://img.shields.io/badge/LLMs-OpenAI-black" alt="Large Language Models">
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/coslynx/OpenAI-Python-Wrapper?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/coslynx/OpenAI-Python-Wrapper?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/coslynx/OpenAI-Python-Wrapper?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📄 License
- 👏 Authors

## 📍 Overview

This repository contains the backend code for the OpenAI Python Wrapper, a Python service designed to simplify the use of OpenAI's API for developers. This service offers a user-friendly interface for sending requests to OpenAI's API and receiving structured responses, making it easier for developers to integrate AI capabilities into their Python applications.

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The service follows a modular architectural pattern with separate directories for different functionalities, ensuring easier maintenance and scalability.             |
| 📄 | **Documentation**  | This repository includes a README file that provides a detailed overview of the project, its dependencies, and usage instructions.  |
| 🔗 | **Dependencies**   | The codebase relies on various external libraries and packages such as `fastapi`, `uvicorn`, `openai`, `pydantic`, and `sqlalchemy`, which are essential for building and managing the API, interacting with OpenAI, and managing data.  |
| 🧩 | **Modularity**     | The modular structure allows for easier maintenance and reusability of the code, with separate directories and files for different functionalities such as services, routes, models, and utilities.  |
| 🧪 | **Testing**        | Unit tests using `pytest` are implemented to ensure the reliability and robustness of the codebase.      |
| ⚡️  | **Performance**    | The service is optimized for efficiency, leveraging asynchronous operations with FastAPI.  |
| 🔐 | **Security**       |  Security is enhanced by implementing measures such as API key handling through environment variables and input validation using Pydantic.  |
| 🔀 | **Version Control**| Utilizes Git for version control. |
| 🔌 | **Integrations**   | The service seamlessly integrates with the OpenAI API and leverages the `openai` library for efficient interaction. |
| 📶 | **Scalability**    | Designed for scalability, using a framework like FastAPI which supports asynchronous operations and can easily handle increased user load and data volume.   |

## 📂 Structure

```text
openai-python-wrapper/
├── requirements.txt
├── .env
├── main.py
├── models/
│   └── base.py
├── services/
│   └── openai_service.py
├── utils/
│   └── openai_utils.py
├── routes/
│   └── api_routes.py
├── tests/
│   ├── test_routes.py
│   ├── test_models.py
│   ├── test_utils.py
│   └── test_services.py
├── commands.json
├── startup.sh
├── logging.conf
└── .gitignore

```

## 💻 Installation

### 🔧 Prerequisites

- Python 3.9+
- `pip` package manager
- PostgreSQL (optional)

### 🚀 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/coslynx/OpenAI-Python-Wrapper.git
   cd OpenAI-Python-Wrapper
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the project root and fill in the required values:
     ```bash
     OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE
     DATABASE_URL=postgresql://user:password@host:port/database
     ```

4. **(Optional) Set up the PostgreSQL database:**
   - Follow the instructions for setting up PostgreSQL on your system.
   - Update the `DATABASE_URL` in the `.env` file with your PostgreSQL connection details.

## 🏗️ Usage

### 🏃‍♂️ Running the MVP

1. **Start the development server:**
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

## 🌐 Hosting

### 🚀 Deployment Instructions

#### Deploying to Heroku

1. Install the Heroku CLI:
   ```bash
   npm install -g heroku
   ```

2. Login to Heroku:
   ```bash
   heroku login
   ```

3. Create a new Heroku app:
   ```bash
   heroku create OpenAI-Python-Wrapper-production
   ```

4. Set up environment variables:
   ```bash
   heroku config:set OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE
   heroku config:set DATABASE_URL=your_database_url_here
   ```

5. Deploy the code:
   ```bash
   git push heroku main
   ```

6. Run database migrations (if applicable):
   ```bash
   heroku run python manage.py migrate
   ```

### 🔑 Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key.
- `DATABASE_URL`: Connection string for your PostgreSQL database (if applicable).

## 📜 API Documentation

### 🔍 Endpoints

- **POST /api/generate_text**
  - Description: Generates text using OpenAI's API.
  - Body:
    ```json
    {
      "prompt": "Write a short story about a cat.",
      "model": "text-davinci-003",
      "max_tokens": 100
    }
    ```
  - Response:
    ```json
    {
      "text": "Once upon a time, there was a fluffy cat named Mittens..."
    }
    ```

- **POST /api/translate_text**
  - Description: Translates text between languages using OpenAI's API.
  - Body:
    ```json
    {
      "text": "Hello, world!",
      "target_language": "fr"
    }
    ```
  - Response:
    ```json
    {
      "translation": "Bonjour le monde !"
    }
    ```

- **POST /api/complete_code**
  - Description: Completes code snippets using OpenAI's API.
  - Body:
    ```json
    {
      "prompt": "def greet(name):\n  print("
    }
    ```
  - Response:
    ```json
    {
      "code": "def greet(name):\n  print(f\"Hello, {name}!\")"
    }
    ```


## 📜 License & Attribution

### 📄 License

This Minimum Viable Product (MVP) is licensed under the [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) license.

### 🤖 AI-Generated MVP

This MVP was entirely generated using artificial intelligence through [CosLynx.com](https://coslynx.com).

No human was directly involved in the coding process of the repository: OpenAI-Python-Wrapper

### 📞 Contact

For any questions or concerns regarding this AI-generated MVP, please contact CosLynx at:
- Website: [CosLynx.com](https://coslynx.com)
- Twitter: [@CosLynxAI](https://x.com/CosLynxAI)

<p align="center">
  <h1 align="center">🌐 CosLynx.com</h1>
</p>
<p align="center">
  <em>Create Your Custom MVP in Minutes With CosLynxAI!</em>
</p>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Developers-Drix10,_Kais_Radwan-red" alt="">
  <img src="https://img.shields.io/badge/Website-CosLynx.com-blue" alt="">
  <img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="">
  <img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4,_v6-black" alt="">
</div>