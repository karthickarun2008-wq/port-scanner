import socket
from concurrent.futures import ThreadPoolExecutor


def scan_port(host, port):
  """Attempts to connect to a specific port on the target host."""
  try:
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)  # Wait up to 1 second per port

    # Attempts to connect (returns 0 on success)
    result = sock.connect_ex((host, port))
    sock.close()

    if result == 0:
      return port
  except Exception:
    pass
  return None


def main():
  print("=== Simple Multithreaded Port Scanner ===")
  target_input = input("Enter target IP or hostname (e.g., scanme.nmap.org): ")

  # Resolve hostname to IP address
  try:
    target_ip = socket.gethostbyname(target_input)
    print(f"Scanning target: {target_input} ({target_ip})\n")
  except socket.gaierror:
    print("Error: Hostname could not be resolved.")
    return

  # Common well-known ports to scan
  ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]
  open_ports = []

  # Use ThreadPoolExecutor to scan ports concurrently
  with ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(
        lambda p: scan_port(target_ip, p), ports_to_scan
    )

    for port in results:
      if port:
        open_ports.append(port)

  # Display scan results
  print("=== Scan Results ===")
  if open_ports:
    for port in open_ports:
      # Retrieve standard service name if known
      try:
        service = socket.getservbyport(port, "tcp")
      except Exception:
        service = "Unknown"
      print(f"Port {port:<5} | OPEN | Service: {service}")
  else:
    print("No open ports found among the target list.")


if __name__ == "__main__":
  main()