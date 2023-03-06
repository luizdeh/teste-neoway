from checkfile import check_file
from sqlalchemy import create_engine

engine = create_engine("postgresql://admin:admin@db:5432/default_db")

file = check_file()


def send_to_db():
    try:
        file.to_sql("base_teste", engine, index=False)
        print(' ')
        print(' [teste-neoway] -> Success! File sent to database')
    except Exception as e:
        print(' ')
        print(' [teste-neoway] -> ERROR')
        print(' [teste-neoway] ->', e)


send_to_db()
