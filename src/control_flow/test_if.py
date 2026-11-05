"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert 'equal to one' in conclusion
    assert conclusion.startswith('Number bigger')



    # Example 1: Multiple elif branches
    # Determine a student's grade based on their score.
    def get_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

    # Test different score ranges.
    assert get_grade(95) == 'A'
    assert get_grade(85) == 'B'
    assert get_grade(75) == 'C'
    assert get_grade(65) == 'D'
    assert get_grade(50) == 'F'



    # Example 2: Nested if statements
    # Check whether a student is eligible for a scholarship.
    def check_scholarship(score, attendance):
        if score >= 85:
            if attendance >= 90:
                return 'Eligible'
            else:
                return 'Not eligible'
        else:
            return 'Not eligible'

    # Test different eligibility conditions.
    assert check_scholarship(95, 95) == 'Eligible'
    assert check_scholarship(90, 80) == 'Not eligible'
    assert check_scholarship(70, 95) == 'Not eligible'
