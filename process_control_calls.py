import os
import time

def exec_demo():
    # Replaces current child with /bin/echo
    program = "/bin/echo"
    args = ["echo", "Child process is running using execve()!"]
    os.execve(program, args, os.environ)

def demonstrate_process_states():
    print(f"Main process ID: {os.getpid()}")
    pid = os.fork()

    if pid > 0:
        # Parent process
        print(f"Parent ({os.getpid()}): Created child ({pid})")
        time.sleep(5)

        print(f"Parent ({os.getpid()}): Waiting for child...")
        os.wait()  # Cleans up zombie
        print(f"Parent ({os.getpid()}): Child cleaned up (no longer zombie)")

        # Now create an orphan process
        orphan_pid = os.fork()
        if orphan_pid == 0:
            print(f"Orphan Child ({os.getpid()}): Parent will exit soon")
            time.sleep(10)
            print(f"Orphan Child ({os.getpid()}): Adopted by init (PID 1)")
        else:
            print(f"Parent ({os.getpid()}): Created orphan ({orphan_pid}), exiting...")
            time.sleep(2)
            exit(0)

    elif pid == 0:
        # Child process
        print(f"Child ({os.getpid()}): Running execve() demo...")
        time.sleep(2)
        exec_demo()
    else:
        print("Fork failed.")

if __name__ == "__main__":
    demonstrate_process_states()














