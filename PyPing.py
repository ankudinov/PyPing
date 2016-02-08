from threading import Thread
from queue import Queue
import subprocess

__author__ = 'Petr Ankudinov'


class Ping(Thread):

    def __init__(self, queue_ip, queue_reachable, queue_unreachable):
        Thread.__init__(self)
        self.queue_ip = queue_ip
        self.queue_reachable = queue_reachable
        self.queue_unreachable = queue_unreachable

    def run(self):

        ip = self.queue_ip.get()
        cmd = 'ping -c 4 -i 0.25 -W 300 -t 1 %s' % ip

        try:
            subprocess.check_output(cmd.split())
        except Exception as _:
            self.queue_unreachable.put(ip)
        else:
            self.queue_reachable.put(ip)

        self.queue_ip.task_done()


def check_if_pingable(ip_list):
    """
    Check what IP addresses from the list are reachable
    :param ip_list: list of IP addresses to ping
    :return: list of reachable and unreachable hosts
    """

    queue_ip = Queue()
    queue_reachable = Queue()
    queue_unreachable = Queue()

    reachable = []
    unreachable = []

    for ip in ip_list:
        queue_ip.put(ip)

    while not queue_ip.empty():
        for x in range(50):
            worker = Ping(queue_ip, queue_reachable, queue_unreachable)
            worker.daemon = True
            worker.start()

    queue_ip.join()

    while not queue_reachable.empty():
        reachable.append(queue_reachable.get())

    while not queue_unreachable.empty():
        unreachable.append(queue_unreachable.get())

    return reachable, unreachable
