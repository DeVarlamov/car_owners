import asyncio
from django.core.management import call_command
from background_task import background


@background(schedule=60 * 60 * 24)  # Запускать каждый день
async def backup_database():
    """Создание резервной копии базы данных"""
    await asyncio.get_event_loop().run_in_executor(
        None, call_command, 'dumpdata', '--output=backup.json')
