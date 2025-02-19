# LIST:

detail = [{"id":1,"name":"rajesh"},{"id":2,"name":"rahul"},{"id":3,"name":"sruthi"}]
value = int(input("Enter a id of a student to display : "))

for x in detail:
    if value==x["id"]:
        print(f"the id :{x['id']} and name : {x['name']}")
        
    
