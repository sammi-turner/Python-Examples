from kvpt import *

def check_table() -> None:
    if db_exists("kv"):
        print("\nTable already exists.")
    else:
        create_key_value_table("kv")
        insert_key_value_pair("kv", "John", "Plumber")
        insert_key_value_pair("kv", "Bill", "Firefighter")
        insert_key_value_pair("kv", "Susan", "Engineer")

def query_table() -> None:
    v0 = select_all_pairs("kv")
    v1 = select_all_keys("kv")
    v2 = select_all_values("kv")

    delete_key_value_pair("kv", "Bill")
    v3 = table_contains_key("kv", "Bill")

    v4 = select_all_keys("kv")
    v5 = select_all_values("kv")

    v6 = select_row_from_key("kv", "John")
    v7 = select_value_from_key("kv", "Susan")

    print(f"\n{v0}\n\n{v1}\n\n{v2}\n\n{v3}\n\n{v4}\n\n{v5}\n\n{v6}\n\n{v7}\n")

def main() -> None:
    if is_sqlite_installed():
        check_table()
        query_table()
    else:
        print("Sqlite3 is not installed.")

if __name__ == "__main__":
    main()
