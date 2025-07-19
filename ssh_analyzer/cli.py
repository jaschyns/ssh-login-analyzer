import argparse
from datetime import timedelta
from ssh_analyzer.parser  import parse_csv
from ssh_analyzer.analyzer import Analyzer
from ssh_analyzer.reporter import report_csv, plot_alerts

def main():
    p = argparse.ArgumentParser(description="SSH Brute‐Force Analyzer")
    p.add_argument('--log',       required=True, help='CSV log path')
    p.add_argument('--threshold', type=int, default=5, help='failures to alert')
    p.add_argument('--window',    type=int, default=60, help='seconds window')
    p.add_argument('--out',       default='alerts.csv', help='output CSV')
    p.add_argument('--plot',      default='alerts.png', help='output chart')
    args = p.parse_args()

    entries  = parse_csv(args.log)
    analyzer = Analyzer(entries, args.threshold, timedelta(seconds=args.window))
    analyzer.run()

    report_csv(analyzer.alerts, args.out)
    plot_alerts(analyzer.alerts, args.plot)
    print(f"Alerts saved to {args.out} and {args.plot}")

if __name__ == '__main__':
    main()
