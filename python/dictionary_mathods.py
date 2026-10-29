#key this is cheack the particolor value
students={
    "name":"pipul kumar",
    "father":"shriram",
   "subject":{
        "phy":97,
        "math":95,
        "location":{
            "village":"harkhpura khas",
            "dist":"azamargh",
        }
    }
}
print(students.keys())
print(students.values())
print(students.items())
print(students.get("subject").get("location").get("village"))
