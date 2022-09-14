import psycopg2
def connectDatabase(user,password,host,port,database):
                return psycopg2.connect(user=user,
                                     password=password,
                                     host=host,
                                     port=port,
                                     database=database)
    
    
                  