# Theseus-PP
Protein superposition using probabilistic programming in Pyro


Publication & Citations: https://ieeexplore.ieee.org/document/8791469



The Calling_SUPERPOSION.py file is designed to call the Theseus-PP model n amount of times with different seeds



The input data is managed on this line of Calling_SUPERPOSITION.py: 

DataManagement.Read_Data('../PDB_files/{}.pdb'.format(name1), '../PDB_files/{}.pdb'.format(name2),type='all',models =(0,100),RMSD=True)

- The files are in the PDB_files folder in the same directory
- name1 and name2 are usually the same file name, but they are separated because some proteins NMR coordinates are divided in 2 different files (1adz1T and 1adz0T)
- type = "all"---> for the PDB with a single sequence
- type = "models" ---> for the protein files with several models in the same PDB
- models = (0,len(seq))----> for the PDB with a single sequence. The number indicates the number of aa to be included
- models = (0,3) ------> for the protein files with several models in the same PDB. The number of the models to be compared
- RMSD = True, indicates if the superposition is initialized with the RMSD
