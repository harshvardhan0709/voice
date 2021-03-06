# Supplementary material - Code examples

These files accompany the article "Introducing Parselmouth: A Python Interface to Praat" and present the full, executable examples of code presented in the article. Every Python script file with code is also accompanied by a version of that file with extra comments, explaining what is happening for each line of code. All Python scripts (except for the PsychoPy one) were tested with Python 3, but are supposed to be working with Python 2 as well.

For detailed and up-to-date instructions to install Parselmouth, and for the latest examples and tutorials, please refer to the online documentation at https://parselmouth.readthedocs.io/ or https://github.com/YannickJadoul/Parselmouth


## Data Visualisation

The data visualisation example from section 2.1 consists of the following files:

- `visualisation.py` contains both parts of the presented code
- `1_b.wav`, `2_b.wav`, `3_b.wav`, `4_b.wav`, `5_b.wav`, `1_y.wav`, `2_y.wav`, `3_y.wav`, `4_y.wav`, and `5_y.wav` in the `audio` subfolder are the files accessed by the script
- `audio/digit_list.csv` contains a structured table of these different audio files and is read in the second part of the example

To run this example, the `seaborn`, `matplotlib`, and `pandas` libraries need to be installed. This example was tested with parselmouth 0.3.0, numpy 1.14.5, seaborn 0.8.1, matplotlib 2.2.2, and pandas 0.23.1.


## File Manipulation

The second example, demonstrating data file manipulation and file system access, consists of these files:

- `batch_process.py` contains the presented code
- `results.csv` is the comma-separated values file read by the script
- `1_b.wav`, `2_b.wav`, `3_b.wav`, `4_b.wav`, `5_b.wav`, `1_y.wav`, `2_y.wav`, `3_y.wav`, `4_y.wav`, and `5_y.wav` in the `audio` subfolder are the files referenced in the CSV file and accessed by the script

To run this example, the `pandas` library needs to be installed. This example was tested with parselmouth 0.3.0, and pandas 0.23.1.


## Audio Manipulation

This example calls Praat commands and actions to manipulate the pitch of an existing audio file:

- `pitch_manipulation.py` contains the presented code
- `audio/4_b.wav` is the file that is read by the script, and of which the pitch is increased by one octave; the script will save the new file as `4_b_octave_up.wav`)

This example was tested with parselmouth 0.3.0, and numpy 1.14.5.


## Integration with Statistical Libraries & Existing Praat Scripts

In the fourth example, an existing Praat script script is run and a statistical analysis is done on the output of the script:

- `syllable_nuclei_stats.py` contains the presented code
- `syllable_nuclei.praat` is the file with the Praat script, slightly modified from the version at https://sites.google.com/site/speechrate/; the modifications are indicated in the comments in this file
- The script reads `corpus/corpus.cvs` and then loads the corresponding files in the `corpus` subdirectory.

To run this example, the `statsmodels` library needs to be installed. This example was tested with parselmouth 0.3.0, numpy 1.14.5, pandas 0.23.1, statsmodels 0.9.0, and bambi 0.1.1.


## Integration into Experimental Design

The last example demonstrates how Parselmouth can be used to access Praat functionality in a PsychoPy experiment:

- `adaptive_listening.psyexp` contains the full PsychoPy experiment that can be read and edited in the PsychoPy builder
- `adaptive_listening.py` contains the relevant parts of custom code, added in a PsychoPy 'Code component'
- `adaptive_listening_lastrun.py` contains the code that is automatically generated by the PsychoPy builder when running the experiment
- `audio/bat.wav` and `audio/bet.wav` are the two audio files read, manipulated, and used in the experiment
- `standalone_psychopy_installation.txt` contains the steps on how to install Parselmouth in the standalone version of the PsychoPy Builder on macOS/OS X and Windows (which is a slightly different procedure from installing Parselmouth in a normal Python distribution); a potentially updated version of these instructions can be found in the documentation online at https://parselmouth.readthedocs.io/

The experiment was created and tested in PsychoPy version 1.85.3, with parselmouth 0.3.0, and numpy 1.14.5.


