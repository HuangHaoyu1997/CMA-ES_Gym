import string
import ray
@ray.remote
def remote_func(value, strings):
    print(strings)
    return value+1.

ID = remote_func.remote(10.,'hello world')
print(ID)
print(ray.get(ID))