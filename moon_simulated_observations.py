
import os, sys
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import h5py as h5py

import astropy.io as aio

sys.path.insert(0, "/home/raul/codes/global21cm/")
import general as gen
import astro as ast

sys.path.insert(0, "/home/raul/codes/substrate/")
import moon_general as mg


par1   = sys.argv[1]	    # a1, a2, ...., f5, f6




'''

2024-12-05: This is the latest version, after correcting the "beam stretching" 
so that the convolution extends to angles below the horizon due to tropospheric and ionospheric refraction



How to run
-----------------------------------

 
python moon_simulated_observations.py a1


'''









def compute_coordinate_file(save_file_hdf5, INST_height_m=1, Ncpu=1):

	'''

	Restart Ipython before running this function	


	'''

	# Loading RING galactic coordinates with NSIDE=64 (ULSA maps are in RING format and NSIDE=64)
	# -------------------------------------------------------------------------------------------
	galactic_coord_file = '/media/raul/SSD_RED_8TB/sky_models/coordinate_maps/pixel_coords_map_ring_galactic_res6.fits'
	coord         = aio.fits.open(galactic_coord_file)
	coord_array   = coord[1].data
	lon           = coord_array['LONGITUDE']
	lat           = coord_array['LATITUDE']


	
	MJD, AZ, EL = ast.parallel_galactic_to_moon_local_coordinates_lunar_day(lon, lat, Ncpu, INST_lat_deg=0, INST_lon_deg=180, INST_height_m=INST_height_m, hours_offset=2)

	#Save results to binary file
	save_folder = '/media/raul/SSD_RED_8TB/EDGES_vol2/subsurface/observation_simulations/map_mjd_az_el/'
	with h5py.File(save_folder + save_file_hdf5, 'w') as hf:
		hf.create_dataset('MJD', data = MJD)
		hf.create_dataset('AZ',  data = AZ)
		hf.create_dataset('EL',  data = EL)


	return 0 #MJD, AZ, EL






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


	# Moon local coordinates of sky
	# -----------------------------
	mjd_az_el_file = '/media/raul/SSD_4TB/EDGES_vol2/subsurface/observation_simulations/map_mjd_az_el/moon_2hr_ring_res6.hdf5'
	MJD, AZ_mjd, EL_mjd = gen.read_hdf5_MJD_AZ_EL(mjd_az_el_file)


	# Horizon profile mask
	# --------------------
	mask = np.ones((len(freq_array), len(MJD), len(AZ_mjd[0,:])))
	
	EL_threshold = 0
	for i in range(len(freq_array)):
		for j in range(len(MJD)):
			print([i, j])
			xx = np.ones(len(EL_mjd[j]))
			xx[EL_mjd[j] < EL_threshold] = 0
			mask[i,j,:] = xx
			
					

	# Sky model
	# ---------
	f_map, sky_model = ast.map_ULSA()   # nside=128


	# Computing results
	# -----------------
	Ncpu = 16

	# NOTE: the same result is obtained with and without normalization of the beam solid angle 
	# because the normalization is just a multiplicative constant that gets cancelled out in the computation of the antenna temperature

	ion_trans = np.ones((len(freq_array), len(AZ_freq)))    # Without tropospheric and ionospheric effects
	mjd_out, freq_out, ant_temp_out = ast.parallel_convolution_test(MJD, freq_array, AZ_freq, EL_freq, beam_freq, ion_trans, AZ_mjd, EL_mjd, mask, sky_model, Ncpu)







	# Save results to binary file
	# ---------------------------

	results_file        = '/media/raul/SSD_4TB/EDGES_vol2/subsurface/observation_simulations/sky_observation_' + beam_case + '.hdf5'
	with h5py.File(results_file, 'w') as hf:
		hf.create_dataset('mjd',      data = mjd_out)
		hf.create_dataset('freq',     data = freq_out)
		hf.create_dataset('ant_temp', data = ant_temp_out)






	#plt.figure()
	#plt.imshow(np.log(ant_temp_out), aspect='auto', interpolation=None)
	
	#plt.figure()
	#plt.loglog(freq_out, ant_temp_out.T)
	
	#plt.figure()
	#plt.plot(ant_temp_out[:,10])
	
	#plt.show()



	return 0 #lst_out, freq_out, ant_temp_out



compute_antenna_temperature_v3(par1)








