# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 10:47:52 2021

@author: gomez
"""
import numpy as np

lista = list(range(0,800))
print(lista)

# tiene 9 elementos?

print("Moder foquer") if len(lista) != 9 else print("Perfect")

if(len(lista) != 9):
      raise ValueError("List must contain nine numbers.")

# Convertir en matriz

M = np.array(lista).reshape(3,3)
F = np.array(lista)    
# operacones por fila

# mean
mean_rows = M.mean(axis = 1)
mean_cols = M.mean(axis = 0)
mean_flat = F.mean()

# variance
var_rows = M.var(axis = 1)
var_cols = M.var(axis = 0)
var_flat = F.var()

# standard deviation
std_rows = M.std(axis = 1)
std_cols = M.std(axis = 0)
std_flat = F.std()

# max
max_rows = M.max(axis = 1)
max_cols = M.max(axis = 0)
max_flat = F.max()

# min
min_rows = M.min(axis = 1)
min_cols = M.min(axis = 0)
min_flat = F.min()

# sum
sum_rows = M.sum(axis = 1)
sum_cols = M.sum(axis = 0)
sum_flat = F.sum()

final_dic = {
        'mean': [mean_cols, mean_rows, mean_flat],
        'variance': [var_cols, var_rows, var_flat],
        'standard deviation': [std_cols, std_rows, std_flat],
        'max': [max_cols, max_rows, max_flat],
        'min': [min_cols, min_rows, min_flat],
        'sum': [sum_cols, sum_rows, sum_flat]    
    }

print(final_dic)

final_dic = { # cols, rows, flat
        'mean': [M.mean(axis = 0), M.mean(axis = 1), F.mean()],
        'variance': [M.var(axis = 0), M.var(axis = 1), F.var()],
        'standard deviation': [std_cols, std_rows, std_flat],
        'max': [max_cols, max_rows, max_flat],
        'min': [min_cols, min_rows, min_flat],
        'sum': [sum_cols, sum_rows, sum_flat]    
    }