import numpy as np
from model import point,element

a=point(1,-1,0)
b=point(2,0,-1)
c=point(3,0,0)

ans=element(1,a,b,c)
print(ans.matrix_K())