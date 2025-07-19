# SSH Login‐Attempt Analyzer

## Problem

\- Detect brute‐force SSH login attempts from an auth‐log CSV.



## Solution

\- **parser.py**: read & parse log into `LogEntry`

\- **analyzer.py**: slide a `timedelta` window to flag IPs

\- **reporter.py**: write CSV + bar‐chart of offenders

\- **cli.py**: user‐friendly CLI with `argparse`


## Installation

1. Clone the repo

    ```bash
    git clone https://github.com/jaschyns/ssh-login-analyzer.git
    cd ssh-login-analyzer
    ```

2. Create and activate a virtual environment

    ```bash
    python -m venv venv

    # Windows
    venv\Scripts\activate

    # macOS / Linux
    source venv/bin/activate
    ```

3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```


## Usage
  
```
python -m ssh_analyzer.cli --log data\auth_sample.csv --threshold 5 --window 60 --out alerts.csv --plot alerts.png
```
      

--log : Path to your SSH log CSV

--threshold : Number of failed attempts to trigger an alert

--window : Time window (in seconds) for counting failures

--out : Output CSV file path

--plot : (Optional) Output bar-chart PNG file path

## Sample Data Format (data/auth_sample.csv)

```
timestamp,user,ip,status
2025-06-29 14:12:11,root,192.168.1.100,Failed
2025-06-29 14:12:14,admin,192.168.1.100,Failed
2025-06-29 14:13:20,jdoe,192.168.1.200,Accepted
```

## License / Author
Justin Schyns · USF Information Science & Security Senior
Feel free to fork or adapt this tool.
