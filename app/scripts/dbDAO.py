from sqlalchemy import create_engine
def testDb():
    dbString = 'postgresql://dqztvtptwfxbby:e5a231bd25668c9e261bd51a3a1e90514072ddeabcab0290341e706c9e4aa0b0@ec2-52-5-247-46.compute-1.amazonaws.com:5432/dak6f33ndfqk62'
    try:
        db = create_engine(dbString)
        conn = db.connect()
        conn.close()
        return "Success"
    except:
        return "Failed"

