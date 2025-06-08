from database.DB_connect import DBConnect
from model.order import Order
from model.store import Store


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getStores():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from stores
                """
        cursor.execute(query)

        for row in cursor:
            result.append(Store(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodes(store):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from orders
                    where store_id = %s 
                    """

        cursor.execute(query, (store,))

        for row in cursor:
            result.append(Order(**row))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getEdges(store_id,K):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """select o1.order_id as id1, o2.order_id as id2, count(oi1.quantity + oi2.quantity) as quantity
                    from orders o1, orders o2, order_items oi1, order_items oi2 
                    where o1.order_id = oi1.order_id 
                        and o1.order_date > o2.order_date
                        and o2.order_id = oi2.order_id 
                        and o1.store_id = o2.store_id
                        and o1.store_id = %s
                        and DATEDIFF(o1.order_date, o2.order_date) < %s
                    group by o1.order_id, o2.order_id
                    """
        cursor.execute(query,(store_id, K))

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result