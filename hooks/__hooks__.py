from flat_schedule import create_flat_schedule
from guidebook import create_csv_schedule
from schedule_summary import create_summary_schedule

hooks = {
    'site.done': [create_flat_schedule, create_csv_schedule, create_summary_schedule],
}
