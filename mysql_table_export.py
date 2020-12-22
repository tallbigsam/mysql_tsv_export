#!/usr/bin/python3

import subprocess
import json
import re

sql_commands = ""
db_name = "sample"
username = "root"
password = "rootroot"
with open("sql_commands.json") as json_file:
    sql_commands = json.load(json_file)
    for command_name in sql_commands["commands"]:
        print("Running command: " + command_name)
        
        sql_statement = "--execute={0}".format(sql_commands["commands"][command_name])
        command = subprocess.run(["/usr/local/mysql/bin/mysql", db_name, "--user={0}".format(username), "--password={0}".format(password), sql_statement], capture_output=True)
        with open(command_name+"_out.tsv", 'w') as command_output_file:
            command_without_trailing_white_space = re.sub(b" +\\t", b'\\t', command.stdout)
            command_output_file.write(command_without_trailing_white_space.decode('ascii'))