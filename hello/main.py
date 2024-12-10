import asyncio
from hello_activity import main as activity
from hello_activity_choice import main as activity_choice
from hello_child_workflow import main as child_workflow
from hello_workflow import main as workflow


# async def amain():
#     # Don't work. Need more workers?
#     tasks = []

#     tasks.append(asyncio.create_task(activity()))
#     tasks.append(asyncio.create_task(activity_choice()))
#     tasks.append(asyncio.create_task(child_workflow()))
#     tasks.append(asyncio.create_task(workflow()))

#     results = await asyncio.gather(*tasks)

#     print(tasks)
#     print(results)


def smain():
    asyncio.run(activity())
    asyncio.run(activity_choice())
    asyncio.run(child_workflow())
    asyncio.run(workflow())


if __name__ == "__main__":
    smain()
    # asyncio.run(amain())
