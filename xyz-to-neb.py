#Make sure XYZ files have the same order
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-in", "--initial", dest = "initialstructure", default = "initial.xyz", help="Name of Initial Structure")
parser.add_argument("-fin", "--final", dest = "finalstructure", default = "final.xyz", help="Name of Final Structure")
parser.add_argument("-rep", "--replicas", dest = "Num_Replicas", default = "6", help="Enter the number of structures to interpolate")
args = parser.parse_args()

import pandas as pd
df1 = pd.read_csv(args.initialstructure, skiprows=2, names=['Atom', 'X', 'Y', 'Z'], sep="\s+", engine='python')
df2 = pd.read_csv(args.finalstructure, skiprows=2, names=['Atom', 'X', 'Y', 'Z'], sep="\s+", engine='python')
Num_Replicas = int(args.Num_Replicas)
Num_Atoms = len(df1['Atom'])
Atoms = df1['Atom']

X1, Y1, Z1 = (df2['X']-df1['X'])/(Num_Replicas-1), (df2['Y']-df1['Y'])/(Num_Replicas-1), (df2['Z']-df1['Z'])/(Num_Replicas-1)

for i in range(Num_Replicas):
     filename = '%d.xyz' % i
     X, Y, Z = df1['X'] + X1*i, df1['Y'] + Y1*i, df1['Z'] + Z1*i
     with open(filename, "w") as f:
         print(Num_Atoms, file=f)
         print("XYZ file created with xyz-to-neb.py", file=f)
         for j in df1.index:
             print(df1['Atom'].iloc[j], X.iloc[j], Y.iloc[j], Z.iloc[j], file=f)
     f.close()


