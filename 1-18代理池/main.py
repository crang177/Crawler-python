
from get_ip import get_ip as get_ip_get_ip
from multiprocessing import Process
from app import run as app_run
from test_ip import run as test_run

def main():
    Process(target=get_ip_get_ip).start()
    Process(target=app_run).start()
    Process(target=test_run).start()

if __name__=="__main__":
    main()