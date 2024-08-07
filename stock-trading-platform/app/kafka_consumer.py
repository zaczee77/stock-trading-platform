from aiokafka import AIOKafkaConsumer
import asyncio

async def consume():
    consumer = AIOKafkaConsumer(
        'stock-price-topic',
        bootstrap_servers='kafka:9092',
        group_id='stock-group'
    )
    await consumer.start()
    try:
        async for msg in consumer:
            print("Consumed message:", msg.value.decode())
    finally:
        await consumer.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(consume())
