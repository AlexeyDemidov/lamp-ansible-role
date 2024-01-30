#!/bin/bash

# MONIT_HOST
# MONIT_SERVICE
# MONIT_DESCRIPTION
# MONIT_EVENT
# MONIT_DATE
# MONIT_ACTION

/usr/local/bin/lamp createAlert --message "$MONIT_SERVICE $MONIT_EVENT on $MONIT_HOST" --config /etc/lamp.conf --source "$MONIT_HOST" --description "$MONIT_DESCRIPTION" --priority P2
