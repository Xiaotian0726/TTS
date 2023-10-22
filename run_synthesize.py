import subprocess
import os

def remove_punc(s: str):
    return s.replace(',', '').replace('.', '')

OUTPUT_FOLDER = 'TTS-generated'

transcripts = [
    # # Wakeup word
    # 'Hi, Mia.',

    # Speech with privacy risk
    'My dad went to the national bank to withdraw money just now.',
    'I need some loans from the bank.',
    'My bank card password is your birthday.',
    "Today is your birthday.",
    "I'm scheduled for a tumor surgery next week.",
    "I'm going to the barber's to have a haircut.",

    # Commands
    'Please open the door.',
    'Turn on the bluetooth.',
    'Turn off the computer.',
    'Add an appointment to the calendar.',
]

if __name__ == '__main__':
    for t in transcripts:
        target_dir = os.path.join(OUTPUT_FOLDER, remove_punc(t).upper())
        os.makedirs(target_dir, exist_ok=True)

        arg_list = [
            'python',
            'TTS/bin/synthesize.py',
            '--model_name', 'tts_models/en/ljspeech/tacotron2-DDC',
            '--vocoder_name', 'vocoder_models/en/ljspeech/hifigan_v2',
            '--text', t,
            '--out_path', os.path.join(target_dir, '[' + t[0:7] + ']' + '.wav'),
        ]

        subprocess.run(arg_list)
