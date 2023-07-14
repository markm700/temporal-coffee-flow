import asyncio
from temporalio.client import Client
from workflows import YourWorkflow

"""dacx
Use the `connect()` method on the Client class to create and connect to a Temporal Client to the Temporal Cluster.

To start a Workflow Execution in Python, use either the [`start_workflow()`](https://python.temporal.io/temporalio.client.Client.html#start_workflow) or [`execute_workflow()`](https://python.temporal.io/temporalio.client.Client.html#execute_workflow) asynchronous methods in the Client.

To set a Workflow Id in Python, specify the `id` argument when executing a Workflow with either [`start_workflow()`](https://python.temporal.io/temporalio.client.Client.html#start_workflow) or [`execute_workflow()`](https://python.temporal.io/temporalio.client.Client.html#execute_workflow) methods.
The `id` argument should be a unique identifier for the Workflow Execution.

To set a Task Queue in Python, specify the `task_queue` argument when executing a Workflow with either [`start_workflow()`](https://python.temporal.io/temporalio.client.Client.html#start_workflow) or [`execute_workflow()`](https://python.temporal.io/temporalio.client.Client.html#execute_workflow) methods.
dacx"""

async def main():
    client = await Client.connect("localhost:7233")
    result = await client.execute_workflow(
        YourWorkflow.run,
        "your name",
        id="your-workflow-id",
        task_queue="your-task-queue",
    )
    print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())