import numpy as np
import netCDF4 as NC

GRID = '05'

grid_handle = NC.Dataset ('./ocean_hgrid_'+GRID+'.nc',mode = 'r' )
topog_handle = NC.Dataset ('./topog_'+GRID+'.nc',mode = 'r' )

# 2. Read in Super Grid
# 3. Read in Topog

H_LON = grid_handle.variables['x'][1::2,1::2]
H_LAT = grid_handle.variables['y'][1::2,1::2]
H_DPT = topog_handle.variables['depth'][:,:]

L1,L2 = np.shape(H_DPT)

H_MSK_SP_NP=np.ones(np.shape(H_DPT))
H_MSK_80_NP=np.zeros(np.shape(H_DPT))
H_MSK_75_NP=np.zeros(np.shape(H_DPT))
H_MSK_SP_88=np.zeros(np.shape(H_DPT))
H_MSK_80_88=np.zeros(np.shape(H_DPT))

for ii in range(L1):
    for jj in range(L2):
        if (H_LAT[ii,jj]>75):
            H_MSK_75_NP[ii,jj]=1
        if (H_LAT[ii,jj]>80):
            H_MSK_80_NP[ii,jj]=1
        if (H_LAT[ii,jj]>80 and H_LAT[ii,jj]<88):
            H_MSK_80_88[ii,jj]=1
        if (H_LAT[ii,jj]<88):
            H_MSK_SP_88[ii,jj]=1

fg1=open('./GlobTriPolar_'+GRID+'.Mask_80_88','w')
fg2=open('./GlobTriPolar_'+GRID+'.Mask_SP_88','w')
fg3=open('./GlobTriPolar_'+GRID+'.Mask_80_NP','w')
fg4=open('./GlobTriPolar_'+GRID+'.Mask_SP_NP','w')
fg5=open('./GlobTriPolar_'+GRID+'.Mask_75_NP','w')

fd1=open('./GlobTriPolar_'+GRID+'.1000.Dpt','w')
fd2=open('./GlobTriPolar_'+GRID+'.Dpt','w')
f3=open('./GlobTriPolar_'+GRID+'.Obstr','w')
f4=open('./GlobTriPolar_'+GRID+'.Lat','w')
f5=open('./GlobTriPolar_'+GRID+'.Lon','w')

for ii in range(L1):
    for jj in range(L2):
        fg1.write(str(H_MSK_80_88[ii,jj])+' ')
        fg2.write(str(H_MSK_SP_88[ii,jj])+' ')
        fg3.write(str(H_MSK_80_NP[ii,jj])+' ')
        fg4.write(str(H_MSK_SP_NP[ii,jj])+' ')
        fg5.write(str(H_MSK_75_NP[ii,jj])+' ')
        fd1.write(str(-1000.)+' ')
        fd2.write(str(H_DPT[ii,jj])+' ')
        f3.write(str(0.)+' ')
        f4.write(str(H_LAT[ii,jj])+' ')
        f5.write(str(H_LON[ii,jj])+' ')
    fg1.write('\n')
    fg2.write('\n')
    fg3.write('\n')
    fg4.write('\n')
    fg5.write('\n')
    fd1.write('\n')
    fd2.write('\n')
    f3.write('\n')
    f4.write('\n')
    f5.write('\n')

for ii in range(L1):
    for jj in range(L2):
        f3.write(str(0.)+' ')
    f3.write('\n')

fg1.close()
fg2.close()
fg3.close()
fg4.close()
fg5.close()
fd1.close()
fd2.close()
f3.close()
f4.close()
f5.close()
