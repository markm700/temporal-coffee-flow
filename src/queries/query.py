import asyncio
from temporalio.client import Client
from query_workflow import GreetingWorkflow

"""dacx
To send a Query to the Workflow, use the [`query`](https://python.temporal.io/temporalio.client.WorkflowHandle.html#query) method from the [`WorkflowHandle`](https://python.temporal.io/temporalio.client.WorkflowHandle.html) class.

To send a Query to a Workflow Execution from Client code, use the `query()` method on the Workflow handle.
dacx"""

async def main():
    client = await Client.connect("localhost:7233")
    handle = await client.start_workflow(
        GreetingWorkflow.run,
        "World",
        id="hello-query-workflow-id",
        task_queue="query-tq",
    )

    result = await handle.query(GreetingWorkflow.greeting)

    print(f"First greeting result: {result}")
    result = await handle.query("Custom Query Name")
    print(f"Custom query result: {result}")

    await asyncio.sleep(3)
    result = await handle.query(GreetingWorkflow.greeting)
    print(f"Second greeting result: {result}")

if __name__ == "__main__":
    asyncio.run(main())