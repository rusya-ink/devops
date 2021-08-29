## Best practices of python web app writing

- Code should work as expected
    - Solution should be testable
    - Solution should be tested to follow requirements
- Solution should be easily extendable
- Code should be readable and understandable
- Solution should be effective enough for the requirements
- Code should follow framework standards

## Why my solution follows these practices

- Solution works as expected (it is tested to show Moscow time and time refreshes after page refresh)
- Code is readable (variables are named meaningfully and comments are present, code is styled)
- Solution is extendable (specific values are stored in variables, page is stored as template)
- Solution is effective enough as it shows time without any processing
- Code follow flask standards

## Unit testing

- Function of making shift in time according to utc was tested with unit tests
- Unit test was completed with best practices (tests are automated, all paths were tested, values from different boundaries were used)
