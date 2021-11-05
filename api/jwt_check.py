from jwcrypto import jwt,jwk
import json
import jwt as jt
import requests

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
		if "student" in ans['resource_access']['resource']['roles']:
			return(ans['preferred_username'],"student")
		elif "admin" in ans['resource_access']['resource']['roles']:
			return(ans['preferred_username'],"admin")
		else:
			return("No")
	except Exception as e:
		ans = "Token Invalid"
		return("No "+ str(e))
