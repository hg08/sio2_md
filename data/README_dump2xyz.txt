#STEP 1
# use command `%s/ITEM: TIMESTEP/1536/g`

#STEP 2
(base) mac@gangMac:~/github/sio2_md/data (main)$ awk -v N=1536 '{if (NR%(N+9)<3 && NR%(N+9)>0) print $0; else if ((NR%(N+9)==0 || NR%(N+9)>9) && $2==1) print $0}' dump.data > pos1.xyz
(base) mac@gangMac:~/github/sio2_md/data (main)$ awk -v N=1536 '{if (NR%(N+9)<3 && NR%(N+9)>0) print $0; else if ((NR%(N+9)==0 || NR%(N+9)>9) && $2==2) print $0}' dump.data > pos2.xyz

#STEP 3
(base) mac@gangMac:~/github/sio2_md/data (main)$ awk -v OFS='\t' '
    NF<pNF || NR==1 { blockNr++ }
    { print blockNr, NF, NR, (NF>1 ? $1 : NR), $0; pNF=NF }
' pos1.xyz | sort -n -k1,1 -k2,2 -k4,4 -k3,3 | cut -f5- > pos_1
(base) mac@gangMac:~/github/sio2_md/data (main)$ vi pos_1
(base) mac@gangMac:~/github/sio2_md/data (main)$ awk -v OFS='\t' '
    NF<pNF || NR==1 { blockNr++ }
    { print blockNr, NF, NR, (NF>1 ? $1 : NR), $0; pNF=NF }
' pos2.xyz | sort -n -k1,1 -k2,2 -k4,4 -k3,3 | cut -f5- > pos_2

#STEP 4
(base) mac@gangMac:~/github/sio2_md/data (main)$ awk 'NR<514001{print $0}' pos_1 > pos_1.xyz
(base) mac@gangMac:~/github/sio2_md/data (main)$ awk 'NR<1026001{print $0}' pos_2 > pos_2.xyz

#STEP 5
(base) mac@gangMac:~/github/sio2_md/data (main)$ awk -v N=512 -v a=28.640 '{if (NR%(N+2)<3 && NR%(N+2)>0) print $0; else if (NR%(N+2)==0 || NR%(N+2)>2) print $2, a*$3, a*$4, a*$5}' pos_1.xyz > pos_1a.xyz
(base) mac@gangMac:~/github/sio2_md/data (main)$ awk -v N=1024 -v a=28.640 '{if (NR%(N+2)<3 && NR%(N+2)>0) print $0; else if (NR%(N+2)==0 || NR%(N+2)>2) print $2, a*$3, a*$4, a*$5}' pos_2.xyz > pos_2a.xyz

# STEP extra
mv pos_1a.xyz pos_1.xyz
mv pos_2a.xyz pos_2.xyz
