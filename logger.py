from datetime import datetime
def log(message,logfile ="app.log"):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open (logfile,"a") as f:
        f.write(f"[{time}] {message}\n")