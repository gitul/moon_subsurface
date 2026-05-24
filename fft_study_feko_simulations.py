
import numpy as np
import subprocess
import time
import os
import sys
import time


# BEFORE RUNNING, add to .bashrc:
# export FEKOSIM=$HOME'/Desktop/FEKO_simulations/'
#
#
#
# HOW TO RUN:
# python FEKO_simulations_fft_study.py 0 125




# Input parameters
# ----------------
start_sim = int(sys.argv[1])  # first simulation to compute, counting from zero
end_sim   = int(sys.argv[2])  # last simulation to compute, counting from zero









# Folders
# ------------------
project_folder            = '/media/raul/SSD_RED_8TB/FEKO_simulations/subsurface/fft_study/'

# Change to project folder
# ---------------------------
os.chdir(project_folder)





results_subfolder         = 'results'
#project_file_no_extension = 'mars2024_4layers_5MHz'
#results_file_no_extension = 'results'





# Create results subfolder and index file
# ---------------------------------------
folder_exist = os.path.exists(results_subfolder)
if not folder_exist:
        os.mkdir(results_subfolder)












project_file_no_extension = [
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',

        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',

        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',

        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',

        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',

        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',
        'single_layer',


        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',

        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',

        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',

        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',

        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',

        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',



        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',

        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',

        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',

        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',

        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',

        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        'two_layer',
        
        
        'free_space',
        'free_space',
        'free_space',
        'free_space',
        'free_space',
        'free_space'
        
        
]




string_parameters = [
        
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=500000',

        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=500000',

        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=500000',
        
        
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=500000',

        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=500000',

        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=500000',        
        





         
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=500000',
        
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=500000',
        
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=500000',
        
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=500000',
        
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=500000',
        
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=1 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=500000',
        
        
        
 
          
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=500000',
        
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=500000',
        
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=500000',
        
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=500000',
        
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=500000',
        
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=0.5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=5',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=50',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=500',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=5000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=50000',
        ' -# A_G1_C=0.0002 -# A_G1_P=3 -# A_G2_C=0.001 -# A_G2_P=8 -# A_DIAM=0.001 -# A_L=0.15 -# A_G1_T=10 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=500000',
        
        
        
        
        ' -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=15 -# A_D_PHI=0 -# A_H=0',
        ' -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=0',
        ' -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=0 -# A_D_THETA=75 -# A_D_PHI=0 -# A_H=0',
        ' -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=0 -# A_D_PHI=0 -# A_H=0',
        ' -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=0 -# A_H=0',
        ' -# A_DIAM=0.001 -# A_L=0.15 -# A_ROT=90 -# A_D_THETA=45 -# A_D_PHI=90 -# A_H=0'        
            
        
]
         




for i in range(start_sim, end_sim+1):
                     
        string_iteration = str(i).zfill(3)
        results_file  = 'results_' + string_iteration + '.out'
        
        
        #file_exist = os.path.exists(results_file)
        #if not file_exist:
                
                
        # 2025-07-15: New code to handle errors
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        error = 'yes'
        Nattempts = 100
        for j in range(Nattempts):
        
                try:
        
                
                        # Same code as before
                        # ********************************************************************************
                        print(' ')
                        print('-------------------------------------------')
                        print('FEKO simulation file ' + string_iteration + ' does not exist ... ')
                        print('-------------------------------------------')
                        print(' ')

                        
                                          
                        # Delete temporary files from project folder
                        # ------------------------------------------
                        process = subprocess.run('rm -f *.bof *.cfm *.fek *.out *.pre *.str', shell=True)
                        print(process.args)
                        print(process.returncode)
                        print(process.stdout)                
                        
                                              
                        
                        # Start simulation
                        # ----------------
                        print(' ')
                        print(' ')
                        print(' ')
                        print(' ')
                        print('------------------------------')
                        print('FEKO simulation running ...')
                        print(' ')
                        print('File: ' + project_file_no_extension[i] + '.cfx\n' + 'Parameters: ' + string_parameters[i])
                        print(' ')
                        
                        
                        l2 = 'export PATH=$PATH:~/2025/altair/feko/bin/  \n'
                        l3 = 'cadfeko_batch ' + project_file_no_extension[i] + '.cfx' + string_parameters[i] + ' \n'
                        l4 = 'runfeko ' + project_file_no_extension[i] + '.cfx -np all >/dev/null' + ' \n'
                        
                        file1 = open('fekorun.sh', 'w')
                        L = [l2, l3, l4]
                        file1.writelines(L)
                        file1.close()
                        
                        
                        # Run simulation
                        # --------------
                        time1 = time.time()
                        time.sleep(2)
                        
                        process = subprocess.run('bash fekorun.sh', shell=True)
                        print(process.args)
                        print(process.returncode)
                        print(process.stdout)
                        
                        time2 = time.time()
                        elapsed = str(np.round(time2-time1,4))
                        
                        
                        
                        
                        print('FEKO simulation DONE')
                        print('Computation time: ' + elapsed + ' seconds')
                        print('------------------------------')
                        print(' ')
                        print(' ')
                        print(' ')
                        print(' ')
                        
                        
                        # Renaming and moving results file       
                        os.rename(project_file_no_extension[i] + '.out', results_subfolder + '/' + results_file)
                        # ********************************************************************************                                
                        time.sleep(3)

                        error = 'no'
                            
                except:
                        pass
                                    
                if error == 'yes':
                        time.sleep(3)
                else:
                        break
                # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
