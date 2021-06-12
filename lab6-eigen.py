from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

def compressImg(X):
    
    X_centered = X - X.mean(axis=0)
    m = X.shape[0]
    X_cov = np.dot(X_centered.T, X_centered) / (m - 1)
    eigenvalues, eigenvectors = np.linalg.eig(X_cov)
    eigenvalues = np.real(eigenvalues)
    eigenvectors = np.real(eigenvectors)
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:,idx]
    # print(f'Eigenvectors: {eigenvectors.shape}, engenvalues: {eigenvalues.shape}')
    percent = 0
    k = 0
    for i in eigenvalues:
        k+=1
        percent += i/sum(eigenvalues)
        if(percent > .9):
            break
    ev = np.array(eigenvectors[:, :k], ndmin=2)
    pcaT = np.array(np.dot(X_centered, ev), ndmin=2)
    evT = np.array(eigenvectors[:, :k], ndmin=2).T
    X_reconstructed = np.dot(pcaT, evT) + X.mean(axis=0)
    X_reconstructed = X_reconstructed.astype(int)
    print(evT.shape, ' ', pcaT.shape)
    return X_reconstructed
    # imgRec = Image.fromarray(X_reconstructed)
    # return imgRec

dims = (250,250)
X_main = []
for file in os.listdir("./EigenFaces"):
    if(not file.endswith('.jpg')):
        continue
    img = Image.open(f'./EigenFaces/{file}').convert('L')
    
    X = np.asarray(img).flatten()
    X_main.append(X)
X_main = np.array(X_main)
img = compressImg(X_main.T)
# plt.figure()
# plt.imshow(Image.fromarray(img))
# plt.show()
for i in range(img.shape[1]):
    newimgArr = img[:, i].reshape(dims[0], -1)
    newimg = Image.fromarray(newimgArr*255)
    newimg.save(f'img{i}.png')