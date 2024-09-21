# Custom-Log-Handler
Logging in Python with custom handler:
```
DB Log Handler : Logging into database
Async Log Handler : Logging asynchronously to database
Console log Handler : Logging onto the console
File Log Handler : Logging into the file
Memory Log Handler : Logging into the Memory
```

### Project Structure
```
custom_log_handler_app/
├── src/                  # New source folder
│   ├── app.py            # Main application
│   ├── handlers/         # Handlers for logging
│   │   ├── db_handler.py
│   │   ├── async_handler.py
│   │   ├── console_handler.py
│   │   ├── file_handler.py
│   │   └── memory_handler.py
│   ├── memory_log_buffer.py  # In-memory log buffer
│   ├── config.py         # Configuration file
├── logs/                 # Directory for log files
│   └── app.log           # Log file for File Log Handler
├── database_setup.sql     # SQL for setting up logs table
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile             # Dockerfile for the Python app
├── requirements.txt       # Python dependencies
└── celery_worker.py       # Celery worker for asynchronous logging
```

# sample ENVIRONMENT Variable
```
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=db
DB_PORT=5432
REDIS_HOST=redis
REDIS_PORT=6379
```