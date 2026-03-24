# # Horsi pristup
# f = open("hello.txt", "w")
# f.write("Hello world")
# f.close()
#
# f = open("hello.txt", "r")
# result = f.read()
# f.close()
# print(result)
#
# # Lepsi pristup
# with open("hello2.txt", "w") as f:
#     f.write("Hello world")
#
# with open("hello2.txt", "r") as f:
#     result = f.read()
#     print(result)
#
# # Prace s tabulkovyma datama
# import pandas as pd
#
# result = pd.read_csv("customers-100.csv")
#
# print("konec")
#
# d = {"name": ["Ales", "Honza"], "age": [30, 40]}
# new_customers = pd.DataFrame(d)
# new_customers.to_csv("customers-new.csv", index=False)
#
#
# # PRACE S JSONEM
# import json
#
# d = {"name": "Honza", "age": 5}
#
# with open("data.json", "w") as f:
#     json.dump(d, f)
#
# with open("data.json", "r") as f:
#     new_d = json.load(f)
#
# print(new_d)

# JEDNODUCHA PRACE S DB
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///mydb.sqlite', echo=False)

with engine.connect() as conn:
    d = {"name": ["Ales", "Honza", "Pavel"], "age": [30, 40, None]}
    df = pd.DataFrame.from_dict(d)
    df.to_sql(name="Users", con=conn, if_exists="append")

    res = pd.read_sql("select * from Users", conn)

