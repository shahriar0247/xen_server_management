import psutil

def get_total_cpu_usage():
    return psutil.cpu_percent()

def get_total_ram_usage():
     return psutil.virtual_memory().percent
        
