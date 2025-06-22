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
        desktop_start_cmd: str,
        gid: int = 1000,
        uid: int = 1000
    ) -> None:

        self.compositor = compositor
        self.platform = platform
        self.instance = instance
        self.user = user
        self.desktop_start_cmd = desktop_start_cmd
        self.gid = gid
        self.uid = uid
        self.count_down = 5

    def checkCompositor(self) -> bool:
        compositor = Path(self.compositor)
        if not compositor.is_socket():
            return False
        else:
            return True

    def checkInstance(self) -> bool:
        state = run(
            [
                self.platform,
                "query",
                "--request",
                "GET",
                f"/1.0/instances/{self.instance}/state",
            ],
            capture_output=True,
            encoding="utf-8",
        )
        self.status = loads(state.stdout)
        if self.count_down > 0:
            if self.status["status"] in ["Started", "Starting", "Success"]:
                sleep(3)
                self.checkInstance()
                self.count_down -= 1
            elif self.status["status"] == "Stopped":
                run(
                    [
                        self.platform,
                        "query",
                        "--request",
                        "PUT",
                        f"/1.0/instances/{self.instance}/state",
                        "--data",
                        '{"action":"start"}',
                    ]
                )
                sleep(5)
                self.checkInstance()
                self.count_down -= 1
            elif self.status["status"] == "Running":
                return True
        return False

    def startGUI(self) -> None:
        if not self.checkInstance():
            exit(f"cannot start {self.instance}")
        if self.checkCompositor():
            run(
                [
                    self.platform,
                    "query",
                    "--request",
                    "POST",
                    f"/1.0/instances/{self.instance}/exec",
                    "--data",
                    f'{{"command":["bash","-c","{self.desktop_start_cmd}"],"environment":{{"SHELL":"/bin/bash","CWD":"/home/{self.user}","HOME":"/home/{self.user}","USER":"{self.user}","PATH":"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"}},"group":{self.gid},"user":{self.uid}}}',
                ]
            )
        else:
            exit(f"cannot find {self.compositor}")

    def __call__(self) -> None:
        self.startGUI()


if __name__ == "__main__":
    # default gid and uid is 1000, add them if needed
    Start("/run/user/1000/wayland-1", "incus", "htpc", "lxc", "labwc")()
    # Start('/tmp/.X11-unix/X0', 'lxc', 'htpc', 'username', 'mate-session')()
