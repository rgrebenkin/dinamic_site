#!/bin/bash

#mysql -uroot -e "create user admin identified by 'admin'"
mysql -uroot -e "create database test"
mysql -uroot -e "grant all on test.* to root"