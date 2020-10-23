"""
AWS Athena 유틸리티
"""

import time
import json
import traceback
import boto3

class AthenaUtil:
    """
        AWS Athena 및 AWS Credential 연결
    """

    def __init__(self, session_name='default', database='', bucket='', path=''):
        try:
            self.session_name = session_name
            self.session = boto3.Session(profile_name=session_name)
            self.client = self.session.client('athena')
            self.database = database
            self.bucket = bucket
            self.path = path
            if self.path[-1] == '/':
                self.path = self.path[:-1]
            if self.path[0] == '/':
                self.path = self.path[1:]
            self.output_location = f"s3://{bucket}/{path}"
        except Exception:
            print('AWS CREDENTIAL Error')
            print(traceback.format_exc)

    def run_query(self, query, cnt=180):
        """
            Athena Query Run
        """
        result = {}
        athena = self.client
        try:
            response = athena.start_query_execution(
                QueryString=query,
                QueryExecutionContext={
                    'Database': self.database
                },
                ResultConfiguration={
                    'OutputLocation': self.output_location
                }
            )

            query_id = response['QueryExecutionId']
            result['query_id'] = query_id
            retry_cnt = 0

            while True:
                try:
                    response = athena.get_query_execution(
                        QueryExecutionId=query_id
                    )

                    query_status = response['QueryExecution']['Status']['State']
                    #print('query status : ' + query_status)
                    if query_status in ('SUCCEEDED', 'FAILED', 'CANCELLED'):
                        result['query_status'] = query_status
                        res_query_results = athena.get_query_results(QueryExecutionId=query_id, MaxResults=1000)
                        query_result_dict_list = []
                        query_result_list = res_query_results['ResultSet']['Rows']

                        query_result_key_list = []
                        query_result_value_list = []
                        for idx, val in enumerate(query_result_list):
                            if idx == 0:
                                query_result_key_list = val['Data']
                            else:
                                query_result_value_list.append(val['Data'])

                        for value in query_result_value_list:
                            query_result_dict = {}
                            for idx, val in enumerate(query_result_key_list):
                                query_result_dict[val['VarCharValue']] = value[idx]['VarCharValue']
                            query_result_dict_list.append(query_result_dict)
                        result['data'] = query_result_dict_list
                        # print(result)
                        json_result = json.dumps(result, indent=4, ensure_ascii=False)
                        print(json_result)
                    else:
                        retry_cnt += 1
                        time.sleep(3)
                        if retry_cnt == cnt:
                            athena.stop_query_execution(QueryExecutionId=query_id)
                    break
                except Exception as ex:
                    #str(traceback.format_exc())
                    print(ex)
                    break

        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    ATHENAUTIL = AthenaUtil(session_name='[SESSION]', database='[DATABASE]', bucket='[BUCKET]', path='[PATH]')
    ATHENAUTIL.run_query("[QUERY STRING]")
