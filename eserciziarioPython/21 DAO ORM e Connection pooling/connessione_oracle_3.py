"""
Test di connessione al database Oracle 23ai della macchina virtuale Oracle Linux
"""

import getpass

import oracledb

connessione_oracle = oracledb.connect(user = "System",
                                      password = "oracle",
                                      dsn = "localhost:11521/free")





