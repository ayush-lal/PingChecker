# -*- coding: utf-8 -*-
import rumps  # Library used to create Taskbar apps
import os
import threading


class pingChecker(object):
    def __init__(self):
        self.config = {
            "app_name": "PingChecker",
        }
        self.app = rumps.App(self.config["app_name"])
        self.check_ping()

    def check_ping(self):
        # 1.0 seconds value can be changed to anything
        threading.Timer(1.0, self.check_ping).start()
        hostname = "8.8.8.8"
        response = os.system("ping -c 1 " + hostname)
        if response == 0:  # Begin checking the response value. 0 = Successful | 512 = Failed
            pingStatus = "Network ⬆"
        else:
            pingStatus = "Network ⬇"
        self.app.title = pingStatus

    def run(self):
        self.app.run()


if __name__ == '__main__':
    app = pingChecker()
    app.run()
