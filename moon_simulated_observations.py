
import os, sys
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import h5py as h5py

import astropy.io as aio

sys.path.insert(0, "/media/raul/SSD_RED_8TB/codes/global21cm/")
import general as gen
import astro as ast

sys.path.insert(0, "/media/raul/SSD_RED_8TB/codes/moon_subsurface/")
import moon_general as mg


par1   = sys.argv[1]	    
par2   = float(sys.argv[2])



'''

2024-12-05: This is the latest version, after correcting the "beam stretching" 
so that the convolution extends to angles below the horizon due to tropospheric and ionospheric refraction



How to run
-----------------------------------

 
python moon_simulated_observations.py a1


'''










def compute_antenna_temperature_v3(beam_case):

	'''

	site: 'a1', ..., 'f6' 

	'''
	

	# Beam model
	# ----------
	FLOW  = 1
	FHIGH = 120
	ix_list, fr, AZ_beam, EL_beam, di_shifted = mg.frequency_binned_beam(case=beam_case)
	freq_array = fr[(fr>= FLOW) & (fr<=FHIGH)]
	beam_array = di_shifted[(fr>= FLOW) & (fr<=FHIGH),:,:]


	# Converting beam and beam coordinate arrays to frequency-dependent 1D arrays
	# ---------------------------------------------------------------------------
	AZ_2D, EL_2D = np.meshgrid(AZ_beam, EL_beam)	
	AZa     = AZ_2D.flatten()
	ELa     = EL_2D.flatten()


	# Rotating beam relative to absolute celestial coordinates, i.e., AZ=0 and EL=0 corresponding to the true north and local meridian, respectively.
 	# ----------------------------------	
	angle_about_longaxis  =  0    # 0
	angle_about_shortaxis =  0    # 0 
	angle_about_vertical  =  0    # 0: antenna along north-south axis

	AZb, ELb = ast.rotation(AZa, ELa, 0, angle_about_longaxis)
	AZc, ELc = ast.rotation(AZb, ELb, 1, angle_about_shortaxis)
	AZd, ELd = ast.rotation(AZc, ELc, 2, angle_about_vertical)

	AZ_1D = np.copy(AZd)
	EL_1D = np.copy(ELd)


	# Array of flattened coordinates and beam
	# ---------------------------------------
	AZ_freq   = np.zeros((len(freq_array), len(AZ_1D)))
	EL_freq   = np.zeros((len(freq_array), len(AZ_1D)))	
	beam_freq = np.zeros((len(freq_array), len(AZ_1D)))

	for i in range(len(freq_array)):
		AZ_freq[i,:]   = AZ_1D
		EL_freq[i,:]   = EL_1D
		beam_freq[i,:] = beam_array[i,:,:].flatten()



	## Moon local coordinates of sky
	## -----------------------------
	#mjd_az_el_file = '/media/raul/SSD_4TB/EDGES_vol2/subsurface/observation_simulations/map_mjd_az_el/moon_2hr_ring_res6.hdf5'
	#MJD, AZ_mjd, EL_mjd = gen.read_hdf5_MJD_AZ_EL(mjd_az_el_file)


	## Horizon profile mask
	## --------------------
	#mask = np.ones((len(freq_array), len(MJD), len(AZ_mjd[0,:])))
	
	#EL_threshold = 0
	#for i in range(len(freq_array)):
		#for j in range(len(MJD)):
			#print([i, j])
			#xx = np.ones(len(EL_mjd[j]))
			#xx[EL_mjd[j] < EL_threshold] = 0
			#mask[i,j,:] = xx
			
					

	## Sky model
	## ---------
	#f_map, sky_model = ast.map_ULSA()   # nside=128


	## Computing results
	## -----------------
	#Ncpu = 16

	## NOTE: the same result is obtained with and without normalization of the beam solid angle 
	## because the normalization is just a multiplicative constant that gets cancelled out in the computation of the antenna temperature

	#ion_trans = np.ones((len(freq_array), len(AZ_freq)))    # Without tropospheric and ionospheric effects
	#mjd_out, freq_out, ant_temp_out = ast.parallel_convolution_test(MJD, freq_array, AZ_freq, EL_freq, beam_freq, ion_trans, AZ_mjd, EL_mjd, mask, sky_model, Ncpu)







	## Save results to binary file
	## ---------------------------

	#results_file        = '/media/raul/SSD_4TB/EDGES_vol2/subsurface/observation_simulations/sky_observation_' + beam_case + '.hdf5'
	#with h5py.File(results_file, 'w') as hf:
		#hf.create_dataset('mjd',      data = mjd_out)
		#hf.create_dataset('freq',     data = freq_out)
		#hf.create_dataset('ant_temp', data = ant_temp_out)






	#plt.figure()
	#plt.imshow(np.log(ant_temp_out), aspect='auto', interpolation=None)
	
	#plt.figure()
	#plt.loglog(freq_out, ant_temp_out.T)
	
	#plt.figure()
	#plt.plot(ant_temp_out[:,10])
	
	#plt.show()



	return 0 #lst_out, freq_out, ant_temp_out










def compute_antenna_temperature_v4(beam_file_no_extension, antenna_phi_angle):
	
	'''
	Use v3 for beams from Feko.
	Use this version (v4) for HDF5 beams from GO

	'''
	

	# Beam model
	# ----------
	FLOW  = 1
	FHIGH = 120
	
	file_path = '/media/raul/SSD_RED_8TB/EDGES_vol2/subsurface/gobeams/try4/' + beam_file_no_extension + '.hdf5'
	fr, theta, phi, gw, F_sky, sp, cf = mg.binned_gobeam(file_path, theta_step=1, antenna_phi_angle=antenna_phi_angle, weighted_average_pixels='yes')
	
	
	#fr, theta, phi, d, theta_binned, d_binned, theta_out, phi_out, d_out, sp, cf = mg.load_gobeam_hdf5('/media/raul/SSD_RED_8TB/EDGES_vol2/subsurface/gobeams/try2/' + beam_file_no_extension + '.hdf5', theta_step=1, antenna_phi_angle=antenna_phi_angle)
	# fr, theta, phi, d, theta_binned, d_binned, phi_f, d_f = mg.load_gobeam_hdf5('/media/raul/SSD_RED_8TB/EDGES_vol2/subsurface/gobeams/' + beam_file_no_extension + '.hdf5', theta_step=1)
	
	# AZ is equal to theta in two cases:
	# 1. When horizontal dipole was aligned with x-axis, from which theta is defined. Due to phi symmetry, the opposite signs of AZ and phi can be dismissed.
	# 2. When the dipole is orientated vertically along z-axis. Due to phi symmetry, the opposite signs of AZ and phi can be dismissed.
	AZ_beam = np.copy(phi)
	EL_beam = 90 - theta
	
	freq_array = fr[(fr>= FLOW) & (fr<=FHIGH)]
	beam_array = gw[(fr>= FLOW) & (fr<=FHIGH),:,:]


	# Converting beam and beam coordinate arrays to frequency-dependent 1D arrays
	# ---------------------------------------------------------------------------
	
	# Flattened coordinates
	# ---------------------
	AZ_2D, EL_2D = np.meshgrid(AZ_beam, EL_beam)	
	AZ_1D  = AZ_2D.flatten()
	EL_1D  = EL_2D.flatten()


	## Rotating beam relative to absolute celestial coordinates, i.e., AZ=0 and EL=90 corresponding to the true north and local meridian, respectively.
 	## ----------------------------------	
	#angle_about_longaxis  =  0    # 0
	#angle_about_shortaxis =  0    # 0 
	##angle_about_vertical  =  0    # 0: antenna along north-south axis

	#AZb, ELb = ast.rotation(AZa, ELa, 0, angle_about_longaxis)
	#AZc, ELc = ast.rotation(AZb, ELb, 1, angle_about_shortaxis)
	#AZd, ELd = ast.rotation(AZc, ELc, 2, angle_about_vertical)




	# Array of flattened coordinates and beam as a function of frequency
	# ------------------------------------------------------------------
	AZ_freq   = np.zeros((len(freq_array), len(AZ_1D)))
	EL_freq   = np.zeros((len(freq_array), len(AZ_1D)))	
	beam_freq = np.zeros((len(freq_array), len(AZ_1D)))

	for i in range(len(freq_array)):
		AZ_freq[i,:]   = AZ_1D
		EL_freq[i,:]   = EL_1D
		beam_freq[i,:] = beam_array[i,:,:].flatten()



	# Plotting beam in local coordinates as a cross-check
	# ---------------------------------------------------
	
	#plt.figure()
	#plt.plot(AZ_freq[0,:])
	#plt.xlabel('index')
	#plt.ylabel('AZ [deg]')
	
	#plt.figure()
	#plt.plot(EL_freq[0,:])
	#plt.xlabel('index')
	#plt.ylabel('EL [deg]')	
	
	
	#plt.figure()
	#plt.scatter(AZ_freq[0,:], EL_freq[0,:], c=beam_freq[0,:]); plt.colorbar()
	#plt.xlabel('AZ [deg]')
	#plt.ylabel('EL [deg]')
	#plt.title('directivity at 1 MHz')
	
	#plt.figure()
	#plt.scatter(AZ_freq[119,:], EL_freq[100,:], c=beam_freq[100,:]); plt.colorbar()
	#plt.xlabel('AZ [deg]')
	#plt.ylabel('EL [deg]')
	#plt.title('directivity at 120 MHz')
	
	#plt.show()




	# Moon local coordinates of sky
	# -----------------------------
	mjd_az_el_file = '/media/raul/SSD_RED_8TB/EDGES_vol2/subsurface/observation_simulations/map_mjd_az_el/moon_2hr_ring_res6.hdf5'
	MJD, AZ_mjd, EL_mjd = gen.read_hdf5_MJD_AZ_EL(mjd_az_el_file)


	# Horizon profile mask
	# --------------------
	mask = np.ones((len(freq_array), len(MJD), len(AZ_mjd[0,:])))
	
	# Computation is done for all directions above the moon horizon
	# -------------------------------------------------------------
	EL_threshold = np.min(EL_beam)  # Beam is provided only for directions with line of sight to the sky
	for i in range(len(freq_array)):
		for j in range(len(MJD)):
			#print([i, j])
			xx = np.ones(len(EL_mjd[j]))
			xx[EL_mjd[j] < EL_threshold] = 0	# Same mask is applied for all frequencies and mjds
			mask[i,j,:] = xx
			
					

	# Sky model
	# ---------
	f_map, sky_model = ast.map_ULSA()   # nside=128


	# Computing results
	# -----------------
	Ncpu = 64

	# NOTE: the same result is obtained with and without normalization of the beam solid angle 
	# because the normalization is just a multiplicative constant that gets cancelled out in the computation of the antenna temperature

	ion_trans = np.ones((len(freq_array), len(AZ_freq)))    # Without tropospheric and ionospheric effects
	mjd_out, freq_out, ant_temp_out = ast.parallel_convolution_test(MJD, freq_array, AZ_freq, EL_freq, beam_freq, ion_trans, AZ_mjd, EL_mjd, mask, sky_model, Ncpu)







	# Save results to binary file
	# ---------------------------

	results_file        = '/media/raul/SSD_RED_8TB/EDGES_vol2/subsurface/observation_simulations/beams_gomoon/try4/sky_obs_' + beam_file_no_extension + '_' + str(int(antenna_phi_angle)) + 'deg.hdf5'
	with h5py.File(results_file, 'w') as hf:
		hf.create_dataset('mjd',      data = mjd_out)
		hf.create_dataset('freq',     data = freq_out)
		hf.create_dataset('ant_temp', data = ant_temp_out)




	return 0 #lst_out, freq_out, ant_temp_out


















#compute_antenna_temperature_v3(par1)

compute_antenna_temperature_v4(par1, par2)







