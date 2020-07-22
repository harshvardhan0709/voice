import os
import sys
import numpy as np
import parselmouth
from parselmouth.praat import call

for file in os.listdir(sys.argv[1]):
  if file.endswith(".wav"):
    file_list = os.path.join(sys.argv[1], file)
    snd = parselmouth.Sound(file_list)
    pitch = snd.to_pitch(time_step=1/200)
    pitch_values = pitch.selected_array['frequency']
    pv = np.savetxt(sys.stdout, pitch_values, newline=',', fmt="%.8f")
    print(file_list,pv)

# pitch_strength = pitch.selected_array['strength']