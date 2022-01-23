#import environ
from os import environ

with open(environ['GITHUB_ENV'], 'a') as f:
  subcomment = "some subcomment test test test"
  f.write('GITHUB_COMMENT<<EOF')
  f.write(subcomment)
  f.write('EOF')