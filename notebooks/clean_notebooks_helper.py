import subprocess
import sys
import json
import glob
import csv

def strip_output_from_cell(cell, SAVE_OUTPUT=False):
    if "outputs" in cell and not SAVE_OUTPUT:
        cell["outputs"] = []
    if "execution_count" in cell:
        cell["execution_count"] = None
    if "metadata" in cell:
        cell["metadata"] = {}
    
    if "outputs" in cell and SAVE_OUTPUT:
        for output in cell["outputs"]:
            if "execution_count" in output:
                output["execution_count"] = None
    

ipynb_files = glob.glob('*.ipynb')

files_in_config = {}
try:
    csv_file_handle = open('clean_config.csv')
    config_loader = csv.DictReader(csv_file_handle)
    for row in config_loader:
        files_in_config[row['notebook']] = row['SAVE_OUTPUT']
    csv_file_handle.close()
except FileNotFoundError:
    pass

for ipynb_file in ipynb_files:
    print('Cleaning file: ', ipynb_file, end='. ')
    
    save_output = ipynb_file in files_in_config and files_in_config[ipynb_file]=='1'
    if save_output:
        print('SAVING OUTPUT', end='')
    print()
    
    with open(ipynb_file, encoding='utf-8') as f:
        ipynb = json.load(f)
    
    ipy_version = int(ipynb["nbformat"])-1 # nbformat is 1 more than actual version.

    if ipy_version == 2:
        for sheet in ipynb["worksheets"]:
            for cell in sheet["cells"]:
                strip_output_from_cell(cell, save_output)
    else:
        for cell in ipynb["cells"]:
            strip_output_from_cell(cell, save_output)
    
    ipynb["metadata"] = {"language_info": {"name":"python", "pygments_lexer": "ipython3"}}
    json.dump(ipynb, open(ipynb_file, 'w', encoding='utf-8'), sort_keys=True, indent=1, separators=(",",": "))

# commit_msg = input('Enter commit message: ')
print('Pulling latest changes')
pull = subprocess.run("git pull", shell=True)
print('Pull code: {}'.format(pull.returncode))
print('Inform Burhanuddin if above code is not 0')
# add_files = subprocess.run("git add .", shell=True)