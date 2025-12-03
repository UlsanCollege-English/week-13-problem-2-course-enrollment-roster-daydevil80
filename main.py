def build_roster(registrations):
    """
    Given a list of (student_id, course_id) pairs, build a course roster.

    The result should be a dictionary where:
      - each key is a course id (string)
      - each value is a sorted list of unique student ids (strings)
        enrolled in that course

    Duplicate registrations for the same (student_id, course_id) pair
    should appear only once in the output.
    """

    roster = {}  # course → set of students (use set to prevent duplicates)

    for student, course in registrations:
        if course not in roster:
            roster[course] = set()   # store students temporarily in a set
        roster[course].add(student)  # set prevents duplicates automatically

    # Convert sets → sorted lists for final output
    final_roster = {}
    for course, students in roster.items():
        final_roster[course] = sorted(students)

    return final_roster
