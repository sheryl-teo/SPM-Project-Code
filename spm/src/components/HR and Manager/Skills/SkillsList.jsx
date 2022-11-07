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


// Fetching Skill List Data
const CourseListContext = React.createContext({
    CourseList: [], fetchCourseList: () => { }
})

export default function JobList() {
    const [CourseList, setCourseList] = useState([])
    const fetchCourseList = async () => {
        const response = await fetch("http://127.0.0.1:8000/skills")
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
    console.log(JobAssignment)
    const JobAssignmentList={}
    
    JobAssignment.map((JobAssignment)=>{
        if(JobAssignment.Skill_ID in JobAssignmentList){
            if(JobAssignment.Skill_ID=='undefined'){
            }
            else{
        const skills = JobAssignment.Job_Role_ID +' '
        JobAssignmentList[JobAssignment.Skill_ID].push(skills)
            }

        }

        else{
            if(JobAssignment.Skill_ID=='undefined'){
            }
            else{
        const skills = JobAssignment.Role_Job_ID +' '
        JobAssignmentList[JobAssignment.Skill_ID]=[skills]
        }
    }
   
    })


    CourseList.map((Course)=>{
        if(Course.Skill_ID in JobAssignmentList){
            Course['Roles']=JobAssignmentList[Course.Skill_ID]

        }

        else{
            Course['Roles']='-'
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
            
            
            <h1><b><u>Skills Available</u></b></h1>
            <ol>
                <AddCourses/>
                <SoftDelete/>
                <UndoSoftDelete/>
                <UpdateCourses/>
                <AssignSkills/>
                {CourseList.map((CourseList) => (
                    
                    <>
                        
                        <li>Skill ID: <b>{CourseList.Skill_ID}</b> Skill Name: <b>{CourseList.Skill_Name}</b>  Status:<b>{CourseList.Status}</b> Roles That Requires The Skill: {CourseList.Roles}</li><br></br>
                        
                        {/* <TodoHelper Role_Name={CourseList.Job_Role_Name} Department = {CourseList.Job_Department} id={CourseList.Job_Role_ID} fetchCourseList={fetchCourseList} /> <br></br> */}
                    </>
            ))}
            </ol>

        </CourseListContext.Provider>
        
    )
}

// Adding Skills to Skill List

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

    const handleSubmit = (event) => {
        const newCourses = {
            "Skill_ID": item1,
            "Skill_Name": item2,
            'Active':1
        }

        fetch("http://127.0.0.1:8000/skills/create",
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
        <p><b><u>Skill Addition</u></b></p>
        <form>
        <label>
            Skill ID: <input type="text" name="name" onChange={handleInput1}/>
        </label>
        
        <label>
            Skill Name: <input type="text" name="name" onChange={handleInput2}/>
        </label>
        
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

    

    const handleSubmit = (event) => {
        const newCourses = {
            "Skill_ID": id,
            "Skill_Name": name,
            'Active':1
        }

        fetch("http://127.0.0.1:8000/skills/update",
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
        const response = await fetch("http://127.0.0.1:8000/skills")
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
        IDList.push(JobID.Skill_ID)
        
    })


    return (
        <>
        <p><b><u>Skill Update</u></b></p>
        <form>
        Skill ID:
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

             <button type="submit" value="Submit" onClick={handleSubmit}>Update</button>


        </form>
        </>
            
    )
}

// Soft Delete Of Skills

function SoftDelete(){

    const [id, setID] = React.useState("")

    const { Courses, fetchCourseList } = React.useContext(CourseListContext)

    const handleInput1 = (id1)=> {
        setID(id1)
        
    }

    const handleSubmit = (event) => {
        fetch("http://127.0.0.1:8000/skills/delete/soft/"+id)
        .then(fetchCourseList)

        .then(response=>console.log(response))
        .catch(error=>console.log(error))
    }

    const [JobID, setJobID] = useState([])
    const fetchJobID = async () => {
        const response = await fetch("http://127.0.0.1:8000/skills")
        const JobID = await response.json()
        setJobID(JobID)
    }
    useEffect(() => {
        fetchJobID()
    }, [])

    console.log(JobID)

    const IDList=[]
    JobID.map((JobID)=>{
        IDList.push(JobID.Skill_ID)
        
    })

    return (
            <>
            <p><b><u>Skill Soft Delete</u></b></p>
            <form>
                Skill ID: 
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
        fetch("http://127.0.0.1:8000/skills/delete/softrestore/"+id)
        .then(fetchCourseList)

        .then(response=>console.log(response))
        .catch(error=>console.log(error))
    }

    const [JobID, setJobID] = useState([])
    const fetchJobID = async () => {
        const response = await fetch("http://127.0.0.1:8000/skills")
        const JobID = await response.json()
        setJobID(JobID)
    }
    useEffect(() => {
        fetchJobID()
    }, [])

    console.log(JobID)

    const IDList=[]
    JobID.map((JobID)=>{
        IDList.push(JobID.Skill_ID)
        
    })

    return (
            <>
            <p><b><u>Skill Soft Delete</u></b></p>
            <form>
                Skill ID: 
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
        .catch(error=>alert(error))

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
   
    

    return (
        <>
        <p><b><u>Roles Assignment</u></b></p>
        <form>
 

        Skills ID:
        <select 
        onChange={(event) => handleInput3(event.target.value)}>
            <option>Select</option>
           {skillList.map((skill)=>
           <option value = {skill} >{skill}</option>
           )}
        </select>

        Role ID:
        <select 
        onChange={(event) => handleInput1(event.target.value)}>
        <option>Select</option>
           {IDList.map((ID)=>
           <option value = {ID} >{ID}</option>
           )}
        </select>

             <button type="submit" value="Submit" onClick={handleSubmit}>Assign</button>


        </form>
        </>
            
    )
}


   