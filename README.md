# PyPing
Basic ping tool with multithreading

Add your own IPs to the PyPing_start.py and excute it.
You'll get a list of reachable and unreachable IPs:
```text
Reachable:
127.0.0.1
8.8.8.8
192.30.252.128
72.163.4.161

Unreachable:
3.3.3.3
2.2.2.2
```

You can inject PyPing into any other code.
It's very fast due to multithreading.

NOTE: supported on Linux and MacOS only, as it's relying on linux ping command.
For windows supoort try to change ```cmd``` in ```run(self)```, but it's not tested.
