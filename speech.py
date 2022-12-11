# pip install azure-ai-textanalytics
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
def sample_analyze_sentiment(documents):
    endpoint = "" # Will be provided 
    key = "" # Will be provided
    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    response = text_analytics_client.analyze_sentiment(documents, show_opinion_mining=True)
    results = [doc for doc in response if not doc.is_error]
    for result in results:
        print(result.id, result.sentiment, result.confidence_scores)
sample_analyze_sentiment([
        """I am good""",
        """I am bad""",
        """I am horny""",
        """I am ok""",
    ])
