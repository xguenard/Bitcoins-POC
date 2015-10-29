import json



json_string = '{"first_name": "Guido" , "Last" : "Red" }'
parsed_json = json.loads( json_string )

print( parsed_json[ 'Last' ] )
