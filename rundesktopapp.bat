@ECHO OFF

SET /P CMD="Select command to run 1: Create Empty Database 2: Single User mode 3: Default Mode and Press Enter"
CALL :CASE_%CMD%

ECHO Done.
EXIT /B

:CASE_1 REM Create a Database
    ECHO Create Empty Database
    SET /P VERSION=Please Enter the Version Number (eg. 2.8.2)
    set databaseurl="jdbc:hsqldb:file:../OpenRobertaDesktopApp-Documents/db-%VERSION%/openroberta-db"
    java -cp "OpenRobertaParent/OpenRobertaServer/target/*" de.fhg.iais.roberta.main.Administration createemptydb "%databaseurl%" OpenRobertaServer-2.8.2-SNAPSHOT-jar-with-dependencies.jar
    GOTO :EOF

:CASE_2 REM Single-User Mode
    ECHO Single-User Mode
    java -cp "OpenRobertaParent/OpenRobertaServer/target/*;OpenRobertaParent/RobotArdu/target/*;OpenRobertaParent/RobotEV3/target/*;OpenRobertaParent/RobotMbed/target/*;OpenRobertaParent/RobotNAO/target/*;OpenRobertaParent/RobotNXT/target/*;OpenRobertaParent/RobotVorwerk/target/*;OpenRobertaParent/RobotWeDo/target/*;target/*;OpenRobertaParent/OpenRobertaDesktopApp/target/*" de.fhg.iais.DesktopApp  "-ddatabase.mode=embedded" "-ddatabase.parentdir=../OpenRobertaDesktopApp-Documents" "-dserver.staticresources.dir=OpenRobertaParent/OpenRobertaServer/staticResources" "-dsingleuser=true" OpenRobertaDesktopApp-2.8.2-SNAPSHOT-jar-with-dependencies.jar
    GOTO END_CASE

:CASE_3 REM Default User Mode
    ECHO Default User Mode
    java -cp "OpenRobertaParent/OpenRobertaServer/target/*;OpenRobertaParent/RobotArdu/target/*;OpenRobertaParent/RobotEV3/target/*;OpenRobertaParent/RobotMbed/target/*;OpenRobertaParent/RobotNAO/target/*;OpenRobertaParent/RobotNXT/target/*;OpenRobertaParent/RobotVorwerk/target/*;OpenRobertaParent/RobotWeDo/target/*;target/*;OpenRobertaParent/OpenRobertaDesktopApp/target/*" de.fhg.iais.DesktopApp  "-ddatabase.mode=embedded" "-ddatabase.parentdir=../OpenRobertaDesktopApp-Documents" "-dserver.staticresources.dir=OpenRobertaParent/OpenRobertaServer/staticResources" OpenRobertaDesktopApp-2.8.2-SNAPSHOT-jar-with-dependencies.jar
    GOTO END_CASE

:CASE_default
  GOTO :EOF
:END_CASE
  GOTO :EOF