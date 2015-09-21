''' __hooks__.py

Attach Python functions to wok hooks.
'''

import flat_schedule
import guidebook
import schedule_summary

# The `hooks` dictionary that wok will import
# See http://wok.mythmon.com/docs/hooks/
hooks = {
    'site.done': [
            flat_schedule.create_flat_schedule,
            guidebook.create_csv_schedule,
            schedule_summary.create_summary_schedule,
        ],
    }
