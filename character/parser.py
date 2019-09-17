#!/usr/bin/env python

import ConfigParser as config_parser
import datetime

class Odometry():
  def __init__(self):
    self.line_list = []
    self.read_file_path = ""
    self.write_file_path = ""
    self.file_postfix = ""

odometry = Odometry()

# parse config
def parse_config():
  cp = config_parser.ConfigParser()
  cp.read('parser.cfg')
  odometry.read_file_path = cp.get('file', 'Read')
  odometry.write_file_path = cp.get('file', 'Write')
  odometry.file_postfix = cp.get('file', 'Postfix')
  print(odometry.read_file_path)
  print(odometry.write_file_path)

# read txt file
def read_file(): 
  f_in = open(odometry.read_file_path + odometry.file_postfix, "r")
  lines = f_in.readlines()
  for line in lines[0:]:
    ch = line.strip('\n').split(' ')
    for c in ch[0:]:
      if len(c) > 0:
        odometry.line_list.append(c[0 : c.index("_")])

  f_in.close()

# write txt file
def write_file(): 
  nowTime = datetime.datetime.now().strftime('-%Y-%m-%d-%H:%M:%S')
  f_out = open(odometry.write_file_path + nowTime + odometry.file_postfix, "w")
  for line in odometry.line_list[0:]:
    f_out.write(line + "\n")
    print("write: " + line)
  f_out.close()

################################################################
# Main function
################################################################
def main():
  parse_config()
  read_file()
  write_file()

if __name__ == "__main__":
  main()