# analysis.py
import matplotlib.pyplot as plt

# Quarterly customer retention data
quarters = ["Q1", "Q2", "Q3", "Q4"]
retention = [71.15, 67.22, 71.77, 74.06]
industry_target = 85
average_retention = sum(retention) / len(retention)

# Print frequency stats
print(f"Quarterly retention: {retention}")
print(f"Average retention: {average_retention:.2f}")

# Plot trend
plt.figure(figsize=(6,4))
plt.plot(quarters, retention, marker='o', label="Company Retention")
plt.axhline(y=industry_target, color='r', linestyle='--', label="Industry Target")
plt.title("Customer Retention Trend - 2024")
plt.ylabel("Retention Rate")
plt.ylim(60, 90)
plt.legend()
plt.grid(True)
plt.savefig("retention_trend.png", dpi=100)
plt.show()
