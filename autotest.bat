del report.xml
newman run %1 -e %2 -d data.csv -r junit --reporter-junit-export report.xml
