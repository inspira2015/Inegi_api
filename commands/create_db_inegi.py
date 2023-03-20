from python_mysql import mysql_db

with mysql_db() as db:
    db.execute("CREATE TABLE inegi_data ( id INT AUTO_INCREMENT PRIMARY KEY, MAPA VARCHAR(25), ESTATUS VARCHAR(25), CVE_ENT VARCHAR(25), NOM_ENT VARCHAR(100), NOM_ABR VARCHAR(25), CVE_MUN VARCHAR(50),NOM_MUN VARCHAR(100)," 
                "CVE_LOC VARCHAR(25)," +
                "NOM_LOC VARCHAR(255)," +
                "AMBITO VARCHAR(5)," +
                "LATITUD VARCHAR(255)," +
                "LONGITUD VARCHAR(255)," +
                "LAT_DECIMAL FLOAT(10,8)," +
                "LON_DECIMAL FLOAT(10,8)," +
                "ALTITUD FLOAT(10,2)," +
                "CVE_CARTA VARCHAR(100)," +
                "POB_TOTAL INT(11)," +
                "POB_MASCULINA INT(11)," +
                "POB_FEMENINA INT(11)," +
                "TOTAL_VIV_HAB INT(11))")

