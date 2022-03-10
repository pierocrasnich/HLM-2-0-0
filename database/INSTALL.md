README

Before to install DataBase for the first time, must check that:

   - all /data/db folder are empty
   - all /data/log/db.log file are empty


first installation:

   1) start database with /cfg/start_DB.sh script

        $ sh /cfg/start_DB.sh

   2) enter in mongoDB console

         $ mongo

   3) configure replica set

         $ rs.initiate()

   4) add replica set member in mongoDB configuration  

         $ rs.add( { host: "XXX.XXX.XXX.XXX:27018" } )

Repeat step (4) for each replica DataBase

After first installation START and STOP DataBase with command.

Command:

    Start database: sh /cfg/start_DB.sh
    Stop database: sh /cfg/stop_DB.sh

DB Backup:

      $ mongodump --host="rs0/127.0.0.1:27017,127.0.0.1:27018" 

DB Restore:

      $ mongorestore --host="rs0/127.0.0.1:27017,127.0.0.1:27018" dump/

