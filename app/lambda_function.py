# -*- coding: utf-8 -*-

from controllers import youtube


def lambda_handler(event, context):
    if 'id' not in event:
        return {
            'statusCode': 500,
            'body': 'id required',
        }

    video_id = event['id']
    video = youtube.get_video(video_id)

    return {
        'statusCode': 200,
        'body': video,
    }
