#!/bin/bash

check_permission()
{
  file=$1
  mod=$2

  if [ ! -e "$file" ]; then
    echo "[!] $file does not exist"
    return
  fi

  cur_mod=$(stat -c %a "$file")

  if [ "$cur_mod" -le "$mod" ]; then
    echo "[O] $file permission is secure"
  else
    echo "[X] $file permission is unsecure"
    echo "    Current permission : $cur_mod"
    echo "    Secure permission  : $mod"
  fi
  echo ""
}

check_umask()
{
  umask=$(umask)
  if [ $umask -le 0022 ]; then
    echo "[O] umask setting is secure"
  else
    echo "[X] umask setting is unsecure"
    echo "    Current umask : $umask"
    echo "    Secure umask  : 0022"
  fi
}

check_permission "/etc/passwd" "644"
check_permission "/etc/shadow" "400"
check_permission "/etc/group" "644"
check_umask
