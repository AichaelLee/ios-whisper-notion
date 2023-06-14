from notion_client import Client
import datetime
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

DATABASE_ID = os.environ.get('DATABASE_ID')
NOTION_AUTH = os.environ.get('NOTION_AUTH')


def send_to_notion(label, transcript):
    notion = Client(auth=NOTION_AUTH)
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Split the transcript into chunks of 2000 characters each
    transcript_chunks = [transcript[i:i + 2000] for i in range(0, len(transcript), 2000)]

    # Create a list of blocks, each containing a chunk of the transcript
    children_blocks = [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": chunk}}]
            }
        } for chunk in transcript_chunks
    ]

    notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Name": {
                "title": [{"text": {"content": timestamp + '-' + label}}]
            },
        },
        children=children_blocks
    )
