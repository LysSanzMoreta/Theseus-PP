# Theseus-PP
Protein superposition using probabilistic programming in Pyro


Publication: https://ieeexplore.ieee.org/document/8791469

Citation:
```
@INPROCEEDINGS{theseusPP2019,
author={L. S. {Moreta} and A. S. {Al-Sibahi} and D. {Theobald} and W. {Bullock} and B. N. {Rommes} and A. {Manoukian} and T. {Hamelryck}},
booktitle={2019 IEEE Conference on Computational Intelligence in Bioinformatics and Computational Biology (CIBCB)},
title={A Probabilistic Programming Approach to Protein Structure Superposition},
year={2019},
volume={},
number={},
pages={1-5},
keywords={Bayes methods;biology computing;expectation-maximisation algorithm;iterative methods;maximum likelihood estimation;molecular biophysics;proteins;Bayesian model;THESEUS model;probabilistic model;protein superposition;latent mean structure;deep probabilistic programming language Pyro;maximum likelihood estimation;Bayesian probabilistic models;biomolecular structure;Bayesian protein structure prediction;probabilistic programming approach;protein structure superposition;correlated atom positions;THESEUS-PP model;MAP estimation;Proteins;Probabilistic logic;Covariance matrices;Bayes methods;Biological system modeling;Quaternions;Programming;protein superposition;Bayesian modelling;deep probabilistic programming;protein structure prediction},
doi={10.1109/CIBCB.2019.8791469},
ISSN={null},
month={July},}
```



The Calling_SUPERPOSION.py file is designed to call the Theseus-PP model n amount of times with different seeds




https://user-images.githubusercontent.com/34369639/153401150-7a7bdfea-1a88-4407-9087-3fbc15007c77.mp4


The input data is managed on this line of Calling_SUPERPOSITION.py: https://github.com/LysSanzMoreta/Theseus-PP/blob/master/Calling_SUPERPOSITION.py#L31

DataManagement.Read_Data('../PDB_files/{}.pdb'.format(name1), '../PDB_files/{}.pdb'.format(name2),type='all',models =(0,100),RMSD=True)

- The files are in a **PDB_files folder** in the same directory
- name1 and name2 are usually the same file name, but they are separated because some proteins NMR coordinates are divided in 2 different files (1adz1T and 1adz0T)<br/><br/>
a) *PDB files containing a **single** sequence/model* <br/><br/>
- type = "all"---> for the PDB with a single sequence/model
- models = (0,len(seq))----> for the PDB with a single sequence. The number indicates the number of aa to be included<br/><br/>
b) *PBD files containing **>1** models* <br/><br/>
- type = "models"
- models = (0,3) ------> for the protein files with several models in the same PDB. The number of the models to be compared
- RMSD = True, indicates if the superposition is initialized with the RMSD (Kabsch)
