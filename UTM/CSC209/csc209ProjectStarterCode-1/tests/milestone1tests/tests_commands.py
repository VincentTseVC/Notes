from subprocess import CalledProcessError, STDOUT, check_output, TimeoutExpired, Popen, PIPE 
import os
import shutil
import pty
import datetime
import sys
from time import sleep 
import multiprocessing
from tests_helpers import * 


def _test_1unkown_command(comment_file_path, student_dir, timeout=0.05):
  start_test(comment_file_path, "Unknown command should display corresponding message")
  try:
    p = Popen(['./mysh'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    write(p, "destroy")
    output = read_stderr(p)
    if "ERROR: Unrecognized command: destroy" in output and "input line too long" not in output:
      finish(comment_file_path, "OK")
      return 
    else:
      finish(comment_file_path, "NOT OK")
  except Exception as e:
    finish(comment_file_path, "NOT OK")

def _test_10unkown_commands(comment_file_path, student_dir):
  start_test(comment_file_path, "Multiple unknown commands")
  try:
    process = start("./mysh")
    for i in range(10):
        write(process, "nonexistantcommand" + str(i))
        if "ERROR: Unrecognized command" not in read_stderr(process):
          finish(comment_file_path, "NOT OK")
          return 
    else:
      write(process, "exit")
      finish(comment_file_path, "OK")
      return 
  except Exception as e:
    finish(comment_file_path, "NOT OK")


def _test_long_line(comment_file_path, student_dir, timeout=0.05):
  start_test(comment_file_path, "Long command input is invalid")
  try:
    p = Popen(['./mysh'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    s = "echo " + "o" * 75
    stdout = p.communicate(input=s.encode(), timeout=timeout)[1]
    if "ERROR: input line too long" in stdout.decode() and "Unrecognized command" not in stdout.decode():
        finish(comment_file_path, "OK")
    else:
      finish(comment_file_path, "NOT OK")
  except Exception:
    finish(comment_file_path, "NOT OK")

def _test_long_priority(comment_file_path, student_dir, timeout=0.05):
  start_test(comment_file_path, "Long command message takes priority")
  try:
    p = Popen(['./mysh'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    s = "a" * 100
    stdout = p.communicate(input=s.encode(), timeout=timeout)[1]
    if "ERROR: input line too long" in stdout.decode() and "Unrecognized command" not in stdout.decode():
        finish(comment_file_path, "OK")
    else:
      finish(comment_file_path, "NOT OK")
  except Exception:
    finish(comment_file_path, "NOT OK")



def test_commands_suite(comment_file_path, student_dir):
  start_suite(comment_file_path, "Unknown Command Message")
  start_with_timeout(_test_1unkown_command, comment_file_path)
  start_with_timeout(_test_10unkown_commands, comment_file_path)
  end_suite(comment_file_path)

  start_suite(comment_file_path, "Long Command Message")
  start_with_timeout(_test_long_line, comment_file_path)
  start_with_timeout(_test_long_priority, comment_file_path)
  end_suite(comment_file_path)

