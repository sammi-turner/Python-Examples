import subprocess
import os

# Double-quote escape character
dq = "\""

# Executes a shell command and returns its output.
def shell(command:str) -> str:
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    exit_code = process.wait()
    if exit_code != 0:
        raise RuntimeError(f"Command execution failed with exit code {exit_code}")
    return output.decode('utf-8').strip()

# Checks if a database exists in the working directory
def db_exists(name:str) -> bool:
    db_name = name + ".db"
    return os.path.exists(db_name)

# Checks if SQLite is installed.
def is_sqlite_installed() -> bool:
    s = shell("sqlite3 --version")
    return s.startswith('3')

# Creates a key-value table in SQLite.
def create_key_value_table(t:str) -> str:
    s = shell(f"echo {dq}CREATE TABLE {t} (key VARCHAR(50) PRIMARY KEY, value TEXT);{dq} | sqlite3 {t}.db")
    return s

# Inserts a key-value pair into the SQLite table.
def insert_key_value_pair(t:str, k:str, v:str) -> str:
    s = shell(f"echo {dq}INSERT INTO {t} (key, value) VALUES ('{k}', '{v}');{dq} | sqlite3 {t}.db")
    return s

# Deletes a key-value pair from the SQLite table.
def delete_key_value_pair(t:str, k:str) -> str:
    s = shell(f"echo {dq}DELETE FROM {t} WHERE key = '{k}';{dq} | sqlite3 {t}.db")
    return s

# Selects all key-value pairs from the SQLite table.
def select_all_pairs(t:str) -> str:
    s = shell(f"echo {dq}SELECT * FROM {t};{dq} | sqlite3 {t}.db")
    return s

# Selects all keys from the SQLite table.
def select_all_keys(t:str) -> str:
    s = shell(f"echo {dq}SELECT key FROM {t};{dq} | sqlite3 {t}.db")
    return s

# Selects all values from the SQLite table.
def select_all_values(t:str) -> str:
    s = shell(f"echo {dq}SELECT value FROM {t};{dq} | sqlite3 {t}.db")
    return s

# Selects a row from the SQLite table based on a key.
def select_row_from_key(t:str, k:str) -> str:
    s = shell(f"echo {dq}SELECT * FROM {t} WHERE key = '{k}';{dq} | sqlite3 {t}.db")
    return s

# Selects a value from the SQLite table based on a key.
def select_value_from_key(t:str, k:str) -> str:
    s = shell(f"echo {dq}SELECT value FROM {t} WHERE key = '{k}';{dq} | sqlite3 {t}.db")
    return s

# Checks if a table contains a specific key.
def table_contains_key(t:str, k:str) -> bool:
    all_keys = select_all_keys(t)
    all_keys_list = all_keys.split('\n')
    return k in all_keys_list
