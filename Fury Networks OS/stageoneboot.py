import os #type: ignore
import time
print("|      |")
print("|      |")
print("--------")
print("|      |")
print("|      |")
print("  ")
print("  ")
print("|-------")
print("|       ")
print("|-------")
print("|       ")
print("|-------")
print("  ")
print("  ")
print("|")
print("|")
print("|")
print("|")
print("--------")
print("  ")
print("  ")
print("|")
print("|")
print("|")
print("|")
print("--------")
print("  ")
print("  ")
print("--------")
print("|      |")
print("|      |")
print("|      |")
print("--------")
time.sleep(1)
print("FURY NETWORKS OS")
import os
import sys
import subprocess

class CroshClone:
    def init(self):
        self.commands = {
            "help": self.help,
            "exit": self.exit,
            "version": self.version,
            "ping": self.ping,
            "ssh": self.ssh,
            "top": self.top,
        }

    def run(self):
        print("Welcome to Fury Networks OS run board..")
        while True:
            command = input("crosh> ").strip().lower()
            if command in self.commands:
                self.commands[command]()
            else:
                print(f"Unknown command: {command}")

    def help(self):
        print("Available commands:")
        for cmd in self.commands:
            print(f"- {cmd}")

    def exit(self):
        print("Exiting crosh clone.")
        sys.exit(0)

    def version(self):
        print("crosh clone version 0.1")

    def ping(self):
        host = input("Enter hostname or IP to ping: ")
        os.system(f"ping -c 4 {host}")

    def ssh(self):
        host = input("Enter hostname or IP to connect: ")
        os.system(f"ssh {host}")

    def top(self):
        subprocess.run(["top", "-n", "1"])

if NameError == "main": # type: ignore
    crosh = CroshClone()
    crosh.run()