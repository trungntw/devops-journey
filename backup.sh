#!/bin/bash
# Script backup folder week1

SOURCE="$HOME/Projects/devops-journey/week1"
DEST="$HOME/Projects/devops-journey/backup_$(date +\%Y\%m\%d_\%H\%M\%S).tar.gz"

echo "Backing up $SOURCE ..."
tar -czf "$DEST" "$SOURCE"
echo "Done! Saved to: $DEST"
