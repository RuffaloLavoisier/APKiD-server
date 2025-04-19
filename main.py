from flask import Flask, request
import os
import subprocess
import time

app = Flask(__name__)

# Set the path to the APKID command
# E.g. "apkid" or the full path to the APKID executable
APKID_CMD = "YOUR_APKID_COMMAND"  # Replace with the actual command to run APKID

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def save_with_progress(file, save_path, chunk_size=1024 * 1024):
    total_size = file.content_length 
    bytes_written = 0
    with open(save_path, 'wb') as f:
        while True:
            chunk = file.stream.read(chunk_size)
            if not chunk:
                break
            f.write(chunk)
            bytes_written += len(chunk)

            if total_size:
                progress = (bytes_written / total_size) * 100
                draw_progress_bar(progress, bytes_written, total_size)

            time.sleep(0.1)
        print()

def draw_progress_bar(percent, bytes_written, total_size, bar_length=10):
    filled_length = int(round(bar_length * percent / 100))
    bar = '[' + '█' * filled_length + '-' * (bar_length - filled_length) + ']'
    print(f"{bar} {percent:.2f}% ({bytes_written}/{total_size})", end='\r')

@app.route('/upload', methods=['POST'])
def upload():
    print("[+] Request Upload File..")

    if 'file' not in request.files:
        print("[+] File not found")
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        print("[+] File name is empty")
        return 'No selected file', 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    save_with_progress(file, file_path)
    print(f"[+] Saved: {file.filename} ({os.path.getsize(file_path)} bytes)")

    print("[+] APKID Start")
    result = subprocess.run([APKID_CMD, file_path], capture_output=True, text=True)
    print(result.stdout)
    
    return result.stdout, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
