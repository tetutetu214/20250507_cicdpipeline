import json
from datetime import datetime
import pytz

def lambda_handler(event, context):
    # 東京時間の取得
    tokyo_tz = pytz.timezone('Asia/Tokyo')
    current_time = datetime.now(tokyo_tz).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # メッセージを取得(event パラメータから'message'キーを取得）
    message = event.get('message', 'Default message from Lambda!')
    
    return {
        'statusCode': 200, # HTTP ステータスコード
        'body': json.dumps({
            'greeting': f'Hello from {message}!',
            'event': event, # 受け取ったイベント全体を返す（デバッグ用）
            'requested_at': datetime.now(tokyo_tz).isoformat(), # ISO形式の日時
            'display_time': current_time, # 見やすい形式の日時
            'request_id': context.aws_request_id # Lambdaリクエストの一意なID
        })
    }
