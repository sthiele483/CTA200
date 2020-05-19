import pandas as pd
import numpy as np
from cosmic.sample.initialbinarytable import InitialBinaryTable
from cosmic.evolve import Evolve

BSEDict = {'xi': 0.5, 'bhflag': 1, 'neta': 0.5, 'windflag': 3, 'wdflag': 1, 'alpha1': 1.0,
           'pts1': 0.001, 'pts3': 0.02, 'pts2': 0.01, 'epsnov': 0.001, 'hewind': 0.5,
           'ck': 1000, 'bwind': 0.0, 'lambdaf': 0.0, 'mxns': 2.5, 'beta': -1.0, 'tflag': 1,
           'acc2': 1.5, 'remnantflag': 3, 'ceflag': 0, 'eddfac': 1.0, 'ifflag': 0, 'bconst': 3000,
           'sigma': 265.0, 'gamma': -2.0, 'pisn': 45.0,
           'natal_kick_array' : [[-100.0,-100.0,-100.0,-100.0,0.0], [-100.0,-100.0,-100.0,-100.0,0.0]],
           'bhsigmafrac' : 1.0, 'polar_kick_angle' : 90,
           'qcrit_array' : [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
           'cekickflag' : 2, 'cehestarflag' : 0, 'cemergeflag' : 0, 'ecsn' : 2.5, 'ecsn_mlow' : 1.4,
           'aic' : 1, 'ussn' : 0, 'sigmadiv' :-20.0, 'qcflag' : 2, 'eddlimflag' : 0,
           'fprimc_array' : [2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,
                             2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0,2.0/21.0],
           'bhspinflag' : 0, 'bhspinmag' : 0.0, 'rejuv_fac' : 1.0, 'rejuvflag' : 0, 'htpmb' : 1,
           'ST_cr' : 1, 'ST_tide' : 1, 'bdecayfac' : 1, 'rembar_massloss' : 0.5, 'zsun' : 0.017}


final_kstar1 = [10, 11, 12]
final_kstar2 = [10, 11, 12]
prim_mod = 'kroupa01'
ecc_mod = 'uniform'
porb_mod = 'sana12'
SF_st = 13700.0
SF_d = 0.0
Z = 0.017
num = 10000

InitBin, mass_singles, mass_binaries, n_singles, n_binaries = InitialBinaryTable.sampler('independent',
                                                                                                 final_kstar1,
                                                                                                 final_kstar2,
                                                                                                 binfrac_model=0.5,
                                                                                                 primary_model=prim_mod,
                                                                                                 ecc_model=ecc_mod,
                                                                                                 porb_model=porb_mod,
                                                                                                 SF_start=SF_st,
                                                                                                 SF_duration=SF_d,
                                                                                                 met=Z, size=num)

bpp, bcm, initC, kick = Evolve.evolve(initialbinarytable=InitBin, BSEDict=BSEDict, n=8)
bpp.to_hdf('datafile.hdf', key='bpp')
bcm.to_hdf('datafile.hdf', key='bcm')
initC.to_hdf('datafile.hdf', key='bcm')
