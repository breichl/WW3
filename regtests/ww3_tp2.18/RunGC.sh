#!/bin/bash
#

cd ../bin

#./run_clean ../../model

#./run_test -g 05_m70_TRPL -o netcdf -i input_GCtest -s PR1_MPI_GLOC -w workGC/TRPL ../../model ../ww3_tp2.18
./run_test -g 05_m70_TRPL_REFR -o netcdf -i input_GCtest -s PR1_MPI_GLOC -w workGC/TRPL_REFR ../../model ../ww3_tp2.18
