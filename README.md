# LLM benchmarks

A sample Python app for investigating the [LLM benchmarks dataset from Kaggle](https://www.kaggle.com/datasets/warcoder/open-llm-perf-leaderboard-dataset). This can be used for some fun demos of [Pieces for Developers](https://pieces.app).

## Pre-requisites

1. Python
1. [Poetry](https://python-poetry.org/docs/#installation) for managing dependencies.
1. Either [VS Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/).
1. [Pieces for Developers](https://pieces.app), along with the relevant browser extension.

After cloning this repo, run `poetry install` to install the dependencies.

## Run the code

To run the code, use the following command:

```bash
poetry run python app.py
```

## Back story

You are a developer picking up this code for the first time. This is some data science code to look at LLM benchmarks, and your first task is to sort the data and plot it.

## Demo 1 - copilot in your IDE

Imagine you have been given some code to work on, and you need to make changes.

1. From the IDE, ask the copilot to explain the code using the code lens
1. Add comments using the code lens

## Demo 2 - snippets

This code would be better if the data frame was sorted by score, so that we can see the best performing models first. Let's research this in the browser, and when we find the relevant code, add it to Pieces.

1. You can see some code to do this at [stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-by-one-column](https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-by-one-column). Open this in your browser.
1. Scroll to the second or third answer that just has the code to do this, and ask the copilot to explain.
1. Add the snippet to Pieces using the browser extension.
1. See this snippet in the Desktop app, and IDE with all the augmentation.
1. Use the snippet in your IDE to sort the data frame.

## Demo 3 - snippets from images

As an additional demo, there is a screenshot of code to add a bar chart in the [`snippets`](./snippets/) folder.

1. Drag the image into Pieces desktop and show the detected code and annotations

## Demo 4 - live context

There is a PR open for this repo to add plotting of a bar chart. This is a great use case for live context.

1. Open the PR in your browser and show the code changes.
1. From the copilot, start a new conversation with live context.
1. Ask the copilot to explain the PR. This prompt works: 'What problems are there in the github pull request I was just looking at?'
1. Show the output.

## Demo 5 - more advanced live context

For a more detailed PR:

1. Open [github.com/pieces-app/documentation/pull/486](https://github.com/pieces-app/documentation/pull/486)
1. Read the PR
1. Ask the copilot to summarize what Mason asked for - 'what changes did mason request in the PR I was just looking at?'
