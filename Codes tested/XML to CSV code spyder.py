# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 01:08:25 2022

@author: rsuri
"""

#source https://www.youtube.com/watch?v=NVES_jL9bnw&list=PLWwXgGzpu6Ks8ipzznEQa7LchvMXwSYaL&index=2&t=323s

import xml.etree.ElementTree as ET

def xml_to_csv(file_path, csv_name) -> None:
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    with open(csv_name, 'w') as csv_file:
        writer = csv.writer(csv_file)
        headers= (child.tag for child in root[8])
        writer.writerow(headers)
        num_records = len(root)
        
        for record in range(num_records):
            rec = (child.text for child in root[record])
            writer.writerrow(rec)
            
if _name_ = '_main_':
    import sys
    import pathlib
    
    try:
        file_path = sys.argv[1]
        csv_name = sys.argv[2]
        
    except IndexError:
        sys.exit('Tow arguments required. One xml path and one save file name.')
        
    with pathlib.Path(file_path) as xml_file:
         if xml_path.is_file():
             xml_to_csv(file_path, csv_name)
          
         else:
             sys.exit(f'Did not find {file_path}')