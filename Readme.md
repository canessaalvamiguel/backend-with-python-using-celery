## Background Process Management with Celery and Django
This module focuses on mastering background process management using Celery, 
a powerful distributed task queue. Through a series of hands-on exercises, 
you'll delve into various Celery methods such as apply_async, group, chain,
and chord, enabling you to efficiently handle asynchronous tasks in your applications.

# Key Features:
- Celery Methods Exploration: Gain a deep understanding of Celery's diverse 
methods including apply_async, group, chain, and chord, and learn how to leverage
them effectively in your projects.
- Integration with Redis: Learn how to seamlessly integrate Celery with Redis, 
a robust and versatile in-memory data structure store, enabling efficient task
queue management.
- Monitoring with Flower: Dive into the monitoring capabilities of Flower, 
a real-time web-based monitoring tool for Celery, allowing you to track the
progress and status of your Celery tasks effortlessly.

## Running app
Use the next command:
```
pip install -r requirements.txt
python manage.py runserver
```

Running celery server:
```
celery -A live worker
```

Running flower server for monitoring:
```
celery -A live flower
```
*For Windows check: Fixing problem in Windows
## Install dependencies manually

```
pip install django
pip install celery
pip install redis
pip install flower
```

## Fixing problem in Windows
There is a small incompatibility on Windows and celery4.0+, to solve this problem:

1 - install gevent:
```
pip install gevent
```

2 - Run celery:
```
celery -A live worker -l info -P gevent
```
https://stackoverflow.com/questions/51243515/django-celery-task-does-not-execute-with-delay