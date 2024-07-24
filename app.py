import matplotlib.pyplot as plt
import pandas as pd
import psutil

def get_fastest_llms():
    df = pd.read_csv('Open LLM-Perf Leaderboard.csv')

    ram_in_mb = psutil.virtual_memory().total/1024/1024

    df = df[df['Throughput (tokens/s)'] >= 20]

    df = df[df['Peak Memory (MB)'] <= ram_in_mb]

    return df

def plot_chart(df_to_plot, filename: str) -> str:
    df_to_plot.plot(x="Model", y="Score (%)", kind="bar")

    plt.title("LLM scores")
    plt.xlabel("Model")
    plt.ylabel("Score (%)")

    plt.savefig(filename)

# Load the fastest LLMs
df = get_fastest_llms()

# Filter the top 10 by score
df = df.nlargest(10, 'Score (%)')

# Sort the dataframe by score descending
sorted_df = df.sort_values(by=['Score (%)'], ascending=False)

# Plot the chart
plot_chart(df, 'llm_scores.png')

