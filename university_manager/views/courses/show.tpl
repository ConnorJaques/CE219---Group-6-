<h1>Course: {{ course.course_id }} </h1>
Name: <b>{{ course.name }}</b><br/>

<h2>Students</h2>
<ul>
  %for s in course.students:
      <li>{{s.lastname}}, {{s.firstname}}</li>
  %end
</ul>

<h2>Exams</h2>
<ul>
  %for e in course.exams:
      <li>{{e.student.lastname}}, {{e.student.firstname}} - Mark: {{e.mark}} </li>
  %end
</ul>

<a href="/">Home</a>
<a href="/courses/{{course.course_id}}/edit">Edit</a>
<a href="/courses/{{course.course_id}}/add_student">Manage students</a>
<a href="/courses/{{course.course_id}}/add_exam">Register exam</a>
