# analysis.py
# Email: 24ds3000105@ds.study.iitm.ac.in

import matplotlib.pyplot as plt

# Quarterly customer retention rates
quarters = ["Q1", "Q2", "Q3", "Q4"]
retention = [71.15, 67.22, 71.77, 74.06]
average = sum(retention) / len(retention)
print("Average customer retention:", round(average, 2))  # Should be 71.05

# Create a bar chart
plt.bar(quarters, retention, color="skyblue")
plt.axhline(85, color="red", linestyle="--", label="Industry Target")
plt.title("Quarterly Customer Retention Rate")
plt.ylabel("Retention Rate")
plt.xlabel("Quarter")
plt.legend()
plt.savefig("retention_trend.png", dpi=100)
plt.show()
