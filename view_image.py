import numpy as np
import h5py 
import matplotlib.pyplot as plt

f = h5py.File('/sf/alvra/data/p17982/raw/camera_test/run_000001.BSREAD.h5_SARES11-XMI125-C4P1.h5')

xy = np.array(f['data/SARES11-XMI125-C4P1:FPICTURE/data'][0,:,:])
print xy
plt.imshow(xy)
plt.xlabel('Pixel')
plt.ylabel('Shot number')
plt.show()


