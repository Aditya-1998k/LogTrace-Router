# License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Aditya-1998k/Custom-Log-Handler/blob/main/LICENSE) file for details.

## LogTrace Router
Logging in Python with custom handler:
```
DB Log Handler : Logging into database
Async Log Handler : Logging asynchronously to database
Console log Handler : Logging onto the console
File Log Handler : Logging into the file
Memory Log Handler : Logging into the Memory
```

### Shortcut Command to start the project
Refer file: Initialize.sh & utils.sh file
```
c up -d (Running container in detach mode)
c up (Running App in Attach Mode)
c restart
c down
c stop
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

### sample ENVIRONMENT Variable
```
LOG_HANDLER=memory
FILE_NAME='app/logs/app.log'
```

### Accessing Web
```
http://127.0.0.1:50001/hello
http://127.0.0.1:50001/log
http://127.0.0.1:5000/clear_log
```

### Custom Memory Handler
<img width="927" alt="Screenshot 2024-09-22 at 10 23 36 PM" src="https://github.com/user-attachments/assets/0f859bb1-ed8a-4aaf-828a-2c41bf08d217">

### Custom Console Handler
<img width="927" alt="Screenshot 2024-09-29 at 6 56 36 AM" src="https://github.com/user-attachments/assets/ac98e886-7430-43a2-bfeb-bf0d7791232c">

### Custom File Handler
Visit [log file](https://github.com/Aditya-1998k/LogTrace-Router/blob/main/src/logs/app.log)
