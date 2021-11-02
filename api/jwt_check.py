from jwcrypto import jwt,jwk
import json
import jwt as jt
import requests
token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJKd3JvaVJjS1laWE01M3V5cmhoSE9VSWFyamgwdFhlQXNETGJSc0lsMjNJIn0.eyJleHAiOjE2MzU4MzEwMTgsImlhdCI6MTYzNTgzMDcxOCwiYXV0aF90aW1lIjoxNjM1ODI4NjQ3LCJqdGkiOiI2NWNjMGU0Yi1iMzM4LTQ4NzAtYWNkNC1jNDA5OWE2YjMzMzciLCJpc3MiOiJodHRwOi8vMTAuNS41LjM6ODA4MC9hdXRoL3JlYWxtcy9XZWJBcHAiLCJhdWQiOlsicmVzb3VyY2UiLCJhY2NvdW50Il0sInN1YiI6ImFjZTEzYzJhLWI0YTctNGIxMi1iMzhkLWM0N2QwMGFlYWNmMiIsInR5cCI6IkJlYXJlciIsImF6cCI6InJlc291cmNlIiwibm9uY2UiOiI2OTc1ODdkNS1jMzg3LTQ3MjQtOTNmMC1iZGQzMTNkZjg2NzUiLCJzZXNzaW9uX3N0YXRlIjoiZmYzZDdiNmYtYWYxNS00NjE3LWI3MjktMzc2MjY5Yjk0ZWFiIiwiYWNyIjoiMCIsImFsbG93ZWQtb3JpZ2lucyI6WyJodHRwOi8vMTAuNS41LjI6MzAzMCJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJkZWZhdWx0LXJvbGVzLXdlYmFwcCIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsicmVzb3VyY2UiOnsicm9sZXMiOlsiYWNjZXNzX21hcmtzIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwic2lkIjoiZmYzZDdiNmYtYWYxNS00NjE3LWI3MjktMzc2MjY5Yjk0ZWFiIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzdHVkZW50In0.lznuYBe-g6DTr4X7BPwgiVTJl-zLTG29jPNjY6t7kFRu_PGb0tzxMyFdztWsAsiU6i_MNERSB9fZOS37G7ZoM9CNoTE1fUZXjYdmRyB1JLJEj_6CibRSsDdyuxi7-DKJq9fZ0jgE15Ygn4cfHV9WaP187CLCvGfY1xx2XEmqUtSvoWgo3ZVE1e5OdRcJqLihSnZoDnUbDAKV3niFDQK5dizIO-YtcKl7LBAxW2WLgRfCVKwYrCoTsoPTyPHdc5aHEjfnV3TFytjwBWH74mo_tHDzohPZteflY0_hBYeLQfoKBlBt04FYofQiXzBA0lZDRLdJtjMQLBk7cEiAuJsnjg"

def check_jwt(token):
	cert_str = requests.get("http://10.5.5.3:8080/auth/realms/WebApp/protocol/openid-connect/certs").content
	cert_arr = json.loads(cert_str)
	kid = jt.get_unverified_header(token)['kid']
	jwk_string = {}
	for cert in cert_arr['keys']:
		if(cert['kid'] == kid):
			jwk_string = cert
			break	
	key = jwt.JWK(**jwk_string)
	try:
		ans = jt.decode(token,key.export_to_pem(),algorithms=["RS256"],options={"verify_signature":True}, audience = ["resource"])
		if "access_marks" in ans['resource_access']['resource']['roles']:
			return(ans['preferred_username'])
		else:
			return("No")
	except Exception as e:
		ans = "Token Invalid"
		return("No "+ str(e))
