import os
import sys
import ping3
import time
import requests


def ping_ip(url, args):
    print(url, args)
    timeout = os.getenv("TIMEOUT", 15)
    last_res = {}
    res = {}

    for arg in args:
        last_res[arg] = (ping3.ping(arg))

    while True:
        time.sleep(int(timeout))
        for arg in args:
            res[arg] = ping3.ping(arg)

            if (not last_res[arg]) != (not res[arg]):
                data = {"content": None}

                if not res[arg]:
                    is_down = True
                    for i in range(5):
                        time.sleep(int(timeout))
                        res[arg] = ping3.ping(arg)
                        if res[arg]:
                            is_down = False
                    if is_down:
                        data["content"] = f"{arg} is down!"
                else:
                    data["content"] = f"{arg} is back up!"

                if data["content"]:
                    requests.post(url, json=data)

            last_res[arg] = res[arg]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <webhook_url> <ip1> <ip2> ...")
        sys.exit(1)
    else:

        ping_ip(sys.argv[1], sys.argv[2:])