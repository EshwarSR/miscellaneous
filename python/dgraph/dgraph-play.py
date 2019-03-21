import pydgraph
import json

server = "10.0.128.111:9080" 
client_stub = pydgraph.DgraphClientStub(server)
client = pydgraph.DgraphClient(client_stub)

email = "eshwar@kenome.io"

# Run query.
query = "query all($a: string){ get_uid(func: eq(email, $a )) { uid } }"
variables = {'$a': email}


res = client.query(query, variables=variables)

# res = client.query(query)

resp_json = json.loads(res.json);

print(resp_json)

if len(resp_json["get_uid"]) == 0:
  print("Entry doesnt exist")
  # Adding it to dgraph
  # https://docs.dgraph.io/mutations/#json-mutation-format
  data = { "name": email.split("@")[0], "email": email}
  txn = client.txn()
  txn.mutate(set_obj=data)
  txn.commit()

else:
  print("Entry exists")
  print("UID is", resp_json["get_uid"][0]["uid"])