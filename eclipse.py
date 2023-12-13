import subprocess
import threading

def nightcrawler_thread(url, depth):
    command = ["python", "nightcrawler.py", url, str(depth)]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    while True:
        line = process.stdout.readline()
        if not line:
            break
        #print(f"{url} {depth}: {line.strip()}")

def main():
    filePath = input("Enter the path to the text file containing URLs: ")
    while True:
        try:
            depth = int(input("Enter the scan depth: "))
            break
        except ValueError:
            print("Please enter a valid integer for the scan depth.")

    while True:
        try:
            threads = int(input("Enter the number of threads: "))
            break
        except ValueError:
            print("Please enter a valid integer for the number of threads.")

    with open(filePath, 'r') as file:
        urls = [line.strip() for line in file.readlines()]

    threads = []
    for url in urls:
        for _ in range(threads):
            thread = threading.Thread(target=nightcrawler_thread, args=(url, depth))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
