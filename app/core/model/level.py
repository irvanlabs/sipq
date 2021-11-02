from pydantic import BaseModel
from fastapi import HTTPException, status
from enum import Enum
from pymysql.connections import Connection
from pymysql.err import IntegrityError
from app.core import config


class Level(int, Enum):
    administrator: int = 1
    admin_pusat: int = 2
    admin_provinsi: int = 3
    admin_kabupaten: int = 4
    caleg: int = 5
    saksi: int = 6
    anggota: int = 7

class Result(BaseModel):
    user_id: int
    user_id_target: int
    target_level: int

class UpgradeLevel(BaseModel):
    user_id: int
    user_id_target: int
    target_level: int
    mode: str = 'upgrade'

async def update_level(user_id: int, user_id_target: int, target_level: Level, mode = None) -> Result:
    conn = Connection(
        user=config.DB_USER,
        password=config.DB_PASS,
        database=config.DB_NAME,
        host=config.DB_HOST,
    )

    
    if mode == 'upgrade':
        update_query = '''
        UPDATE `data_diri` 
        SET level = %s 
        WHERE id = %s
        '''
    elif mode == 'downgrade':
        update_query = '''
        UPDATE `data_diri`
        SET level = %s 
        WHERE id = %s
        '''
    else:
        raise HTTPException(status_code=406, detail="mode is not acceptable")
        return mode
        
    with conn:
            
        with conn.cursor() as cursor:
            checkQuery = '''
            SELECT * FROM `data_diri` WHERE id = %s
            '''
            cursor.execute(query=checkQuery, args=user_id)
            result = cursor.fetchone()
            if result[13] > target_level:
                raise HTTPException(status_code=403, detail="Anda tidak memiliki hak akses")
            

        with conn.cursor() as cursor:
            
            cursor.execute(update_query, (target_level, user_id_target))
            conn.commit()

            return {
                'user_id':user_id,
                'user_id_target':user_id_target,
                'level':target_level,
                'status_code': status.HTTP_200_OK,
            }


