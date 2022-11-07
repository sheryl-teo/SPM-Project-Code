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


// function TodoHelper({ Role_Name,Department, id, fetchCourseList }) {
//     return (
//         <Box p={1} shadow="sm">
//             <Flex justify="middle">
//                 <Text mt={4} as="div">
//                     {/* {Role_Name} */}
//                     <Flex align="end">
//                         <UpdateTodo Role_Name = {Role_Name} Department ={Department} id={id} fetchCourseList={fetchCourseList} />
// {/* //                         <DeleteTodo Role_Name = {Role_Name} Department ={Department} id={id} fetchCourseList={fetchCourseList}/> */}
// //                     </Flex>
// //                 </Text>
// //             </Flex>
// //         </Box>
//     )
// }

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
   
    })

   
    return (
        
        
        <CourseListContext.Provider value={{ CourseList, fetchCourseList }}>
            
            
            <h1><b><u>Roles Available</u></b></h1>
            <ol>
                <AddCourses/>
                <UpdateCourses/>
                <AssignSkills/>
                {CourseList.map((CourseList) => (
                    <>
                        
                        <li>Role ID: <b>{CourseList.Job_Role_ID}</b> Role Name: <b>{CourseList.Job_Role_Name}</b> Department: <b>{CourseList.Job_Department}</b> Skills Required: {CourseList.Skills}</li><br></br>
                        
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
    const [item3, setItem3] = React.useState("")


    const { Courses, fetchCourseList } = React.useContext(CourseListContext)

    const handleInput1 = event => {
        setItem1(event.target.value)
    }

    const handleInput2 = event => {
        setItem2(event.target.value)
    }

    const handleInput3 = event => {
        setItem3(event.target.value)
    }

    const handleSubmit = (event) => {
        const newCourses = {
            "Job_Role_ID": item1,
            "Job_Role_Name": item2,
            "Job_Department": item3,
            'Active':0
        }

        fetch("http://127.0.0.1:8000/jobroles/create",
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(newCourses)
            }).then(fetchCourseList)

            .then(response=>console.log(response))
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

        <label>
            Department : <input type="text" name="name" onChange={handleInput3}/>
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
            "Skill_ID": id,
            "Job_Role_ID": department,
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

             <button type="button" value="Submit" onClick={handleSubmit}>Assign</button>


        </form>
        </>
            
    )
}




// function UpdateTodo({ Role_Name, Department, id }) {
//     const { isOpen, onOpen, onClose } = useDisclosure()
//     const [todo1, setTodo1] = useState(id)
//     const [todo2, setTodo2] = useState(Role_Name)
//     const [todo3, setTodo3] = useState(Department)
//     const { fetchCourseList } = React.useContext(CourseListContext)

//     const updateTodo = async () => {
//         await fetch(`http://127.0.0.1:8000/job_roles/update_job_role/`+ id, {
//             method: "PUT",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({"Job_Role_ID":todo1,"Job_Role_Name": todo2 , "Job_Department":todo3})
//         })
//         // console.log(todo1)
//         onClose()
//         await fetchCourseList()
//     }

//     return (
//         <>
//         <p><b><u>Role Addition</u></b></p>
//         <form>
//         <label>
//             Role ID: <input type="text" name="name" onChange={handleInput1}/>
//         </label>
        
//         <label>
//             Role Name: <input type="text" name="name" onChange={handleInput2}/>
//         </label>

//         <label>
//             Department : <input type="text" name="name" onChange={handleInput3}/>
//         </label>

//              <button type="button" value="Submit" onClick={handleSubmit}>Submit</button>


//         </form>
//         </>
//     )


// }


// function DeleteTodo({Role_Name, Department, id}) {
//     // console.log(id)
//     const {fetchCourseList} = React.useContext(CourseListContext)
  
//     const deleteTodo = async () => {
//       await fetch(`http://127.0.0.1:8000/job_roles/delete_job_role/${id}`, {
//         method: "PUT",
//         headers: { "Content-Type": "application/json" },
//         body: { "Job_Role_ID":id,"Job_Role_Name": Role_Name , "Job_Department":Department }
//       })
//       await fetchCourseList()
//     }
  
//     return (
//       <Button h="1.5rem" size="sm" onClick={deleteTodo}>Delete Role</Button>
//     )
//   }


   