<h1>List of Students</h1>
<ul>
%for s in students:
    <li><a href="/students/{{ s.student_id }}/">{{ s.firstname }} {{s.lastname}}</a>
%end
</ul>
