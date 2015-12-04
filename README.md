Open Roberta Lab
================


Getting started with your own deployment of the OpenRoberta programming environment.

### Introduction

After a fresh git clone you get the **robertalab** project folder.
It includes everything you need to setup and extend your own browser programming
environment. License information is available in the **docs** folder.

Things you need on your computer:

* Java 1.7
* Maven
* Git
* Web browser

Please also check our [wiki](http://wiki.open-roberta.org) for a detailed install
instruction, development procedure, coding conventions and further reading. Please
also checkout our project [issue tracker](http://jira.open-roberta.org).

### Fast installation with maven

#### Step 1: Clone the repository and compile

    git clone git://github.com/OpenRoberta/robertalab.git
    cd robertalab/OpenRobertaParent
    mvn clean install

Get a coffee! Might take a couple of minutes.

A successful build looks like:

    [INFO] ---------------------------------------
    [INFO] Reactor Summary:
    [INFO] RobertaParent ..................SUCCESS
    [INFO] OpenRobertaShared ..............SUCCESS
    [INFO] OpenRobertaServer ..............SUCCESS
    [INFO] OpenRobertaRuntime .............SUCCESS
    [INFO] ---------------------------------------
    [INFO] BUILD SUCCESS

#### Step 2a: Starting your own server instance using a unix-like shell (on either lin* or win*).

    cd .. # return to the root folder
    ./ora.sh --start # start the server using default properties

You can also run `./ora.sh --help` for more options.

#### Step 2b: Starting your own server instance without using the shell script

    cd ../OpenRobertaServer # go to the folder of the server resources and the database
    java -cp target/OpenRobertaServer-1.0.0-SNAPSHOT.jar de.fhg.iais.roberta.main.ServerStarter # start


#### Step 3: Accessing your programming environment

Start your browser at: http://localhost:1999


That's it!
