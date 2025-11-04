import asyncio


from logging_config import get_logger

logger = get_logger(__name__)

async def quick_background_task():
    print("Background task: Starting and finishing quickly.")
    return "Secret data"

async def main():
    print("Main: Starting.")
    
    # Create the task and keep the reference
    task = await asyncio.create_task(quick_background_task())
    
    # Give the event loop a moment to run the quick task
    await asyncio.sleep(0.1)
    
    # At this point, the task has almost certainly finished.
    # We can check its state.
    print(f"Main: Is background task done? {task}") # Will be True
    
    # We can even peek at the result without awaiting
    print(f"Main: Task's result (peek): {task}")
    
    print("Main: Finishing without awaiting the task.")
    # Since we don't await task, we never formally "receive" its result or handle exceptions.

asyncio.run(main())