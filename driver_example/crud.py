import logging

try:
	from driver_example.connector import connection
except Exception as e:
	raise e


def get_all_courses() -> list[tuple]:
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM course;")
	courses = cursor.fetchall()
	return courses


def get_course(course_id: int) -> tuple:
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM course where id=%s;" % course_id)
	course = cursor.fetchone()
	return course


def insert_course(course_name: str, course_duration: int, course_instructor: int) -> bool:
	cursor = connection.cursor()
	try:
		cursor.execute("INSERT INTO course (instructorid, duration, name) VALUES (%s, %s, \'%s\')" % (
			course_instructor, course_duration, course_name))
		connection.commit()

		return True
	except Exception as e:
		logging.error(e)
		return False


def get_all_students() -> list[tuple]:
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM student;")
	students = cursor.fetchall()
	return students


def get_student(student_id: int) -> tuple:
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM student where id=%s;" % student_id)
	student = cursor.fetchone()
	return student


def insert_student(first_name: str, last_name: str) -> bool:
	cursor = connection.cursor()
	try:
		cursor.execute("INSERT INTO student (firstname, lastname) VALUES (\'%s\', \'%s\')" % (
			first_name, last_name))
		connection.commit()

		return True
	except Exception as e:
		logging.error(e)
		return False


def get_all_instructors() -> list[tuple]:
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM instructor;")
	instructors = cursor.fetchall()
	return instructors


def get_instructor(instructor_id: int) -> tuple:
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM instructor where id=%s;" % instructor_id)
	instructor = cursor.fetchone()
	return instructor


def insert_instructor(first_name: str, last_name: str, phone: str) -> bool:
	cursor = connection.cursor()
	try:
		cursor.execute("INSERT INTO instructor (firstname, lastname, phone) VALUES (\'%s\', \'%s\', \'%s\')" % (
			first_name, last_name, phone))
		connection.commit()
		return True
	except Exception as e:
		logging.error(e)
		return False


def get_course_enrollments(course_id: int) -> list[tuple]:
	cursor = connection.cursor()
	cursor.execute(
		"SELECT * FROM student INNER JOIN coursestudentrelation c on student.id = c.student WHERE course=%s;" % course_id)
	enrollments = cursor.fetchall()
	return enrollments


def get_student_enrollments(student_id: int) -> list[tuple]:
	cursor = connection.cursor()
	cursor.execute(
		"SELECT * FROM course INNER JOIN coursestudentrelation c on course.id = c.course WHERE student=%s;" % student_id)
	enrollments = cursor.fetchall()
	return enrollments


def insert_enrollment(course_id: int, student: int) -> bool:
	cursor = connection.cursor()
	try:
		cursor.execute("INSERT INTO coursestudentrelation (course, student) VALUES (%s, %s)" % (
			course_id, student))
		connection.commit()
		return True
	except Exception as e:
		logging.error(e)
		return False
