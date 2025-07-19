# SSH Login‐Attempt Analyzer



# Problem

\- Detect brute‐force SSH login attempts from an auth‐log CSV.



# Solution

\- **parser.py**: read & parse log into `LogEntry`

\- **analyzer.py**: slide a `timedelta` window to flag IPs

\- **reporter.py**: write CSV + bar‐chart of offenders

\- **cli.py**: user‐friendly CLI with `argparse`



\# Usage

```bash

python -m ssh\_analyzer.cli \

--log data/auth\_sample.csv \

--threshold 5 \

--window 60 \

--out alerts.csv \

--plot alerts.png



