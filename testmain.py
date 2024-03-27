##test program

import sys
sys.path.append('../..')

import load_vectordb

returned_vdb = load_vectordb.load_vector_db('db/_chat/')

print(returned_vdb._collection.count())