# APKiD for Android Device

When developing — and especially reverse engineering — Android apps APKiD is incredibly useful for identifying packers, obfuscators, and other software protections.

Over time many protection mechanisms start to look alike and APKiD's rule-based detection makes it possible to identify them in unknown apps without repeating the same manual analysis — as long as similar patterns were seen before.

But here's the problem:
The APK file you find online may not exactly match what's actually running on a device. Versions vary, architectures differ, and sometimes hidden code or packed binaries are only present on the installed app.
Manually extracting and checking each app got old fast.

## 🚀 The Idea
So I built a simple but effective solution:
An app that runs on your device sends installed APK file to a local APKiD server (running on your PC) and shows you the analysis results — automatically.

✅ Pulls real APK directly from the device

🔁 Sends them to your local APKiD server

🧾 Displays the results after analysis

It’s minimal a bit rough but does exactly what I need — and it's fun to use.

## 📡 Note
This project communicates with a local APKiD server not a public one.
Make sure to run APKiD in server mode on your PC and configure your device to upload to that endpoint.

## 📜 Usage

```python
# Set the path to the APKID command
# E.g. "apkid" or the full path to the APKID executable
APKID_CMD = "apkid"  # if you use apkid command

APKID_CMD = "/path/to/APKiD/docker/apkid.sh"  # if you use full path to the APKID executable (docker)
```

Run

```shell
$ python main.py
```

## 💳 Credits

[APKiD](https://github.com/rednaga/APKiD)