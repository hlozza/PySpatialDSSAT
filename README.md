# PySpatialDSSAT

Python3 code for sequential processing of soil features with the DSSAT-CSM. 

## Overview

The DSSAT-CSM simulates the growth and development of crops in interaction with the environment under different treatment proposals (See [DSSAT.net](https://dssat.net).
The original model runs simulations at plot scale. This code allows you to sequentially run the model on multiple plots or units defined in a Shapefile. In particular, the biomass productions computed for each unit are stored in a new vector layer. So the spatial variability for the given treatment is much easier to analyze with the aid of a GIS.

## Contents

Some dummy test data are provided under `CSM` and `Resources` folders 
to check the code. The outcome can be found on `Output` folder.  

## Installation and execution

For further details on the installation and the execution, please consult [Readme_Install.md](Readme_Install.md).


