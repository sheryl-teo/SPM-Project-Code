import React from 'react';
import {BrowserRouter as Router, Link} from 'react-router-dom';

function CourseList(props) {
    const CourseListItems = props.map(
        (course) => {
            return (
                <li>{course.Course_ID}: <a href = {`/Hr/Courses/${course.Course_ID}`}>{course.Course_Name}</a></li>
            )
        }
    )
    return (
        <div>
            <h2>Course List</h2>
            <ol>
                <div>Courses Available:
                {CourseListItems}

                </div>
            </ol>

            <Link to="/">
            <button>
                Back
            </button>
            </Link>
        </div>
    )
}

export default CourseList;