import torch

z = torch.tensor([[[1, 2, 3]]]) 
print("shape de z",z.shape)
print("squeeze de z",z.squeeze().shape)

x = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
print("view",x.view(3,3))
print("squeeze",x.squeeze())
print("shape",x.shape)

x = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
y = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
print("x+y", x+y)

x = torch.tensor([[1,2,3],[4,5,6]])
y = torch.tensor([[1,2,3]])
print("x*y", x*y)

x = torch.tensor([[1,2],[4,5]])
y = torch.tensor([[1,2],[4,5]])
print("x*y", x*y)
print("5*x", 5*x)

a = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
b = torch.tensor([1,2,3])
print("a+b", a+b)

x = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
print(x[:,2:])
print(x[-1,0:])
print(x[1:2,-1] + x[0,2:])
print(x[1,-1] * x[0,0:])
