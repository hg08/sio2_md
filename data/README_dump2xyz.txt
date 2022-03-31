#STEP 1
# use command `%s/ITEM: TIMESTEP/1536/g`

#STEP 2
awk -v N=1536 '{if (NR%(N+9) <3 && NR%(N+9) >0) print -bash; else if ((NR%(N+9) ==0 || NR%(N+9)>9) && ==1) print $2, $3, $4, $5}' dump.data > pos_1.dat
awk -v N=1536 '{if (NR%(N+9) <3 && NR%(N+9) >0) print -bash; else if ((NR%(N+9) ==0 || NR%(N+9)>9) && ==2) print $2, $3, $4, $5}' dump.data > pos_2.dat
