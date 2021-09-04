def run():
    my_dict = {i:i**2 for i in range(1,1001) if i % 2 == 0}
    print(my_dict)
    
    student_id = [1,2,3,4,5,6,7,8,9,10]
    estudiantes = ['juan','jose','farit','mayo','brayan','fatima','nestor','xilena','zaray','samuel']

    #juntnado lo id a los nombre
    estudiantes_id = {uid:studiant for uid, studiant in zip(student_id, estudiantes)}
    print (estudiantes_id)
if __name__ == '__main__':
    run()
