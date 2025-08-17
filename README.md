## Simple Port Scanner
A foundational port scanner tool written in Python. This project is designed to help users identify open ports and active network services on a target IP address by scanning a defined range. It serves as a practical demonstration of basic network communication concepts, including TCP connections and socket programming.

## Disclaimer
This tool is for educational and ethical use only. Always obtain explicit permission before scanning any network.

## Requirements

* **Python 3:** Ensure you have Python 3.x installed. You can download it from the official [Python website](https://www.python.org/downloads/).

* ## Usage

To run the port scanner, simply execute the script from your terminal:

```
python3 port_scanner.py
```

The script will then prompt you to enter the target IP address or hostname and the port range you wish to scan.

Example:

Enter the IP address or hostname: scanme.nmap.org
Enter the starting port: 80
Enter the ending port: 100

## Future Enhancements

* **Multithreading:** Implement multithreading to speed up the scanning process.
* **Port Banner Grabbing:** Extract service banners (e.g., "Apache 2.4.29") from open ports.
* **Service Version Detection:** Identify the specific version of the service running on an open port.
* **Output to a file:** Add the option to save the results to a text file for later analysis.

* Contributions

Your contributions are very welcome! As this is my first public project on GitHub, I am still learning the best practices. If you find any bugs or have ideas for new features, please don't hesitate to open an issue or submit a pull request. Constructive feedback is a great way to help me improve my skills.
