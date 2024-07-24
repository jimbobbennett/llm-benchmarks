import pandas as pd
import psutil

def get_top_llms():
    df = pd.read_csv('Open LLM-Perf Leaderboard.csv')

    ram_in_mb = psutil.virtual_memory().total/1024/1024

    df = df[df['Throughput (tokens/s)'] >= 20]

    df = df[df['Peak Memory (MB)'] <= ram_in_mb]

    return df

# Load the top LLMs
df = get_top_llms()

# Print the top LLMs
print(df.head())
