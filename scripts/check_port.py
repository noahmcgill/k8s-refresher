import subprocess

def check_port(port: int) -> bool:
    result = subprocess.run(["lsof", f"-i:{port}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return result.returncode == 0

if __name__ == "__main__":
    res = check_port(62422)

    if (res):
        print("Port running")
    else:
        print("Port not running")
