from hate.logger import logging
import sys
from hate.exception import CustomException
from hate.configuration.gcloud_syncer import GCloudSync

obj = GCloudSync()
obj.sync_folder_from_gcloud("hate_speech_data2024", "dataset.zip", "dataset.zip")