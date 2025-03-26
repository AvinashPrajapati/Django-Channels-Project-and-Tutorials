# Django Channels File Transfer with Redis

This project implements a **Django Channels** and **Redis**-based system for transferring smaller files in byte format without database storage. The system is designed for efficient file handling and has future scalability features to support larger files (up to **1GB**) via chunking.

## Features
✅ Real-time file transfer using **Django Channels**  
✅ Efficient byte conversion to avoid DB storage  
✅ Utilizes **Redis** as a fast, in-memory data store  
✅ Designed with scalability in mind for future chunk-based large file transfers  

## Future Scope
🚀 Support for transferring files up to **1GB** using **chunking**  
🚀 Optimized resource management for large-scale file transfer  

## Requirements
- Python 3.10+
- Django 4.x
- Django Channels
- Redis server
- ASGI server (like **Daphne** or **Uvicorn**)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AvinashPrajapati/Django-Channels-Project-and-Tutorials.git
   cd Django-Channels-Project-and-Tutorials
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start Redis server (ensure Redis is installed):(in case of windows use memurai)

5. Migrate the database:
   ```bash
   python manage.py migrate
   ```

6. Run the Django development server with ASGI:
   ```bash
   python manage.py runserver
   ```

## Usage
- Upload files directly via the provided interface or API endpoint.
- Files are converted into byte format and streamed directly to clients through **Channels** without database storage.
- For large files, the system will eventually support **chunking** for efficient handling.
