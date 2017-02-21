<h1>Course: {{ course.course_id }} </h1>
Name: <b>{{ course.name }}</b><br/>

<h2>Register exam</h2>
<form action="/courses/{{course.course_id}}/add_exam" method="POST">
  <select name="student_id">
    %for s in course.students:
      <option value="{{s.student_id}}">{{s.lastname}}, {{s.firstname}}</option>
    %end
  </select>
  Mark: <input type="text" name="mark"/></br>
  <input type="submit" value="Save">
</form>

<a href="/courses/{{course.course_id}}/">Back</a>
