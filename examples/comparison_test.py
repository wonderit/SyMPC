
import syft as sy

sy.logger.remove()
import torch

from sympc.session import Session
from sympc.session import SessionManager
from sympc.tensor import MPCTensor
from pytictoc import TicToc


# Define the virtual machines that would be use in the computation
alice_vm = sy.VirtualMachine(name="alice")
bob_vm = sy.VirtualMachine(name="bob")
charlie_vm = sy.VirtualMachine(name="charlie")

# Get clients from each VM
alice = alice_vm.get_root_client()
bob = bob_vm.get_root_client()
charlie = charlie_vm.get_root_client()

parties = [alice, bob, charlie]

# Setup the session for the computation
session = Session(parties=parties)
SessionManager.setup_mpc(session)

# Define the private values to shares
# x_secret = torch.Tensor([[0.1, -1], [-4, 4]])
vector_size = 100000
x_secret = torch.randint(-10, 10, (vector_size,))
y_secret = torch.Tensor([[4.0, -2.5], [5, 2]])

print(x_secret)
print(y_secret)

x = x_secret.share(parties=[alice, bob])
y = y_secret.share(parties=[alice, bob])

print(x)
print(y)
t = TicToc()
t.tic()
a = (x > 0)

t.toc()
a.reconstruct()

print(a)
