<form action="/courses/{{course.course_id}}/edit" method="POST">
  First name: <input type="text" name="name" value="{{ course.name }}"/>
  <input type="submit" value="Save">
</form>
