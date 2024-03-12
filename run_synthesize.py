import subprocess
import os

def remove_punc(s: str):
    return s.replace(',', '').replace('.', '')

# OUTPUT_FOLDER = 'TTS-for-finetune'
# WW_NUM = 2000
# NWW_NUM = 200

# OUTPUT_FOLDER = 'TTS-for-adv'
# WW_NUM = 2000
# NWW_NUM = 200

# OUTPUT_FOLDER = 'TTS-for-local-delta-test'
# WW_NUM = 500
# NWW_NUM = 50

OUTPUT_FOLDER = 'TTS-for-physical-test'
WW_NUM = 100
NWW_NUM = 10

transcripts = [
    # Wake word
    {'t' : 'Hi, Mia.', 
     'num': WW_NUM, 'duration_upper_bound' : 2.0},

    # Speech with privacy risk
    {'t' : 'My dad went to the national bank to withdraw money just now.', 
     'num': NWW_NUM, 'duration_upper_bound' : 5.0},
    {'t' : 'My bank card password is your birthday.', 
     'num': NWW_NUM, 'duration_upper_bound' : 4.0},
    {'t' : "I'm scheduled for a tumor surgery next week.", 
     'num': NWW_NUM, 'duration_upper_bound' : 4.0},
    {'t' : "It is said that Alex will be changing jobs to the neighboring company next month.", 
     'num': NWW_NUM, 'duration_upper_bound' : 7.0},
    {'t' : "His home is located on Center Street, close to the largest bank in the city.", 
     'num': NWW_NUM, 'duration_upper_bound' : 7.0},

    # Daily commands
    {'t' : 'Please open the door.', 
     'num': NWW_NUM, 'duration_upper_bound' : 2.7},
    {'t' : 'Turn on the bluetooth.', 
     'num': NWW_NUM, 'duration_upper_bound' : 2.5},
    {'t' : 'Turn off the computer.', 
     'num': NWW_NUM, 'duration_upper_bound' : 2.5},
    {'t' : 'Add an appointment to the calendar.', 
     'num': NWW_NUM, 'duration_upper_bound' : 3.5},
    {'t' : 'Please play a song.', 
     'num': NWW_NUM, 'duration_upper_bound' : 2.8},
]

if __name__ == '__main__':
    for transcript in transcripts:
        t = transcript['t']
        num = transcript['num']
        duration_upper_bound = transcript['duration_upper_bound']
        
        target_dir = os.path.join(OUTPUT_FOLDER, remove_punc(t).upper())
        os.makedirs(target_dir, exist_ok=True)

        arg_list = [
            'python',
            'TTS/bin/synthesize.py',
            '--model_name', 'tts_models/en/ljspeech/tacotron2-DDC',
            '--vocoder_name', 'vocoder_models/en/ljspeech/hifigan_v2',
            '--text', t,
            '--out_path', os.path.join(target_dir, '[' + t[0:7] + ']' + '.wav'),
            '--num', str(num),
            '--duration_upper_bound', str(duration_upper_bound),
        ]

        subprocess.run(arg_list)
