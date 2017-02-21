<h1>Course: {{ course.course_id }} </h1>
Name: <b>{{ course.name }}</b><br/>

<h2>Students</h2>
<form action="/courses/{{course.course_id}}/add_student" method="POST">
  %for s in students:
      <input type="checkbox" name="student" value="{{s.student_id}}"
      % if s in course.students:
        checked
      % end
      >
      {{s.lastname}}, {{s.firstname}}</br>
  %end
  <input type="submit" value="Save">
</form>

<a href="/courses/{{course.course_id}}/">Back</a>
