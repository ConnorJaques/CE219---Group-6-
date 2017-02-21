<form action="/students/{{student.student_id}}/edit" method="POST">
  First name: <input type="text" name="firstname" value="{{ student.firstname }}"/>
  Last name: <input type="text" name="lastname" value="{{ student.lastname }}"/>
  <input type="submit" value="Save">
</form>
