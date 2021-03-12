import mysql.connector
def Connect_To_MySQLDB():
    try:
        db = mysql.connector.connect(
        host = "localhost",
        user = "raghu",
        passwd = "raghu",
        )
        mycursor = db.cursor()
    except:
        print("MySQL Connection Missing !, Session Closed")
        exit(1)

    try:
        Create_DB_And_Tables = 0
        dbase = mysql.connector.connect(
        host = "localhost",
        user = "raghu",
        passwd = "raghu",
        database = "companysample",
        )
        mycursor = dbase.cursor()
    except:
        print ("Missing Database!")
        Create_DB_And_Tables = 1
        print("Trying to create Database and Tables")

    if Create_DB_And_Tables == 1:
        try:
            mycursor.execute("CREATE DATABASE Company")
            db.close()

            dbase = mysql.connector.connect(
            host = "localhost",
            user = "raghu",
            passwd = "raghu",
            database = "Company",
            )
            mycursor = dbase.cursor()
            """
            #Enter code to create all necessary tables in the database
            mycursor.execute("
                CREATE TABLE `company`.`employee` (
                `EmployeeID` INT NOT NULL AUTO_INCREMENT,
                `FirstName` VARCHAR(45) NOT NULL,
                `LastName` VARCHAR(45) NULL,
                `Age` INT NOT NULL,
                PRIMARY KEY (`EmployeeID`))
                COMMENT = 'Employee Information';
                ")

            mycursor.execute("
                CREATE TABLE `company`.`headerinfo` (
                `DocumentNum` INT NOT NULL AUTO_INCREMENT,
                `DocumentDate` DATETIME NOT NULL,
                `EmployeeID` INT NOT NULL,
                `Remarks` VARCHAR(45) NULL,
                PRIMARY KEY (`DocumentNum`))
                COMMENT = 'Header Information';
                ")

            mycursor.execute("
                CREATE TABLE `company`.`detailinfo` (
                `HeaderID` INT NOT NULL,
                `DetailID` INT NOT NULL,
                `Item` VARCHAR(45) NOT NULL,
                `Quantity` FLOAT NOT NULL,
                `Price` FLOAT NOT NULL,
                `Amount` FLOAT NULL,
                `Remarks` VARCHAR(45) NULL,
                PRIMARY KEY (`HeaderID`, `DetailID`))
                COMMENT = 'Detail Information';
            ")
            """
        except:
            print ("Unable to Create Database and/or Tables!, Session Closed")
            Create_DB_And_Tables = 1
            print("Trying to create Database and Tables")
            exit(1)

        print ("Successfully Created Database and Tables")

    return(dbase,mycursor)
