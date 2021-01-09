from dask.distributed import Client, progress, get_worker
import os

client = Client("tcp://172.31.36.145:8786") # Replace scheduler IP here

def run_on_worker(data):
    print("Inside run on worker. Printing environment variables:")
    print(os.environ) # This contains the `BITSTREAM`, `DEVICE_NAME` env variable.
    return 0

num_of_workers = len(client.scheduler_info()["workers"])
print("Number of connected workers = ", num_of_workers)
futures = client.map(run_on_worker, range(num_of_workers))
results = client.gather(futures)
print("Received results from workers:")
print(results)
