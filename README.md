## Pyshare

## Project Overview
This project is a file-sharing server written in Python, designed for efficient and reliable file transfer. It provides a minimal web interface, file upload, download and users manegement

## Features
- **File Upload & Download:** Secure and efficient file transfers.
- **Minimal Web Interface:** Simple UI for managing file uploads and downloads.

## Future Enhancements
- **Docker & Kubernetes Support:** Containerized deployment for scalability.
- **User Authentication & Access Control:** Role-based access management.
- **Database Integration:** PostgreSQL for file metadata storage.

## Configuration

### Environment Variables
To configure the app, create a `.env` file:

```
# Configuration Mode => development, testing, staging, or production
CONFIG_MODE = development
SECRET_KEY = 

# POSTGRESQL_DATABASE_URI => 'postgresql+psycopg2://user:password@host:port/database'
DEVELOPMENT_DATABASE_URL = 'postgresql+psycopg2://user:password@host:port/testdb'
TEST_DATABASE_URL        =
STAGING_DATABASE_URL     =
PRODUCTION_DATABASE_URL  =
```

## Getting Started

To run this project locally:

1. **create VE:**

```bash
python -m venv venv
```

2. **activate VE:**
On macOS/Linux:
```bash
source venv/bin/activate
```

3. **install dependencies:**

```bash
pip install -r requirements.txt
```

4. **db init**

```bash
flask db init
flask db migrate
flask db upgrade
```

5. **run the application:**

```bash
flask run
```

Your web app will be available at `http://127.0.0.1:5000`.
