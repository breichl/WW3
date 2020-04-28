#!/bin/bash
#

cd ../bin

./run_clean ../../model

Grid='05'

Cases="AlongSeam CrossSeam"
for case in $Cases
do
    ./run_test -g ${Grid} -o netcdf -i input_$case -s PR1_MPI -w work${Grid}/PR1_MPI.80_NP.$case ../../model ../ww3_tp2.18
    ./run_test -g ${Grid}_TRPL_REFR -o netcdf -i input_AlongSeam -s PR1_MPI -w work${Grid}/PR1_MPI.80_NP.TRPL_REFR.$case ../../model ../ww3_tp2.18
    ./run_test -g ${Grid}_TRPL -o netcdf -i input_$case -s PR1_MPI -w work${Grid}/PR1_MPI.80_NP.TRPL.$case ../../model ../ww3_tp2.18

    ./run_test -g ${Grid}_m88 -o netcdf -i input_$case -s PR1_MPI -w work${Grid}/PR1_MPI.80_88.$case ../../model ../ww3_tp2.18
    ./run_test -g ${Grid}_m88_TRPL_REFR -o netcdf -i input_$case -s PR1_MPI -w work${Grid}/PR1_MPI.80_88.TRPL_REFR.$case ../../model ../ww3_tp2.18
    ./run_test -g ${Grid}_m88_TRPL -o netcdf -i input_$case -s PR1_MPI -w work${Grid}/PR1_MPI.80_88.TRPL.$case ../../model ../ww3_tp2.18
done

./run_clean ../../model

for case in $Cases
do
    ./run_test -g ${Grid} -o netcdf -i input_$case -s PR1_MPI_GLOC -w work${Grid}/PR1_MPI_GLOC.80_NP.$case ../../model ../ww3_tp2.18
    ./run_test -g ${Grid}_TRPL_REFR -o netcdf -i input_$case -s PR1_MPI_GLOC -w work${Grid}/PR1_MPI_GLOC.80_NP.TRPL_REFR.$case ../../model ../ww3_tp2.18
    ./run_test -g ${Grid}_TRPL -o netcdf -i input_$case -s PR1_MPI_GLOC -w work${Grid}/PR1_MPI_GLOC.80_NP.TRPL.$case ../../model ../ww3_tp2.18

    ./run_test -g ${Grid}_m88 -o netcdf -i input_$case -s PR1_MPI_GLOC -w work${Grid}/PR1_MPI_GLOC.80_88.$case ../../model ../ww3_tp2.18
    ./run_test -g ${Grid}_m88_TRPL_REFR -o netcdf -i input_$case -s PR1_MPI_GLOC -w work${Grid}/PR1_MPI_GLOC.80_88.TRPL_REFR.$case ../../model ../ww3_tp2.18
    ./run_test -g ${Grid}_m88_TRPL -o netcdf -i input_$case -s PR1_MPI_GLOC -w work${Grid}/PR1_MPI_GLOC.80_88.TRPL.$case ../../model ../ww3_tp2.18
done
