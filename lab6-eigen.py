from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def compressImg(img):
    X = np.asarray(img)
    X_centered = X - X.mean(axis=0)
    m = X.shape[0]
    X_cov = np.dot(X_centered.T, X_centered) / (m - 1)
    eigenvalues, eigenvectors = np.linalg.eig(X_cov)
    eigenvalues = np.real(eigenvalues)
    eigenvectors = np.real(eigenvectors)
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:,idx]
    plotv = []
    s = 0
    percent = 0
    k = 0
    for i in eigenvalues:
        k+=1
        percent += i/sum(eigenvalues)
        if(percent > .9):
            break
    ev = np.array(eigenvectors[:, :k], ndmin=2)

    X_pca = np.dot(X_centered, ev)
    pcaT = np.array(X_pca, ndmin=2)
    evT = np.array(eigenvectors[:, :k], ndmin=2).T
    X_reconstructed = np.dot(pcaT, evT) + X.mean(axis=0)
    X_reconstructed = X_reconstructed.astype(int)
    imgRec = Image.fromarray(X_reconstructed)
    return imgRec

img = Image.open('./EigenFaces/Aaron_Eckhart_0001.jpg').convert('L')
q = compressImg(img)
plt.figure(1)
plt.imshow(q)
plt.show()