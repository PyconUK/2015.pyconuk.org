''' __hooks__.py

Attach Python functions to wok hooks.
'''

import flat_schedule

# The `hooks` dictionary that wok will import
# See http://wok.mythmon.com/docs/hooks/
hooks = {
    'site.done': [flat_schedule.write_flat_schedule],
    }
