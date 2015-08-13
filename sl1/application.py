import multiprocessing

bind = "10.0.0.34:8001"
workers = multiprocessing.cpu_count() *2 +1

