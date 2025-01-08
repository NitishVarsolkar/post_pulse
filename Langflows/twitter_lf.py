from langflow import Flow
from langflow.nodes import FunctionNode

def load_data(file_path):
    import pandas as pd
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        return f"Error loading data: {e}"

def analyze_engagement(data):
    data['engagement_rate'] = (data['retweets'] + data['likes']) / data['followers'] * 100
    return data

def generate_insights(data):
    avg_engagement = data['engagement_rate'].mean()
    high_engagement_tweets = data[data['engagement_rate'] > 5]
    return {
        'average_engagement_rate': avg_engagement,
        'high_engagement_tweets': high_engagement_tweets[['tweet_id', 'engagement_rate']],
    }

flow = Flow()

load_data_node = FunctionNode(
    function=load_data,
    inputs=["file_path"],
    outputs=["data"],
    name="Load Twitter Data"
)

analyze_data_node = FunctionNode(
    function=analyze_engagement,
    inputs=["data"],
    outputs=["analyzed_data"],
    name="Analyze Engagement"
)

generate_insights_node = FunctionNode(
    function=generate_insights,
    inputs=["analyzed_data"],
    outputs=["insights"],
    name="Generate Insights"
)

flow.connect(load_data_node, analyze_data_node)
flow.connect(analyze_data_node, generate_insights_node)

result = flow.run({"file_path": "path_to_twitter_scraped_data.csv"})
insights = result["insights"]
print(insights['average_engagement_rate'])
print(insights['high_engagement_tweets'])
