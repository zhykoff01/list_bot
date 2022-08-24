import psycopg2

from db.config import config
from parser.adsresult import AdsResult


class SqlRepository:
    conn = None

    def __init__(self) -> None:
        try:
            params = config()
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**params)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def print_version(self):
        cur = self.conn.cursor()
        try:
            cur.execute('SELECT version()')
            db_version = cur.fetchone()
            print(db_version)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def is_user_exist(self, user_id):
        cur = self.conn.cursor()
        try:
            cur.execute('''SELECT * FROM users WHERE user_id = %s''', [int(user_id)])
            some_response = cur.fetchone()
            return len(some_response) > 0
        except (Exception, psycopg2.DatabaseError) as error:
            return error
        finally:
            cur.close()

    def save_user(self, user_id, username):
        cur = self.conn.cursor()
        try:
            cur.execute('''INSERT INTO users (user_id, username) values (%s,%s)''', [int(user_id), str(username)])
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.conn.rollback()
        finally:
            cur.close()

    def is_ads_exist(self, ads: AdsResult):
        cur = self.conn.cursor()
        try:
            cur.execute('''SELECT * FROM ads WHERE ads_id = %s''', [str(ads.ads_id)])
            some_response = cur.fetchone()
            return len(some_response) > 0
        except (Exception, psycopg2.DatabaseError) as error:
            return error
        finally:
            cur.close()

    def save_ads(self, ads: AdsResult):
        # bitch! save ads
        # if not self.is_ads_exist(ads):
            cur = self.conn.cursor()
            try:
                cur.execute('''INSERT INTO ads (ads_id, href, title, cost, about, category) values (%s, %s, %s, %s, %s, 
                %s)''', [str(ads.ads_id), str(ads.href), str(ads.title), str(ads.cost), str(ads.about), str(ads.category)])
                self.conn.commit()
                print("Inserting", str(ads.ads_id), str(ads.href), str(ads.title), str(ads.cost), str(ads.about), str(ads.category),
                      sep=" ")
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                self.conn.rollback()
            finally:
                cur.close()
        # else:
        #     print("Skipping ", ads.ads_id)
