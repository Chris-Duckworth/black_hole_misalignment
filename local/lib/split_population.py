'''
split_populations - functions to split the tng100 manga like sample.
'''

import numpy as np
import pandas as pd


def tng100_pa_sample(tng100_main):
    '''
    For the matched manga-like TNG100 sample, this returns the pa defined. Since our TNG100 
    sample is already only matched to main sample manga galaxies we dont have to do the pre-
    selection.
    '''
    tng100_pa = tng100_main[(tng100_main.stel_feature == 0) & (tng100_main.halpha_feature == 0) & ((tng100_main.stel_qual == 1) | (tng100_main.stel_qual == 2)) & ((tng100_main.halpha_qual == 1) | (tng100_main.halpha_qual == 2))]
    return tng100_pa


def SFMS_breakdown(tab):
    '''
    This function splits into individual dataframes based on the flags in annalisa's flags.
    '''
    QU = tab[tab.sfms_flag == 0]
    SF = tab[tab.sfms_flag == 1]
    GV = tab[tab.sfms_flag == -1]
    return QU, SF, GV


def combine_with_tree_split_on_pa(tab, tree_tab, lower_PA=30, upper_PA=30):
    '''
    Function that takes a defined sample in the TNG100 - MPL-8 matched population, combines
    with supplementary tree info (for the main branch) and then splits on PA. Returns 3 
    tables; total info, aligned and misaligned
    '''
    all_tab = tree_tab[tree_tab.root_subfind.isin(tab.subfind_id.values)]
    align_tab = tree_tab[tree_tab.root_subfind.isin(tab.subfind_id.values[tab.pa_offset.values < lower_PA])]
    mis_tab = tree_tab[tree_tab.root_subfind.isin(tab.subfind_id.values[tab.pa_offset.values >= upper_PA])]
    
    print('All:'+str(all_tab.shape[0] / 50)+' Aligned:'+str(align_tab.shape[0] /50)+' Misaligned:'+str(mis_tab.shape[0] /50))

    return all_tab, align_tab, mis_tab


def combine_with_tree_split_on_pa_and_group(tab, tree_tab, lower_PA=30, upper_PA=30):
    '''
    Function that takes a defined sample in the TNG100 - MPL-8 matched population, combines
    with supplementary tree info (for the main branch) and then splits on both PA and group
    membership (i.e. central or satellite). Returns 6 tables; total info, aligned and misaligned
    for centrals and then satellites.
    '''
    cen_all_tab = tree_tab[tree_tab.root_subfind.isin(tab.subfind_id.values[tab.central_flag.values == 1])]
    cen_align_tab = tree_tab[tree_tab.root_subfind.isin(tab.subfind_id.values[(tab.pa_offset.values < lower_PA) & (tab.central_flag.values == 1)])]
    cen_mis_tab = tree_tab[tree_tab.root_subfind.isin(tab.subfind_id.values[(tab.pa_offset.values >= upper_PA) & (tab.central_flag.values == 1)] )]
    
    print('Centrals. All:'+str(cen_all_tab.shape[0] / 50)+' Aligned:'+str(cen_align_tab.shape[0] /50)+' Misaligned:'+str(cen_mis_tab.shape[0] /50))
    
    sat_all_tab = tree_tab[tree_tab.root_subfind.isin(tab.subfind_id.values[tab.central_flag.values == 0])]
    sat_align_tab = tree_tab[tree_tab.root_subfind.isin(tab.subfind_id.values[(tab.pa_offset.values < lower_PA) & (tab.central_flag.values == 0)])]
    sat_mis_tab = tree_tab[tree_tab.root_subfind.isin(tab.subfind_id.values[(tab.pa_offset.values >= upper_PA) & (tab.central_flag.values == 0)] )]
    
    print('Satellites. All:'+str(sat_all_tab.shape[0] / 50)+' Aligned:'+str(sat_align_tab.shape[0] /50)+' Misaligned:'+str(sat_mis_tab.shape[0] /50))
	
    return cen_all_tab, cen_align_tab, cen_mis_tab, sat_all_tab, sat_align_tab, sat_mis_tab


def combine_with_tree_split_on_pa_and_mass(tab, tree_tab, lower_PA=30, upper_PA=30, lower_percentile=25, upper_percentile=75, verbose=False):
    '''
    Function that takes a defined sample in the TNG100 - MPL-8 matched population, combines
    with supplementary tree info (for the main branch) and then splits on both PA and mass 
    of the object at z=0.
    By default the top and bottom quartile are returned.
    Returns 6 tables; total info, aligned and misaligned for high mass and low mass.
    ''' 
    lower_mass = np.percentile(tab.stel_mass.values, lower_percentile)
    upper_mass = np.percentile(tab.stel_mass.values, upper_percentile)
	
    high_mass_all_tab = tree_tab[tree_tab.root_subfind.isin(tab.subfind_id.values[tab.stel_mass.values > upper_mass])]
    high_mass_align_tab = tree_tab[tree_tab.root_subfind.isin(tab.subfind_id.values[(tab.pa_offset.values < lower_PA) & (tab.stel_mass.values > upper_mass)])]
    high_mass_mis_tab = tree_tab[tree_tab.root_subfind.isin(tab.subfind_id.values[(tab.pa_offset.values >= upper_PA) & (tab.stel_mass.values > upper_mass)] )]
        
    low_mass_all_tab = tree_tab[tree_tab.root_subfind.isin(tab.subfind_id.values[tab.stel_mass.values <= lower_mass])]
    low_mass_align_tab = tree_tab[tree_tab.root_subfind.isin(tab.subfind_id.values[(tab.pa_offset.values < lower_PA) & (tab.stel_mass.values <= lower_mass)])]
    low_mass_mis_tab = tree_tab[tree_tab.root_subfind.isin(tab.subfind_id.values[(tab.pa_offset.values >= upper_PA) & (tab.stel_mass.values <= lower_mass)] )]
    
    if verbose == True:
        print('High mass. All:'+str(high_mass_all_tab.shape[0] / 50)+' Aligned:'+str(high_mass_align_tab.shape[0] /50)+' Misaligned:'+str(high_mass_mis_tab.shape[0] /50))
        print('Low mass.  All:'+str(low_mass_all_tab.shape[0] /50)+' Aligned:'+str(low_mass_align_tab.shape[0] / 50)+' Misaligned:'+str(low_mass_mis_tab.shape[0] / 50))
    
    return high_mass_all_tab, high_mass_align_tab, high_mass_mis_tab, low_mass_all_tab, low_mass_align_tab, low_mass_mis_tab


