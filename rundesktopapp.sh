#!/usr/bin/env bash
echo "Script to run the Desktop app and Server"
cd OpenRobertaParent/OpenRobertaDesktopApp
echo "Change Directory to OpenRobertaDesktopApp"
cmd="$1"
shift
case "$cmd" in
                  --createEmptydb)  serverVersionForDb="$1"
                  echo "Create Database"
                  if [[ "$serverVersionForDb" == '' ]]
                  then
                                    lib="../OpenRobertaServer/target/resources"
                                    serverVersionForDb=$(java -cp ./${lib}/\* de.fhg.iais.roberta.main.Administration version-for-db)
                  fi
                  databaseurl="jdbc:hsqldb:file:../OpenRobertaDesktopApp-Documents/db-$serverVersionForDb/openroberta-db"
                  echo -n "do you really want to create the db for version \"$serverVersionForDb\"? If it exists, it will NOT be damaged. 'yes', 'no') "
                  read ANSWER
                  case "$ANSWER" in
                                    yes) : ;;
                                    *)   echo "nothing done"
                                    exit 0 ;;
                  esac
                  cd ../..
                  echo "creating an empty db using the url $databaseurl"
                  main='de.fhg.iais.roberta.main.Administration'
                  java -cp 'OpenRobertaParent/OpenRobertaServer/target/resources/*' "${main}" createemptydb "$databaseurl" ;;

                  --single-user) echo "Single-user"
                  java -cp '../OpenRobertaServer/target/resources/*:target/dependency/*:target/OpenRobertaDesktopApp-2.7.2-SNAPSHOT.jar' de.fhg.iais.DesktopApp '-ddatabase.mode=embedded' '-ddatabase.parentdir=../../../OpenRobertaDesktopApp-Documents' '-dserver.staticresources.dir=../OpenRobertaServer/staticResources' '-dsingleuser=true';;
                  *)
                  java -cp '../OpenRobertaServer/target/resources/*:target/dependency/*:target/OpenRobertaDesktopApp-2.7.2-SNAPSHOT.jar' de.fhg.iais.DesktopApp '-ddatabase.mode=embedded' '-ddatabase.parentdir=../../../OpenRobertaDesktopApp-Documents' '-dserver.staticresources.dir=../OpenRobertaServer/staticResources' ;;
esac
