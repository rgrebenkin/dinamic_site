bind = "127.0.0.1:8080"
# или через сокет
# bind = "unix:/home/proft/projects/blog/run/blog.socket"
workers = 5
user = "www"
group = "www"
logfile = "/home/roma/gunicorn.log"
loglevel = "info"
proc_name = "blog"
