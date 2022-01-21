from common.common import send
from server.output.system_resources import get_total_cpu_usage, get_total_ram_usage
import json


def get_all_info():
    all_info= {
        "total_cpu_usage": get_total_cpu_usage(),
        "total_ram_usage": get_total_ram_usage()
    }
    return json.dumps(all_info)


def send_all_data(all_clients):
    all_info = get_all_info()
    for client in all_clients:
        send(client, all_info)
        