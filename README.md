# License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Aditya-1998k/Custom-Log-Handler/blob/main/LICENSE) file for details.

# LogTrace Router
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
LogTrace-Router/
├── src/                  
│   ├── app.py            
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
LOG_HANDLER=memory
FILE_NAME='app/logs/app.log'
```
