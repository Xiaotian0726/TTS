import wave


def get_time_duration_seconds(wav_path):
    with wave.open(wav_path) as wav_file:
        return wav_file.getnframes() / wav_file.getframerate()