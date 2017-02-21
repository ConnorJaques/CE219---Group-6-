<h1>Student: {{ student.student_id }}</h1>
first name: <b>{{ student.firstname }}</b><br/>
last name: <b>{{student.lastname}}</b>

<h2>Courses</h2>
<ol>
  %for c in student.courses:
      <li>{{c.name}}</li>
  %end
</ol>

<a href="/">Home</a>
<a href="/students/{{student.student_id}}/edit">Edit</a>
