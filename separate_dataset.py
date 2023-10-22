import os
import shutil

DATASET_FOLDER = 'TTS-generated'
TARGET_FOLDER = 'TTS-generated-separated'

if __name__ == '__main__':
    os.makedirs(TARGET_FOLDER, exist_ok=True)
    transcripts = os.listdir(DATASET_FOLDER)
    t2wavs = {}
    for t in transcripts:
        t2wavs[t] = os.listdir(os.path.join(DATASET_FOLDER, t))
        t2wavs[t].sort()


    for i in range(20):
        sep_path = os.path.join(TARGET_FOLDER, '%04d-%04d' % (i*10, i*10+9))
        os.makedirs(sep_path, exist_ok=True)
        for t in t2wavs.keys():
            for j in range(10):
                shutil.copy(
                    src=os.path.join(DATASET_FOLDER, t, t2wavs[t][i*10+j]),
                    dst=os.path.join(sep_path, t2wavs[t][i*10+j])
                )
