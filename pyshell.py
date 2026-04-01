import os
import sys
import subprocess
import readline

history = []

def execute_command(command):
    try:
        # Background execution
        if command.endswith("&"):
            command = command[:-1]
            subprocess.Popen(command, shell=True)
        else:
            subprocess.run(command, shell=True)
    except Exception as e:
        print("Error:", e)

def execute_piped_commands(command):
    commands = command.split("|")
    processes = []
    prev_process = None

    for cmd in commands:
        cmd = cmd.strip().split()

        if prev_process is None:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        else:
            process = subprocess.Popen(cmd, stdin=prev_process.stdout, stdout=subprocess.PIPE)

        prev_process = process
        processes.append(process)

    output = processes[-1].communicate()[0]
    print(output.decode())

def shell():
    while True:
        try:
            cwd = os.getcwd()
            command = input(f"PyShell:{cwd}$ ")

            if not command.strip():
                continue

            history.append(command)
            readline.add_history(command)

            # Exit
            if command == "exit":
                print("Exiting PyShell...")
                break

            # Change Directory
            elif command.startswith("cd "):
                path = command[3:]
                try:
                    os.chdir(path)
                except FileNotFoundError:
                    print("Directory not found")

            # History
            elif command == "history":
                for i, cmd in enumerate(history):
                    print(i + 1, cmd)

            # Piping
            elif "|" in command:
                execute_piped_commands(command)

            # Normal Command
            else:
                execute_command(command)

        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")

if __name__ == "__main__":
    shell()