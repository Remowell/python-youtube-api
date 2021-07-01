# -*- coding: utf-8 -*-
__author__ = "Chirag Rathod (Srce Cde)"
__license__ = "GPL 3.0"
__email__ = "chiragr83@gmail.com"
__maintainer__ = "Chirag Rathod (Srce Cde)"

import os
import argparse
from youtube.videos_channelid import channelVideo

apiKey = "AIzaSyD1OpkSMxv3y2v93rY5WJ5GpW4hIZ1QiZo"

os.makedirs("output", exist_ok=True)
parser = argparse.ArgumentParser()


def getAllChannelVideo(channelurl, maxResults):
    parser.add_argument("--sc", help="calls the search by channel by keyword function", action='store_true')
    parser.add_argument("--channelid", help="channel id", required=True)
    parser.add_argument("--max", help="number of results to return", default=10)
    parser.add_argument("--key", help="Required API key", required=True)

    cv = channelVideo(channelurl, maxResults, apiKey)
    cv.get_channel_videos()