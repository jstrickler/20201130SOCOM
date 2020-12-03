from subprocess import run, CalledProcessError, PIPE
import shlex

cmd = "netstat -n"

def main():
    # windows
    # run(cmd)
    # mac/linux #1
    proc = run(shlex.split(cmd), stdout=PIPE)
    # mac/linux #2
    # run(cmd, shell=True)
    print(proc.returncode)
    stdout_lines = proc.stdout.decode().splitlines()
    for line in stdout_lines:
        if 'ESTAB' in line:
            print(line)

if __name__ == '__main__':
    main()
