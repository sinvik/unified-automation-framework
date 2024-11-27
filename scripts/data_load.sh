#!/bin/bash
# Run DB tests
source /app/.venv/bin/activate
export sql_user=$sql_user
export sql_pwd=$sql_pwd
echo "Database logging as $sql_user"
python3 tests/db/data_load/drop_and_load.py