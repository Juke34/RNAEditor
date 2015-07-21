'''
Created on 05.06.2014

@author: david
'''

from VariantSet import VariantSet
from dbCluster import dbCluster
import numpy as np
from sklearn import metrics
from numpy.ma.core import mean, std

from Helper import Parameters

import os
import gc
import psutil
from time import sleep

#proc = psutil.Process(os.getpid())
gc.collect()
#mem0 = proc.get_memory_info().rss
sleep(9)
# create approx. 10**7 int objects and pointers
print "using memory"
foo = ['abc' for x in range(10**8)]
#mem1 = proc.get_memory_info().rss
sleep(5)
# unreference, including x == 9999999
del foo, x
#mem2 = proc.get_memory_info().rss

# collect() calls PyInt_ClearFreeList()
# or use ctypes: pythonapi.PyInt_ClearFreeList()
print "free memory"
gc.collect()
#mem3 = proc.get_memory_info().rss

#pd = lambda x2, x1: 100.0 * (x2 - x1) / mem0
print "freed and sleep"
sleep(9)
#print "Allocation: %0.2f%%" % pd(mem1, mem0)
#print "Unreference: %0.2f%%" % pd(mem2, mem1)
#print "Collect: %0.2f%%" % pd(mem3, mem2)
#print "Overall: %0.2f%%" % pd(mem3, mem0)
 
"""
variants= VariantSet("/media/Storage/bio-data/David/Kostas/scrambleN/scrambleN_1.vcf")
Yclust = dbCluster()

varPosList = []


for v in variants:
    varPosList.append(v.position)
varPosList = np.asarray(varPosList)

for eps in range(211,211):
    for min_samples in range(3,50):
        #print('EPS: %s, minSamples: %s' % (eps,min_samples))
        Yclust.dbscan(varPosList, eps=eps, min_samples=min_samples)
        core_sample_indices, labels = Yclust.coreSamples, Yclust.labels
        
        # Number of clusters in labels, ignoring noise if present.w
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        labelNames = set(labels)
        X = []
        for el in varPosList:
            X.append([el,0])
        X = np.array(X)

        if n_clusters_ > 0:
            print('EPS: %s, minSamples: %s, #Clusters: %d, SC: %0.3f' % (eps, min_samples, n_clusters_, metrics.silhouette_score(X, labels)))
            #print('#Clusters: %d, SC: %0.3f' % (n_clusters_,metrics.silhouette_score(X, labels)))
        else:
            continue
            #print('EPS: %s, minSamples: %s, #Clusters: %d, SC: %0.3f' % (eps, min_samples, n_clusters_, 0))
            
        #print('Estimated number of clusters: %d' % n_clusters_)
        #print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))
        #print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))

Yclust.dbscan(varPosList, eps=2, min_samples=5)

print "%d number of variants" % len(varPosList)

core_sample_indices, labels = Yclust.coreSamples, Yclust.labels
# Number of clusters in labels, ignoring noise if present.w
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

labelNames = set(labels)
#labels = list(labels)


for label in labelNames:
    if label !=-1:
        #get indices of poinst which belong to the current dbCluster
        labelIndices = np.where(labels == label)[0]
        clusterPoints = varPosList[labelIndices]
        #print "%d" % label
        #print "%s" % ",".join(map(str,clusterPoints))
        mini=min(clusterPoints)
        maxi= max(clusterPoints)
        mean= std(clusterPoints)
        dens= float(len(clusterPoints))/ float((maxi-mini))
        print "dbCluster %d: [%s] ,min: %d, max: %d, mean: %d, Density: %f" % (int(label),",".join(map(str,clusterPoints)),mini, maxi, mean,dens)

X = []
for el in varPosList:
    X.append([el,0])
X = np.array(X)


print('Estimated number of clusters: %d' % n_clusters_)
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))


"""
