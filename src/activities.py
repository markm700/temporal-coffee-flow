from temporalio import activity
from params import YourParams

"""dacx
You can develop an Activity Definition by using the `@activity.defn` decorator.
Register the function as an Activity with a custom name through a decorator argument, for example `@activity.defn(name="your_activity")`.

Activity parameters are the function parameters of the function decorated with `@activity.defn`.
These can be any data type Temporal can convert, including dataclasses when properly type-annotated.
Technically this can be multiple parameters, but Temporal strongly encourages a single dataclass parameter containing all input fields.

An Activity Execution can return inputs and other Activity values.
The following example defines an Activity that takes a string as input and returns a string.

You can customize the Activity name with a custom name in the decorator argument. For example, `@activity.defn(name="your-activity")`.
If the name parameter is not specified, the Activity name defaults to the function name.
dacx"""

@activity.defn(name="your_activity")
async def your_activity(input: YourParams) -> str:
    return f"{input.greeting}, {input.name}!"
