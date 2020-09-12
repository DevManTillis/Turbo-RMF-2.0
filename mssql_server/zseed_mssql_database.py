#!/usr/bin/env python3
import pyodbc
from DB_SCHEMA import SCHEMA

def main():
    db_server="tcp:127.0.0.1"
    db_user="sa"
    db_password="P@55w0rd!"
    database="yautomation"
    with open("seed.log", "w") as logfile:
        logfile.write("Log Start\n")
    
    ## Always ensure that you’ve escaped any backslashes in the ODBC string. 
    conn = pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={db_server};PORT:1433;DATABASE={database};UID=sa;PWD={db_password}")
    cursor = conn.cursor()
    
    load_schema(cursor=cursor)

#    list_data(db_connection=conn, cursor=cursor)
#    create_project_seed_data(db_connection=conn, cursor=cursor)
#    create_ansible_config_seed_data(db_connection=conn, cursor=cursor)
#    create_host_seed_data(db_connection=conn, cursor=cursor)
#    create_role_seed_data(db_connection=conn, cursor=cursor)
#    create_playbook_seed_data(db_connection=conn, cursor=cursor)
#    create_command_seed_data(db_connection=conn, cursor=cursor)



def lazylog(message):
    __log = open("seed.log", "a")
    __log.write(str(message) + "\n")


def load_schema(cursor=None):
    try:
        ## Load SCHEMA TSQL statement
        cursor.execute(SCHEMA)
    except Exception as err:
        lazylog(err)


def list_data(db_connection=None, cursor=None):
    tables = ["Project","AnsibleConfiguration","Role","Host","Playbook","Command", "Output"]
    try:
        for table in tables:
            print(table)
            cursor.execute(f"SELECT * FROM {table}")
            for row in cursor.fetchall():
                print (row)
    except Exception as err:
        lazylog(err)

def create_command_seed_data(db_connection=None, cursor=None):
    try:
        seed_data = list()
        with open("seed_data/Command_seed_data.csv", "r") as data:
            seed_data = data.readlines()
        for row in seed_data:
            columns = row.split(',')
            cursor.execute(f"""
            INSERT INTO Command (cmd_id, arguments, project_id)
            VALUES ('{columns[0].strip()}', '{columns[1].strip()}', '{columns[2].strip()}');
            """)
        db_connection.commit()
    except Exception as err:
        lazylog(err)

def create_playbook_seed_data(db_connection=None, cursor=None):
    try:
        seed_data = list()
        with open("seed_data/Playbook_seed_data.csv", "r") as data:
            seed_data = data.readlines()
        for row in seed_data:
            columns = row.split(',')
            cursor.execute(f"""
            INSERT INTO Playbook (playbook_id, playbook_name, playbook_url, project_id)
            VALUES ('{columns[0].strip()}', '{columns[1].strip()}', '{columns[2].strip()}', '{columns[3].strip()}');
            """)
        db_connection.commit()
    except Exception as err:
        lazylog(err)

def create_role_seed_data(db_connection=None, cursor=None):
    try:
        seed_data = list()
        with open("seed_data/Role_seed_data.csv", "r") as data:
            seed_data = data.readlines()
        for row in seed_data:
            columns = row.split(',')
            cursor.execute(f"""
            INSERT INTO Role (role_id, role_name, role_url, project_id)
            VALUES ('{columns[0].strip()}', '{columns[1].strip()}', '{columns[2].strip()}', '{columns[3].strip()}');
            """)
        db_connection.commit()
    except Exception as err:
        lazylog(err)


def create_host_seed_data(db_connection=None, cursor=None):
    try:
        host_seed_data = list()
        with open("seed_data/Host_seed_data.csv", "r") as data:
            host_seed_data = data.readlines()
        for row in host_seed_data:
            columns = row.split(',')
            cursor.execute(f"""
            INSERT INTO Host (host_id, host_name, project_id)
            VALUES ('{columns[0].strip()}', '{columns[1].strip()}', '{columns[2].strip()}');
            """)
        db_connection.commit()
    except Exception as err:
        lazylog(err)

def create_project_seed_data(db_connection=None, cursor=None):
    try:
        projects_seed_data = list()
        with open("seed_data/Project_seed_data.csv", "r") as data:
            projects_seed_data = data.readlines()
        for row in projects_seed_data:
            columns = row.split(',')
            cursor.execute(f"""
            INSERT INTO Project (project_id, name)
            VALUES ('{columns[0].strip()}', '{columns[1].strip()}');
            """)
        db_connection.commit()
    except Exception as err:
        lazylog(err)

def create_ansible_config_seed_data(db_connection=None, cursor=None):
    try:
        ansible_config_seed_data = list()
        with open("seed_data/AnsibleConfiguration_seed_data.csv", "r") as data:
            ansible_config_seed_data = data.readlines()
        for row in ansible_config_seed_data:
            columns = row.split(',')
            cursor.execute(f"""
            INSERT INTO AnsibleConfiguration (config_id, json_config, project_id)
            VALUES ('{columns[0].strip()}', '{columns[1].strip()}', '{columns[2].strip()}');
            """)
        db_connection.commit()
    except Exception as err:
        lazylog(err)

main()





