import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Link } from 'react-router-dom';
import {
    Box,
    Button,
    Flex,
    Input,
    InputGroup,
    Modal,
    ModalBody,
    ModalCloseButton,
    ModalContent,
    ModalFooter,
    ModalHeader,
    ModalOverlay,
    Stack,
    Text,
    useDisclosure
} from "@chakra-ui/react";

// Fetching Course List Data
const CourseListContext = React.createContext({
    CourseList: [], fetchCourseList: () => { }
})

export default function JobList() {
    const [CourseList, setCourseList] = useState([])
    const fetchCourseList = async () => {
        const response = await fetch("http://127.0.0.1:8000/jobroles/")
        const CourseList = await response.json()
        setCourseList(CourseList)
    }
    useEffect(() => {
        fetchCourseList()
    }, [])


    const [JobAssignment, setJobAssignment] = useState([])
    const fetchJobAssignment = async () => {
        const response = await fetch("http://127.0.0.1:8000/job_role_skills")
        const JobAssignment = await response.json()
        setJobAssignment(JobAssignment)
    }
    useEffect(() => {
        fetchJobAssignment()
    }, [])

    const JobAssignmentList={}
    
    JobAssignment.map((JobAssignment)=>{
        if(JobAssignment.Job_Role_ID in JobAssignmentList){
        const skills = JobAssignment.Skill_ID +' '
        JobAssignmentList[JobAssignment.Job_Role_ID].push(skills)

        }

        else{
        const skills = JobAssignment.Skill_ID +' '
        JobAssignmentList[JobAssignment.Job_Role_ID]=[skills]
        }
   
    })

    CourseList.map((Course)=>{
        if(Course.Job_Role_ID in JobAssignmentList){
            Course['Skills']=JobAssignmentList[Course.Job_Role_ID]

        }

        else{
            Course['Skills']='-'
        }

        if(Course.Active==1){
            Course['Status']='Active'
        }
        else{
            Course['Status']='Retired'
        }
   
    })

   
    return (
        
        
        <CourseListContext.Provider value={{ CourseList, fetchCourseList }}>
            
            
            <h1><b><u>Roles Available</u></b></h1>
            <ol>
                <AddCourses/>
                <SoftDelete/>
                <UndoSoftDelete/>
                <UpdateCourses/>
                <AssignSkills/>
                {/* <DeleteAssignSkills/> */}
                {CourseList.map((CourseList) => (
                    
                    <>
                        
                        <li>Role ID: <b>{CourseList.Job_Role_ID}</b> Role Name: <b>{CourseList.Job_Role_Name}</b> Department: <b>{CourseList.Job_Department}</b> Status:<b>{CourseList.Status}</b> Skills Required: {CourseList.Skills}</li><br></br>
                        
                        {/* <TodoHelper Role_Name={CourseList.Job_Role_Name} Department = {CourseList.Job_Department} id={CourseList.Job_Role_ID} fetchCourseList={fetchCourseList} /> <br></br> */}
                    </>
            ))}
            </ol>

        </CourseListContext.Provider>
        
    )
}

// Adding Courses to Course List

function AddCourses() {
    const [item1, setItem1] = React.useState("")
    const [item2, setItem2] = React.useState("")
    const [department, setDepartment] = React.useState("")
    


    const { Courses, fetchCourseList } = React.useContext(CourseListContext)

    const handleInput1 = event => {
        setItem1(event.target.value)
    }

    const handleInput2 = event => {
        setItem2(event.target.value)
    }

    const handleInput3 = (department1) => {
        setDepartment(department1)
    }

    const [JobID, setJobID] = useState([])
    const fetchJobID = async () => {
        const response = await fetch("http://127.0.0.1:8000/jobroles/")
        const JobID = await response.json()
        setJobID(JobID)
    }
    useEffect(() => {
        fetchJobID()
    }, [])

    // if 'errors' in list of keys of response 
    // show popup for each error 

    console.log(JobID)
    const departmentList=[]
    JobID.map((JobID)=>{
        if(!departmentList.includes(JobID.Job_Department)){
            departmentList.push(JobID.Job_Department)
            }
        
        
    })
    console.log(departmentList)

    const handleSubmit = (event) => {
        const newCourses = {
            "Job_Role_ID": item1,
            "Job_Role_Name": item2,
            "Job_Department": department,
            'Active':1
        }

        fetch("http://127.0.0.1:8000/jobroles/create",
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(newCourses)
            }).then(fetchCourseList)
            // .then(response=>console.log(response))
            .catch(errors=>console.log(errors))

    }



    return (
        <>
        <p><b><u>Role Addition</u></b></p>
        <form>
        <label>
            Role ID: <input type="text" name="name" onChange={handleInput1}/>
        </label>
        
        <label>
            Role Name: <input type="text" name="name" onChange={handleInput2}/>
        </label>

        Department:
        <select 
        onChange={(event) => handleInput3(event.target.value)}>
            <option>Select</option>
           {departmentList.map((department)=>
           <option value = {department} >{department}</option>
           )}
        </select>

        

             <button type="submit" value="Submit" onClick={handleSubmit}>Submit</button>


        </form>
        </>
            
    )
}

// // update DB 

function UpdateCourses() {

    const [id, setID] = React.useState("")
    const [name, setName] = React.useState("")
    const [department, setDepartment] = React.useState("")

    const { Courses, fetchCourseList } = React.useContext(CourseListContext)

    const handleInput1 = (id1)=> {
        setID(id1)
        
    }


    const handleInput2 = event => {
        setName(event.target.value)
    }

    const handleInput3 = (department1) => {
        setDepartment(department1)
    }

    

    const handleSubmit = (event) => {
        const newCourses = {
            "Job_Role_ID": id,
            "Job_Role_Name": name,
            "Job_Department": department,
            'Active':1
        }

        fetch("http://127.0.0.1:8000/jobroles/update",
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(newCourses)
            }).then(fetchCourseList)

            .then(response=>console.log(response))
            .catch(error=>console.log(error))

    }

    
    const [JobID, setJobID] = useState([])
    const fetchJobID = async () => {
        const response = await fetch("http://127.0.0.1:8000/jobroles/")
        const JobID = await response.json()
        setJobID(JobID)
    }
    useEffect(() => {
        fetchJobID()
    }, [])

    // if 'errors' in list of keys of response 
    // show popup for each error 

    const IDList=[]
    JobID.map((JobID)=>{
        IDList.push(JobID.Job_Role_ID)
        
    })

    const departmentList=[]
    JobID.map((JobID)=>{
        if(!departmentList.includes(JobID.Job_Department)){
            departmentList.push(JobID.Job_Department)
            }
        
        
    })


 
  


    return (
        <>
        <p><b><u>Role Update</u></b></p>
        <form>
        Role ID:
        <select 
        onChange={(event) => handleInput1(event.target.value)}>
        <option>Select</option>
           {IDList.map((ID)=>
           <option value = {ID} >{ID}</option>
           )}
        </select>
        
        <label>
            Role Name: <input type="text" name="name" id='name' onChange={handleInput2}/>
        </label>

        Department:
        <select 
        onChange={(event) => handleInput3(event.target.value)}>
            <option>Select</option>
           {departmentList.map((department)=>
           <option value = {department} >{department}</option>
           )}
        </select>

             <button type="submit" value="Submit" onClick={handleSubmit}>Update</button>


        </form>
        </>
            
    )
}

// Soft Delete Of Roles

function SoftDelete(){

    const [id, setID] = React.useState("")

    const { Courses, fetchCourseList } = React.useContext(CourseListContext)

    const handleInput1 = (id1)=> {
        setID(id1)
        
    }

    const handleSubmit = (event) => {
        fetch("http://127.0.0.1:8000/jobroles/delete/soft/"+id,
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(id)
        }).then(fetchCourseList)

        .then(response=>console.log(response))
        .catch(error=>alert(error))
    }

    const [JobID, setJobID] = useState([])
    const fetchJobID = async () => {
        const response = await fetch("http://127.0.0.1:8000/jobroles/")
        const JobID = await response.json()
        setJobID(JobID)
    }
    useEffect(() => {
        fetchJobID()
    }, [])

    const IDList=[]
    JobID.map((JobID)=>{
        IDList.push(JobID.Job_Role_ID)
        
    })

    return (
            <>
            <p><b><u>Role Soft Delete</u></b></p>
            <form>
                Role ID: 
                <select 
                onChange={(event) => handleInput1(event.target.value)}>
                <option>Select</option>
                {IDList.map((ID)=>
                <option value = {ID} >{ID}</option>
                )}
                </select>

                <button type="submit" value="Submit" onClick={handleSubmit}>Delete</button>


            </form>
            </>

        )

}

// Undo Soft Delete

function UndoSoftDelete(){

    const [id, setID] = React.useState("")

    const { Courses, fetchCourseList } = React.useContext(CourseListContext)

    const handleInput1 = (id1)=> {
        setID(id1)
        
    }

    const handleSubmit = (event) => {
        fetch("http://127.0.0.1:8000/jobroles/delete/softrestore/"+id,
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(id)
        }).then(fetchCourseList)

        .then(response=>console.log(response))
        .catch(error=>alert(error))
    }

    const [JobID, setJobID] = useState([])
    const fetchJobID = async () => {
        const response = await fetch("http://127.0.0.1:8000/jobroles/")
        const JobID = await response.json()
        setJobID(JobID)
    }
    useEffect(() => {
        fetchJobID()
    }, [])

    const IDList=[]
    JobID.map((JobID)=>{
        IDList.push(JobID.Job_Role_ID)
        
    })
    return (
            <>
            <p><b><u>Role Undo Soft Delete</u></b></p>
            <form>
                Role ID: 
                <select 
                onChange={(event) => handleInput1(event.target.value)}>
                <option>Select</option>
                {IDList.map((ID)=>
                <option value = {ID} >{ID}</option>
                )}
                </select>

                <button type="submit" value="Submit" onClick={handleSubmit}>Undo Delete</button>


            </form>
            </>

        )

}










    

// Assigning Skills To Roles


function AssignSkills() {

    const [id, setID] = React.useState("")
    const [department, setDepartment] = React.useState("")

    const { Courses, fetchCourseList } = React.useContext(CourseListContext)

    const handleInput1 = (id1)=> {
        setID(id1)
        
    }

    const handleInput3 = (department1) => {
        setDepartment(department1)
    }

    
    const handleSubmit = (event) => {
        const newCourses = {
            "Job_Role_ID": id,
            "Skill_ID": department,
            'Active':1
        }

        fetch("http://127.0.0.1:8000/job_role_skills/create",
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(newCourses)
        }).then(fetchCourseList)

        .then(response=>console.log(response))
        .catch(error=>console.log(error))

        // fetch("http://127.0.0.1:8000/job_role_skills/create",
        //     {
        //         method: "POST",
        //         headers: { "Content-Type": "application/json" },
        //         body: JSON.stringify(newCourses)
        //     }).then(fetchCourseList)

        //     .then(response=>console.log(response))
        //     .catch(error=>console.log(error))

    }

    const [JobID, setJobID] = useState([])
    const fetchJobID = async () => {
        const response = await fetch("http://127.0.0.1:8000/jobroles/")
        const JobID = await response.json()
        setJobID(JobID)
    }
    useEffect(() => {
        fetchJobID()
    }, [])

    const [SkillID, setSkillID] = useState([])
    const fetchSkillID = async () => {
        const response = await fetch("http://127.0.0.1:8000/skills")
        const SkillID = await response.json()
        setSkillID(SkillID)
    }
    useEffect(() => {
        fetchSkillID()
    }, [])

    const IDList=[]
    JobID.map((JobID)=>{
        IDList.push(JobID.Job_Role_ID)
        
    })

    const departmentList=[]
    JobID.map((JobID)=>{
        departmentList.push(JobID.Job_Department)
        
    })
    
    const skillList=[]
    SkillID.map((SkillID)=>{
        skillList.push(SkillID.Skill_ID)
        
    })
   
    console.log(skillList)

    return (
        <>
        <p><b><u>Skills Assignment</u></b></p>
        <form>
        Role ID:
        <select 
        onChange={(event) => handleInput1(event.target.value)}>
        <option>Select</option>
           {IDList.map((ID)=>
           <option value = {ID} >{ID}</option>
           )}
        </select>

        Skills ID:
        <select 
        onChange={(event) => handleInput3(event.target.value)}>
            <option>Select</option>
           {skillList.map((skill)=>
           <option value = {skill} >{skill}</option>
           )}
        </select>

             <button type="submit" value="Submit" onClick={handleSubmit}>Assign</button>


        </form>
        </>
            
    )
}



// function DeleteAssignSkills() {

//     const [id, setID] = React.useState("")
//     const [department, setDepartment] = React.useState("")

//     const { Courses, fetchCourseList } = React.useContext(CourseListContext)

//     const handleInput1 = (id1)=> {
//         setID(id1)
        
//     }

//     const handleInput3 = (department1) => {
//         setDepartment(department1)
//     }

    
//     const handleSubmit = (event) => {
//         const newCourses = {
//             "Job_Role_ID": id,
//             "Skill_ID": department,
//             'Active':1
//         }

//         fetch("http://127.0.0.1:8000/job_role_skills/delete",
//         {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify(newCourses)
//         }).then(fetchCourseList)

//         .then(response=>console.log(response))
//         .catch(error=>console.log(error))

        // fetch("http://127.0.0.1:8000/job_role_skills/create",
        //     {
        //         method: "POST",
        //         headers: { "Content-Type": "application/json" },
        //         body: JSON.stringify(newCourses)
        //     }).then(fetchCourseList)

        //     .then(response=>console.log(response))
        //     .catch(error=>console.log(error))

//     }

//     const [JobID, setJobID] = useState([])
//     const fetchJobID = async () => {
//         const response = await fetch("http://127.0.0.1:8000/jobroles/")
//         const JobID = await response.json()
//         setJobID(JobID)
//     }
//     useEffect(() => {
//         fetchJobID()
//     }, [])

//     const [SkillID, setSkillID] = useState([])
//     const fetchSkillID = async () => {
//         const response = await fetch("http://127.0.0.1:8000/skills")
//         const SkillID = await response.json()
//         setSkillID(SkillID)
//     }
//     useEffect(() => {
//         fetchSkillID()
//     }, [])

//     const IDList=[]
//     JobID.map((JobID)=>{
//         IDList.push(JobID.Job_Role_ID)
        
//     })

//     const departmentList=[]
//     JobID.map((JobID)=>{
//         departmentList.push(JobID.Job_Department)
        
//     })
    
//     const skillList=[]
//     SkillID.map((SkillID)=>{
//         skillList.push(SkillID.Skill_ID)
        
//     })
   
    

//     return (
//         <>
//         <p><b><u>Delete Skills Assignment</u></b></p>
//         <form>
//         Role ID:
//         <select 
//         onChange={(event) => handleInput1(event.target.value)}>
//         <option>Select</option>
//            {IDList.map((ID)=>
//            <option value = {ID} >{ID}</option>
//            )}
//         </select>

//         Skills ID:
//         <select 
//         onChange={(event) => handleInput3(event.target.value)}>
//             <option>Select</option>
//            {skillList.map((skill)=>
//            <option value = {skill} >{skill}</option>
//            )}
//         </select>

//              <button type="button" value="Submit" onClick={handleSubmit}>Assign</button>


//         </form>
//         </>
            
//     )
// }
