import scipy.io as spio
import os

def read(filename, variable=None):
    mat = spio.loadmat(filename, squeeze_me=True)
    if variable:
        if variable in mat:
            mat = mat[variable]
        else:
            mat = None
    return mat

def write(filename, name, variable, append=True):
    if append and os.path.isfile(filename):
        # unfortunately scipy can not directly append. so we read, append, then write.
        mat = read(filename)
        mat[name] = variable
        spio.savemat(filename, mat)
    else:
        spio.savemat(filename, {name: variable})
