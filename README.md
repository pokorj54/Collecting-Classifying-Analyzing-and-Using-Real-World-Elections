# Collecting, Classifying, Analyzing, and Using Real World Elections

This repository contains election data generated as part of the paper "Niclas Boehmer, and Nathan Schaar. Collecting, Classifying, Analyzing, and Using Real-World Elections".

The data is described in detail in the paper. In the folder "raw", we store the unprocessed election data. In the folder "complete", we store complete versions of our elections obtained from the raw elections by deleting voters and candidates until each voter ranks all candidates. In the folder "normalized", we store for each dataset 500 "normalized" elections with 15 candidates and 30 voters generated from the complete elections from this dataset as described in the paper. 

The data is stored in the simple election data format introduced in the [PrefLib](www.preflib.org/data/format) library for preferences.

Please cite the above paper if you use our data. In case you have any questions, please contact me under <niclas.boehmer@tu-berlin.de>.
