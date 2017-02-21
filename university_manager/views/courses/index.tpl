<h1>List of Courses</h1>
<ul>
%for c in courses:
    <li><a href="/courses/{{ c.course_id }}/">{{ c.name }}</a>
%end
</ul>
