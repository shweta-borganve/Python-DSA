import pickle
with open("student.pkl", "rb") as f:
    data = pickle.load(f)
print(data) 