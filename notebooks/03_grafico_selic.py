import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("selic_2025.csv", parse_dates=["data_referencia"])

media = df["taxa_percentual"].mean()

plt.figure(figsize=(11, 5))

plt.plot(
    df["data_referencia"],
    df["taxa_percentual"],
    color="#2563EB",
    marker="o",
    linewidth=2.5,
    label="Selic mensal"
)

plt.title("Selic acumulada mensal - 2025")
plt.xlabel("Mês de referência")
plt.ylabel("Taxa mensal (%)")

plt.axhline(
    y=media,
    color="#E86A33",
    linestyle="--",
    linewidth=2,
    label=f"Média mensal: {media:.2f}%"
)
plt.grid(alpha=0.2)
plt.xticks(
    df["data_referencia"],
    df["data_referencia"].dt.strftime("%m/%Y"),
    rotation=45
)
plt.tight_layout()

plt.legend()

for data, taxa in zip(df["data_referencia"], df["taxa_percentual"]):
    plt.annotate(
        f"{taxa:.2f}%",
        (data, taxa),
        xytext=(0, 10),
        textcoords="offset points",
        ha="center",
        fontsize=9
    )
plt.margins(y=0.15)

plt.savefig("graficos/selic_2025.png", dpi=150, bbox_inches="tight")

plt.show()
