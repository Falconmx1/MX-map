import socket
import threading
from datetime import datetime

class MXScanner:
    def __init__(self, target, ports, threads=100):
        self.target = target
        self.ports = ports
        self.threads = threads
        self.open_ports = []
        self.lock = threading.Lock()

    def scan_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                with self.lock:
                    self.open_ports.append(port)
                    print(f"\033[92m[+] Puerto {port} abierto\033[0m")
            sock.close()
        except:
            pass

    def run(self):
        print(f"\n[+] Escaneando {self.target} desde {datetime.now()}")
        thread_list = []
        for port in self.ports:
            t = threading.Thread(target=self.scan_port, args=(port,))
            thread_list.append(t)
            t.start()
            if len(thread_list) >= self.threads:
                for t in thread_list:
                    t.join()
                thread_list = []
        for t in thread_list:
            t.join()
        return self.open_ports
