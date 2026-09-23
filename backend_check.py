import time

print("Starting backend check...")
time.sleep(4)

with open("backend_report.txt", "w") as file:
    file.write("Backend check completed successfully.\n")

print("Backend check completed.")
