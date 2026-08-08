import json
import os

if os.path.exists("students.json"):
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
    except json.JSONDecodeError:
        students = []
else:
    students = []

if os.path.exists("faculty.json"):
    try:
        with open("faculty.json", "r") as f:
            faculty = json.load(f)
    except json.JSONDecodeError:
        faculty = []
else:
    faculty = []

if os.path.exists("courses.json"):
    try:
        with open("courses.json", "r") as f:
            courses = json.load(f)
    except json.JSONDecodeError:
        courses = []
else:
    courses = []

if os.path.exists("enrollment.json"):
    try:
        with open("enrollment.json", "r") as f:
            enrollment = json.load(f)
    except json.JSONDecodeError:
        enrollment = []
else:
    enrollment = []
