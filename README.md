# HseStudentsDB

Here some instruments to get data about all HSE students from ruz.hse.ru and use it to fill information(faculties, group, course, etc) about specific group of students.

## How to use

* Install Python3

* Install necessary modules
````bash
pip3 install -r requerements.txt
````

* Open settings.py and write your DB(postgres) settings and path of the table with specific group of students.
* Table should have next columns: "ФИО студента",	"Кампус",	"Факультет", "Программа", "Группа"	"Курс", "Квалификация".
* Find table sample in *data_samples*

1. Get all faculties

  ````bash
  python3 faculties.py
  ````
2. Get all HSE groups.
  ````bash
python3 groups.py
  ````
3. Get all students (and wait... I've waited for about 40~ minutes)
  ````bash
python3 students.py
  ````
4. Then collect data from this DB for your table
  ````bash
python3 all_data_collecting.py
  ````
 
