import sqlite3
from app import home          #change app to scraper when u make a differemt file for app

def database_run():                            
    cx = sqlite3.connect("price_compare")

    cursor = cx.cursor()
    cursor.execute(
        ''' 
        create table if not exists product_info(
        title1                     VARCHAR(100) PRIMARY KEY, 
        price1                   numeric,  
        rating1                  VARCHAR(10), 
        reviews1                 integer,
        availability1            varchar(30)
        )
        '''

    )
    insert_query='''
        insert into product_info(
        title1,price1,rating1,reviews1) 
        values(title,price,rating,reviews)

        '''
    #cursor.execute(insert_query,(title1,price1,rating1,reviews1))

    cx.commit()
    cx.close()

    print("Database created and variable data stored successfully!")