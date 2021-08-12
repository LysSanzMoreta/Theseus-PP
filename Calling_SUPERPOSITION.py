import numpy as np
import statistics
from random import randint
from SUPERPOSITION import *
#from SUPERPOSITION_Animation import *
import torch
import time
import pandas as pd
import timeit
name1 = '1zwg' #2nl7:139 #2do0=114
name2 ='1zwg'
models = (0,3)


def random_with_N_digits(n):
    """Generates a random number of n length to switch the torch seeds in each iteration"""
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
#Number of times to run the model
iterations=1
#Dataframe to save results information and computational times:
DistancesDataframe = pd.DataFrame()
TimesDataframe=pd.DataFrame()
distances_list=[]
iterations_list=[]
duration_list=[]

for i in range(iterations):
    torch.manual_seed(random_with_N_digits(10))
    #Read the data, calculate distance of the structure to the origin and the average structure between the inputs
    data_obs = data_management.Read_Data('../PDB_files/{}.pdb'.format(name1), '../PDB_files/{}.pdb'.format(name2),type='chains',models =models,RMSD=True)
    max_var = data_management.Max_variance(data_obs[0])  # calculate the max pairwise distance to origin of the structure to set as value for max variance in the prior for mean struct
    average = data_management.Average_Structure(data_obs)
    data1, data2 = data_obs
    #Write the RMSD superimposed C alpha traces to a PDB file and visualize it in Pymol
    data_management.write_ATOM_line(data1, 'RMSD_{}_data1.pdb'.format(name1))
    data_management.write_ATOM_line(data2, 'RMSD_{}_data2.pdb'.format(name2))
    data_management.Pymol("RMSD_{}_data1.pdb".format(name1), "RMSD_{}_data2.pdb".format(name2))
    data_obs = max_var, data1, data2
    #Run the model and extract the parameters
    #SuperpositionModel.Run(data_obs, average, name1) #For Superposition Animation
    #exit()
    T2, R, M, X1, X2,distances,info,duration = superposition_model.Run(data_obs, average, name1)

    duration_list.append(duration)
    iterations_list.append(info[0])
    data_management.write_ATOM_line(M, 'M.pdb')
    data_management.write_ATOM_line(X1, 'Result_{}_X1.pdb'.format(name1))
    data_management.write_ATOM_line(X2, 'Result_{}_X2.pdb'.format(name2))
    data_management.Write_PDB(r"../PDB_files/{}.pdb".format(name2), np.transpose(R), -T2,'Transformed')
    data_management.Pymol("Result_{}_X1.pdb".format(name1), "Result_{}_X2.pdb".format(name2))
    distances_list.append(pd.Series(np.round(distances)).astype(int))
    print("Done_{}".format(i))

#Save the results and print them
DistancesDataframe = pd.concat(distances_list,axis=1).reset_index(drop=True).T
DistancesDataframe.loc[len(DistancesDataframe)]= DistancesDataframe.apply(lambda x: x.duplicated()).sum()
DistancesDataframe.to_csv("DistancesCheckpoint_{}".format(name1),sep='\t')
Results=DistancesDataframe.loc[DistancesDataframe.shape[0]-1].values.tolist() #.apply(lambda x: x.tolist(), axis=1)


print("Percentage:" + str((Results.count(iterations-1)/DistancesDataframe.shape[1])*100))
print("Iterations average:" + str(sum(iterations_list)/len(iterations_list)) + "\t"+"Standard Deviation:" + str(statistics.stdev(iterations_list)))
print("Running Time average:" + str(sum(duration_list)/len(duration_list)) + "\t"+ "Standard Deviation:" + str(statistics.stdev(duration_list)))
print(str(sum(duration_list)/len(duration_list)) + '\t' + str(statistics.stdev(duration_list)) + '\t' + str(sum(iterations_list)/len(iterations_list)) + "\t" + str(statistics.stdev(iterations_list)))
print(str(sum(duration_list)/len(duration_list))+"$\pm$" + str(statistics.stdev(duration_list))+ "&" +str(sum(iterations_list)/len(iterations_list))+"$\pm$"+str(statistics.stdev(iterations_list)) +"\\")