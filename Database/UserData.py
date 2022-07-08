import pymongo
client = pymongo.MongoClient("mongodb+srv://Raja:Shravanib30@serverlessinstance0.5atee.mongodb.net/?retryWrites=true&w=majority")
db = client["UserRegistrations"]
col = db["UserDatabase"]
def CreateUser(name,contact,email,password,avatar):
    courses = ["Animations","Artificial Intelligence"]
    user_data = {"Name":name,"Contact":contact,"Email":email,"Password":password,"Approval":"Pending", "Courses":courses,"Avatar":avatar,"AnimationXp":0,"AnimationR":1,"AIXP":0,"AIR":1,"Appreciation":[""]}
    user_check = col.find_one({"Email":email})
    if user_check ==None:
        col.insert_one(user_data)
        return "success"
    else:
        return "failure"
def UserLogin(email,password):
    user_pass = col.find_one({"Email":email})
    if password == user_pass["Password"] and user_pass["Approval"]=="Approved":
        Data_user = col.find_one({"Email":email,"Password":password})
        return [Data_user,"success"]
    elif password == user_pass["Password"] and user_pass["Approval"]=="Pending":
        return [0,"Pending"]
    else:
        return [0,"failure"]

