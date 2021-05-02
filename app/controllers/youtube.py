# -*- coding: utf-8 -*-

import googleapiclient.discovery
import googleapiclient.errors
import os

api_service_name = "youtube"
api_version = "v3"

print(os.environ.get('API_KEY', ''))

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=os.environ.get('API_KEY', ''))


def get_video(video_id):
    return youtube.videos().list(
        id=video_id,
        part="snippet,contentDetails,statistics",
    ).execute()


def get_livechat_message(chat_id, page_token):
    return youtube.liveChatMessages().list(
        liveChatId=chat_id,
        part="id,snippet,authorDetails",
        pageToken=page_token
    ).execute()
