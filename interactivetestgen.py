import subprocess,sys,random,time

TEST=369

sol:subprocess.Popen

def send(txt):
    sol.stdin.write(str(txt)+"\n")
    sol.stdin.flush()
def recv():
    res=sol.stdout.readline()
    if not res: 
        raise RuntimeError("recv er")
    return res
def rd(l,r): 
    return random.randint(l,r)


def proc():
    pass


for test in range(1,TEST+1):
    sol=subprocess.Popen(
        ["nazunasdish.exe"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    proc()
    sol.terminate()
    sol.wait()
    print(test)
