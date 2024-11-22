#!/usr/bin/python3

from pathlib import Path
from sys import exit
from subprocess import run
from json import loads
from time import sleep

class Start:
    def __init__(
            self, 
            compositor: str, 
            platform: str, 
            instance: str, 
            user: str,
            ip: str
            ) -> None:
        
        self.compositor = compositor
        self.platform = platform
        self.instance = instance
        self.user = user
        self.ip = ip
        self.count_down = 5
    
    def checkCompositor(self) -> bool:
        compositor = Path(self.compositor)
        if not compositor.is_socket():
            exit(f'cannot find {self.compositor}')
        else:
            return True
    
    def checkInstance(self) -> bool:
        state = run(
            [
                self.platform, 
                'query', 
                '--request', 
                'GET', 
                f'/1.0/instances/{self.instance}/state'
                ], 
            capture_output=True, 
            encoding='utf-8'
            )
        self.status = loads(state.stdout)
        if self.count_down > 0:
            if self.status['status'] in ['Started','Starting', 'Success']:
                sleep(3)
                self.checkInstance()
                self.count_down -= 1
            elif self.status['status'] == 'Stopped':
                run([
                    self.platform, 
                    'query', 
                    '--request', 
                    'PUT', 
                    f'/1.0/instances/{self.instance}/state', 
                    '--data', 
                    '{"action":"start"}'
                    ])
                sleep(5)
                self.checkInstance()
                self.count_down -= 1
            elif self.status['status'] == 'Running':
                return True
        else:
            exit(f'cannot start {self.instance}')
    
    def startGUI(self):
        if self.checkCompositor() and self.checkInstance():
            run(['ssh', f'{self.user}@{self.ip}'])
    
    def __call__(self) -> None:
        self.startGUI()

if __name__ == '__main__':
    Start('/run/user/1000/wayland-1', 'incus', 'htpc', 'username', 'ip')()
    #Start('/tmp/.X11-unix/X0', 'lxc', 'htpc', 'username', 'ip')()
