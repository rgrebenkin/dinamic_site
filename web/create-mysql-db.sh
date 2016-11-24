
mysql -uroot -e "create user admin identified by 'admin'"
mysql -uroot -pdeep -e "create database test"
mysql -uroot -pdeep -e "grant all on test.* to  admin"