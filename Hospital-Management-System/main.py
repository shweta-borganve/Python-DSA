import json
import os

if os.path.exists("patients.json"):
    try:
        with open("patients.json", "r") as file:
            patients = json.load(file)
    except json.JSONDecodeError:
        patients = [] 
else:
    patients = [] 

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == "hospital" and password == "hospital123":
        print("Login successful!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False 
        

if login():
    print("\nWelcome to the Hospital Management System!\n")
else:
    print("Access denied. Exiting the system.")
    exit()
 
def add_patient():
    print("-" * 20)
    print("\nAdd Patient Details: \n")
    print("-" * 20)
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    gender = input("Enter Patient Gender: ")
    disease = input("Enter Patient Disease: ")
    doctor = input("Enter Doctor Name: ")
    phone = input("Enter Patient Phone Number: ") 
    address = input("Enter Patient Address: ") 
    date = input("Enter Admission Date (YYYY-MM-DD): ")

    patient = {
        "patient_id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "disease": disease,
        "doctor": doctor,
        "phone": phone,
        "address": address,
        "admission_date": date,
    }
    patients.append(patient)

    with open("patients.json", "w") as file:
        json.dump(patients, file, indent=4)

    print("\nPatient details added successfully!\n") 

def view_patient():
    print("-" * 20)
    print("\nView Patient Details: \n")
    print("-" * 20)
    if len(patients) == 0:
        print("No patient records found.")
    else: 
        for patient in patients:
            print(f"Patient ID: {patient['patient_id']}")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Gender: {patient['gender']}")
            print(f"Disease: {patient['disease']}")
            print(f"Doctor: {patient['doctor']}")
            print(f"Phone: {patient['phone']}")
            print(f"Address: {patient['address']}")
            print(f"Admission Date: {patient['admission_date']}")
            print("-" * 20)

def search_patient():
    print("-" * 20)
    print("\nSearch Patient Details: \n")
    print("-" * 20)
    search_id = input("Enter Patient ID to search: ")
    found = False
    for patient in patients:
        if patient['patient_id'] == search_id:
            print(f"Patient ID: {patient['patient_id']}")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Gender: {patient['gender']}")
            print(f"Disease: {patient['disease']}")
            print(f"Doctor: {patient['doctor']}")   
            print(f"Phone: {patient['phone']}")
            print(f"Address: {patient['address']}")
            print(f"Admission Date: {patient['admission_date']}")
            found = True
            break
    if not found:
        print("Patient not found.")

def update_patient():
    print("-" * 20)
    print("\nUpdate Patient Details: \n")
    print("-" * 20)
    update_id = input("Enter Patient ID to update: ")
    found = False

    for patient in patients:
        if patient['patient_id'] == update_id:
            print(f"Current Name: {patient['name']}")
            patient['name'] = input("Enter new Name (leave blank to keep current): ") or patient['name']
            print(f"Current Age: {patient['age']}")
            age_input = input("Enter new Age (leave blank to keep current): ")

            if age_input:
                patient['age'] = int(age_input)
            print(f"Current Gender: {patient['gender']}") 
            patient['gender'] = input("Enter new Gender (leave blank to keep current): ") or patient['gender']
            print(f"Current Disease: {patient['disease']}")
            patient['disease'] = input("Enter new Disease (leave blank to keep current): ") or patient['disease']
            found = True
            break

    if found:
        with open("patients.json", "w") as file:
            json.dump(patients, file, indent=4)
        print("Patient details updated successfully.")
    else:
        print("Patient not found.") 

def delete_patient():
    print("-" * 20)
    print("\nDelete Patient Record: \n")
    print("-" * 20)
    delete_id = input("Enter Patient ID to delete: ")
    found = False

    for patient in patients:
        if patient['patient_id'] == delete_id:
            patients.remove(patient)
            found = True
            break

    if found:
        with open("patients.json", "w") as file:
            json.dump(patients, file, indent=4)
        print("Patient record deleted successfully.")
    else:
        print("Patient not found.")

def view_doctor_details():
    print("-" * 20)
    print("\nView Doctor Details: \n")
    print("-" * 20)
    doctors = set(patient['doctor'] for patient in patients)
    if len(doctors) == 0:
        print("No doctor records found.")
    else:
        for doctor in doctors:
            print(f"Doctor Name: {doctor}")
            print("-" * 20)

def book_appointment():
    print("-" * 20)
    print("\nBook Appointment: \n")
    print("-" * 20)
    patient_id = input("Enter Patient ID: ")
    appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
    appointment_time = input("Enter Appointment Time (HH:MM): ")

    for patient in patients:
        if patient['patient_id'] == patient_id:
            patient['appointment_date'] = appointment_date
            patient['appointment_time'] = appointment_time
            with open("patients.json", "w") as file:
                json.dump(patients, file, indent=4)
            print("Appointment booked successfully.")
            return

    print("Patient not found.") 

def view_appointment():
    print("-" * 20)
    print("\nView Appointment Details: \n")
    print("-" * 20)
    found = False 
    
    for patient in patients:
        if 'appointment_date' in patient and 'appointment_time' in patient:
            print(f"Patient ID: {patient['patient_id']}")
            print(f"Name: {patient['name']}")
            print(f"Appointment Date: {patient['appointment_date']}")
            print(f"Appointment Time: {patient['appointment_time']}")
            print("-" * 20)
            found = True
            
    if not found:
        print("No appointments found.")  

def discharge_patient():
    print("-" * 20)
    print("\nDischarge Patient: \n")
    print("-" * 20)
    discharge_id = input("Enter Patient ID to discharge: ")
    found = False

    for patient in patients:
        if patient['patient_id'] == discharge_id:
            patients.remove(patient)
            found = True
            break

    if found:
        with open("patients.json", "w") as file:
            json.dump(patients, file, indent=4)
        print("Patient discharged successfully.")
    else:
        print("Patient not found.") 

def patient_count():
    print("-" * 20)
    print("\nTotal Patient Count: \n")
    print("-" * 20)
    count = len(patients)
    print(f"Total number of patients: {count}") 


while True:
    print("*" * 20) 
    print("\nHospital Management System Menu: \n")
    print("*" * 20) 
    print("1. Add Patient")
    print("2. View Patient")    
    print("3. Search Patient")
    print("4. Update Patient Details")
    print("5. Delete Patient Record ")
    print("6. View Doctor Details")
    print("7. Book Appointment")
    print("8. View Appointment")
    print("9. Discharge Patient")
    print("10.Patient Count")
    print("11. Exit\n") 

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please Enter a valid Choice.")
        continue 

    if choice == 1:
        add_patient() 

    elif choice == 2:
        view_patient() 

    elif choice == 3:
        search_patient() 

    elif choice == 4:
        update_patient()

    elif choice == 5:
        delete_patient()

    elif choice == 6:
        view_doctor_details()

    elif choice == 7:
        book_appointment()  

    elif choice == 8:
        view_appointment() 

    elif choice == 9:
        discharge_patient() 

    elif choice == 10:
        patient_count()  

    elif choice == 11:
        print("Exiting....")
        print("\nThank you for using this application\n")
        break 