import sys
import getopt
from monitoring.monitoring import Monitoring 

def main():
    #------------------------------ Processing input arguments     
    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:d:e:f:q:", ["command=", "database=", "experiment=", "file=", "query="])
    except getopt.GetoptError as err:
        print (err)
        sys.exit(2)
        
    command = database = experiment = query = fileName = None
    data = ""
    
    for o, a in opts:
        if o in ("-c", "--command"):
            command = a
        elif o in ("-d", "--database"):
            database = a
        elif o in ("-e", "--experiment"):
            experiment = a
        elif o in ("-f", "--file"):
            fileName = a
        elif o in ("-q", "--query"):
            query = a
        else:
            assert False, "unhandled option."
        
    #------------------------------ Generate CSV file
    m = Monitoring()
    if query and (command or database or experiment):
            print("WARN: Parameter query was set, other will be ignored.")
    if not query:
        query = m.getReportQuery(command, database, experiment)
    
    m.copyToCSV(query, fileName)
    
    
if __name__ == "__main__":
	main()
    
