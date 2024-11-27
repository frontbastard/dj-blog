# DJ Blog

**DJ Blog** is a Django-based web application that provides a fully-featured blogging platform. This project includes functionalities for creating, editing, and viewing blog posts.

## 📋 Overview

DJ Blog demonstrates the capabilities of the Django Framework by incorporating essential components like models, templates, views, and admin configurations. It also integrates advanced features to enhance user experience and application functionality.

### Key Features:
- **Blog Posts Management**: Create, edit, and delete posts.
- **Tagging System**: Implemented using a third-party application.
- **Post Recommendations**: Based on complex QuerySets.
- **Custom Template Tags and Filters**: Extend Django templates with additional functionalities.
- **Sitemap**: Enable search engines to crawl your site efficiently.
- **RSS Feeds**: Allow users to subscribe to your blog content.
- **Full-Text Search**: Built using PostgreSQL's search engine.

---

## 📁 Project Structure

- **`blog/`**: Main blogging application.
- **`blog_service/`**: Additional services or supporting functionality.
- **`manage.py`**: Service file to manage the project.
- **`requirements.txt`**: Python dependencies for the project.

---

## ⚙️ Installation

### Prerequisites
- Python 3.8+
- pip
- virtualenv
- Docker

### Steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/frontbastard/dj-blog
   cd dj-blog-master
   ```

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate # For Windows: env\Scripts\activate
   ```

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

1. **Pull Postgres**
   ```bash
   docker pull postgres:16.2
   ```

1. **Run Postgres**
   ```bash
   docker run --name=blog_db -e POSRGRES_DB=blog -e POSTGRES_USER=blog -e POSTGRES_PASSWORD=xxxxx -p 5432:5432 -d postgres:16.2
   ```

1. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

1. **Run the server:**
   ```bash
   python manage.py runserver
   ```

1. Open in your browser: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🤝 Contributions

We welcome contributions from the community! Feel free to create pull requests or open issues to discuss improvements.
