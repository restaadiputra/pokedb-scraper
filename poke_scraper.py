#!/usr/bin/python

import sys, getopt

import image_scrape
import stats_scrape
import message

def main(argv):
   
   try:
      command = argv[0]
      args1 = argv[1]
      args2 = argv[2]

      if command == 'image' or command == 'i':
         image_scrape.scrape(args1, args2)
      elif command == 'stats' or command == 's':
         stats_scrape.scrape(args1, args2)

   except IndexError:
      message.invalid_command()

if __name__ == "__main__":
   main(sys.argv[1:])