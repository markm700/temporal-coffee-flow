from datetime import timedelta
from temporalio import workflow
with workflow.unsafe.imports_passed_through():
    from activities import your_activity
    from params import YourParams

"""dacx
To spawn an Activity Execution, use the [`execute_activity()`](https://python.temporal.io/temporalio.workflow.html#execute_activity) operation from within your Workflow Definition.
`execute_activity()` is a shortcut for [`start_activity()`](https://python.temporal.io/temporalio.workflow.html#start_activity) that waits on its result.
To get just the handle to wait and cancel separately, use `start_activity()`.
In most cases, use `execute_activity()` unless advanced task capabilities are needed.
A single argument to the Activity is positional. Multiple arguments are not supported in the type-safe form of `start_activity()` or `execute_activity()` and must be supplied by the `args` keyword argument.

You can customize the Workflow name with a custom name in the decorator argument. For example, `@workflow.defn(name="your-workflow-name")`. If the name parameter is not specified, the Workflow name defaults to the function name.

In the Temporal Python SDK programming model, Workflows are defined as classes.
Specify the `@workflow.defn` decorator on the Workflow class to identify a Workflow.
Use the `@workflow.run` to mark the entry point method to be invoked. This must be set on one asynchronous method defined on the same class as `@workflow.defn`. Run methods have positional parameters.

To return a value of the Workflow, use `return` to return an object.
To return the results of a Workflow Execution, use either `start_workflow()` or `execute_workflow()` asynchronous methods.

Use [`start_activity()`](https://python.temporal.io/temporalio.workflow.html#start_activity) to start an Activity and return its handle, [`ActivityHandle`](https://python.temporal.io/temporalio.workflow.ActivityHandle.html). Use [`execute_activity()`](https://python.temporal.io/temporalio.workflow.html#execute_activity) to return the results.
You must provide either `schedule_to_close_timeout` or `start_to_close_timeout`.
`execute_activity()` is a shortcut for `await start_activity()`. An asynchronous `execute_activity()` helper is provided which takes the same arguments as `start_activity()` and `await`s on the result. `execute_activity()` should be used in most cases unless advanced task capabilities are needed.
dacx"""

@workflow.defn(name="YourWorkflow")
class YourWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            your_activity,
            YourParams("Hello", name),
            start_to_close_timeout=timedelta(seconds=10),
        )