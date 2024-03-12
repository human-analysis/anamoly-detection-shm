#Copyright (c) 2012, Carnegie Mellon University.
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions
#are met:
#1. Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#2. Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#3. Neither the name of the University nor the names of its contributors
#   may be used to endorse or promote products derived from this software
#   without specific prior written permission.

from numpy import *

import matplotlib.mlab as mlab

if not hasattr(mlab, "PCA"):
    import mlab

class PCACenterFix(mlab.PCA):
    '''
    Work around divide by zero error in matplotlib PCA
    '''
    def __init__(self, a):
        mlab.PCA.__init__(self, a)

    def center(self, x):
        for dx in xrange(len(self.sigma)):
            if self.sigma[dx] == 0:
                self.sigma[dx] = 1
        return (x - self.mu) / self.sigma

class PCA:
    #@param thresh the threshold for dropping principal components
    def __init__(self, thresh):
        self.thresh = thresh
        self.fixk = False

    def getreclog(self):
        if None == self.reclog:
            print ("Reconstruction log not saved.")
        return self.reclog

    def gethvlog(self):
        if None == self.ylog:
            print( "Hidden variable log not saved.")
        return self.ylog

    def getmlog(self):
        if None == self.mlog:
            print( "Number of hidden variables log not saved")
        return self.mlog

    def getcenter(self):
        return (self.center_sigma, self.center_mu)
    
    def setfixk(self, k):
        self.fixk = k

    def run(self, data, save):
        print( "Running PCA ...")
        p = PCACenterFix(data)

        if self.fixk != False:
            npcs = self.fixk
        else:
            npcs = sum(p.fracs>self.thresh)

        self.W = p.Wt[0:npcs,:]
        self.center_sigma = p.sigma
        self.center_mu = p.mu

        if save:
            self.ylog = p.Y
            self.reclog = dot(p.Y[:,0:npcs], p.Wt[0:npcs,:]) * p.sigma + p.mu
            self.mlog = ones((data.shape[0]))*npcs
