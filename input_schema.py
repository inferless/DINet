INPUT_SCHEMA = {
    "video_url": {
        'datatype': 'STRING',
        'required': True,
        'shape': [-1],
        'example': ["https://infer-global-models.s3.amazonaws.com/DINet/test4.mp4"]
    },
    "audio_url": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://infer-global-models.s3.amazonaws.com/DINet/driving_audio_1.wav"]
    }
}
