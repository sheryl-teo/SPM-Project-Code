import {BrowserRouter as Router, Link} from 'react-router-dom';

function CourseAdd(){
 
    return (
        <div>
        <h2>Course Addition</h2>
        <form>
            Course ID: <input type = 'text' name ='Course ID'></input> <br></br> 
            Course Name: <input type = 'text' name ='Course Name'></input><br></br> 
            Skills: Leadership <input type = 'checkbox' name ='Skills'></input>
            Engineering <input type = 'checkbox' name ='Skills'></input><br></br> 
            Roles: Sales Rep<input type = 'checkbox' name ='Roles'></input>
            Repair Engineer <input type = 'checkbox' name ='Roles'></input><br></br> 
            Course Description: <br></br><textarea name ='Course Description'></textarea>
        </form>

            
            <button onClick=''>
                Back
            </button>
            
        </div>
        
    )
        
        
    

}

export default CourseAdd