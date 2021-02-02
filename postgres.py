import psycopg2
from config import config
import json
import os


def connect(list_value, authors):
    author1 = [(x,) for x in authors]

    sql_value = """INSERT INTO items (contentType,title,url_page,url_pdf,url_doi,publicationName,doi,publicationDate,abstract) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
    sql_author = """INSERT INTO authors (author_name) VALUES(%s);"""
    conn = None
    try:
        params = config()

        print('Connecting to the PostgreSQL database...')

        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute(sql_value,(*list_value,))
        cur.executemany(sql_author,author1)
        print('done')


        conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def get_items():
    catgory = ['contentType', 'title', 'url', 'creators',
               'publicationName', 'doi', 'publicationDate', 'abstract']
    directory = 'F:\SQL_project\Data Mining and Knowledge Discovery'
    for page in os.listdir(directory):
        if page.endswith(".json"):
            with open(page, 'r') as json_data:
                record_list = json.load(json_data)
                first_record = record_list["records"]
                json_data.close()

            for i, record_dict in enumerate(first_record):
                list_value = []
                authors = []
                for j in catgory:
                    a = record_dict[j]
                    if type(a) == list:
                        for i in a:
                            try:
                                if i.get('value'):
                                    url_value = i.get('value')
                                    list_value.append(url_value)
                                elif i.get('creator'):
                                    author_value = i.get('creator')
                                    authors.append(author_value)
                            except:
                                pass
                    else:
                        list_value.append(a)

                connect(list_value, authors)
            else:
                continue
    

if __name__ == '__main__':
    get_items()


