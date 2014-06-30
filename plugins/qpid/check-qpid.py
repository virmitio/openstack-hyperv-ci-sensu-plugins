#!/usr/bin/env python

import sys
from qpid.messaging import *

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3

if len(sys.argv)<2:
  broker =  "localhost:5672" 
else:
  broker = sys.argv[1]

if len(sys.argv)<3: 
  address = "amq.topic" 
else:
  address = sys.argv[2]

connection = Connection(broker)

try:
  connection.open()
  session = connection.session()

  sender = session.sender(address)
  receiver = session.receiver(address)

  sender.send(Message("==qpid connection test message=="));

  message = receiver.fetch()
  print message.content
  session.acknowledge()
  connection.close()
  sys.exit(STATE_OK)

except MessagingError,m:
  print m
  connection.close()
  sys.exit(STATE_CRITICAL)

