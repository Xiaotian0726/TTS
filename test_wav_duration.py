import os
import wave

from statistics import mean

from TTS.utils.utils import get_time_duration_seconds


# TARGET_DIR = 'TTS-for-finetune'
TARGET_DIR = 'TTS-for-adv'
# TARGET_DIR = 'TTS-test'

if __name__ == '__main__':
    t_list = os.listdir(TARGET_DIR)
    for t in t_list:
        duration2wav = {}
        wav_list = os.listdir(os.path.join(TARGET_DIR, t))
        for wav in wav_list:
            d = get_time_duration_seconds(os.path.join(TARGET_DIR, t, wav))
            d_float = int(d * 10) / 10.0
            if d_float not in duration2wav.keys():
                duration2wav[d_float] = set()
            duration2wav[d_float].add(wav)

        print(t)
        print(list(duration2wav.keys()))

        max_item = max(list(duration2wav.keys()))
        time_set_remove_max = list(duration2wav.keys())
        time_set_remove_max.remove(max_item)
        mean_value = mean(time_set_remove_max)

        print('Duration of', max_item, ':', duration2wav[max_item])

        print('')

        