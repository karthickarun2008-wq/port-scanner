
---

# 🔎 Network Port Scanner — `README.md`

```markdown
# 🔎 Network Port Scanner

A Python-based network security project that scans common TCP ports on a target host and identifies accessible ports.

## 📌 About

The Network Port Scanner uses Python socket programming to connect to selected TCP ports and determine whether they are accessible.

The project also uses multithreading to perform multiple port checks efficiently.

## 🛠️ Technologies Used

- Python
- Socket Programming
- TCP
- Multithreading

## ⚙️ How It Works

The program:

1. Takes a hostname or IP address as input.
2. Resolves the hostname to an IP address.
3. Scans a predefined list of common TCP ports.
4. Attempts to connect to each port.
5. Displays the ports that are accessible.

### Example

```text
Enter Hostname or IP Address: example.com

Scanning example.com (IP_ADDRESS)...

Port 22 is open
Port 80 is open
Port 443 is open

Scan complete.
