import torch
a = [1,2,3]
a = torch.tensor(a,dtype=torch.float32)
a = torch.softmax(a,dim=0)
print(a)