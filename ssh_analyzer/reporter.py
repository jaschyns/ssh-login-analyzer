import csv
import matplotlib.pyplot as plt

def report_csv(alerts, out_file):
    """Write alerts list to CSV."""
    with open(out_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ip','start','end','count'])
        writer.writerows(alerts)

def plot_alerts(alerts, png_file):
    """Save a bar chart of counts per IP."""
    ips   = [a[0] for a in alerts]
    counts= [a[3] for a in alerts]
    plt.bar(ips, counts)
    plt.xlabel('IP Address')
    plt.ylabel('Failed Attempts')
    plt.title('Detected Brute‐Force Attacks')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(png_file)
