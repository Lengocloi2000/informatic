import threading
import sys
import os, re

received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")

def thread_job(number):
    received_packages = re.compile(r"(\d) received")
    status = ("no response", "alive but losses", "alive")
    ip = "192.168.178." + str(number)
    ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])
    sys.stdout.flush()

def run_threads(count):
    threads = [
        threading.Thread(target=thread_job, args=(i,))
        for i in range(20, count)
    ]
    for thread in threads:
        thread.start()  # каждый поток должен быть запущен
    for thread in threads:
        thread.join()  # дожидаемся исполнения всех потоков


run_threads(30)