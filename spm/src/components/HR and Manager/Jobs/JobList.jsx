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
                {CourseList.map((CourseList) => (
                    <>
                        
                        <li>Role ID: <b>{CourseList.Job_Role_ID}</b> Role Name: <b>{CourseList.Job_Role_Name}</b> Department: <b>{CourseList.Job_Department}</b> Skills Required: {CourseList.Skills}</li>
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
            'Active':1
        }
        console.log(newCourses)

        fetch("http://127.0.0.1:8000/jobroles/create",
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(newCourses)
            }).then(fetchCourseList)
    }

    return (
        <>
        <p><b><u>Role Addition</u></b></p>
        <form>
        <label>
            Role Name: <input type="text" name="name" onChange={handleInput1}/>
        </label>
        
        <label>
            Role ID: <input type="text" name="name" onChange={handleInput2}/>
        </label>

        <label>
            Department : <input type="text" name="name" onChange={handleInput3}/>
        </label>

             <button type="button" value="Submit" onClick={handleSubmit}>Submit</button>


        </form>
        </>
            
    )
}

// // update DB 


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
//             <Button h="1.5rem" size="sm" onClick={onOpen}>Update Role</Button>
//             <Modal isOpen={isOpen} onClose={onClose}>
//                 <ModalOverlay />
//                 <ModalContent>
//                     <ModalHeader>Update Role</ModalHeader>
//                     <ModalCloseButton />
//                     <ModalBody>
//                         <InputGroup size="md">
                            
//                             <Input
//                                 pr="4.5rem"
//                                 type="text"
//                                 placeholder= "Update Role ID"
//                                 aria-label="Update Role ID"
//                                 // value={todo}
//                                 onChange={e => setTodo1(e.target.value)}
//                             />

//                             <Input
//                                 pr="4.5rem"
//                                 type="text"
//                                 placeholder="Update Role Name"
//                                 aria-label="Update Role Name"
                        
//                                 onChange={e => setTodo2(e.target.value)}
//                             />

//                             <Input
//                                 pr="4.5rem"
//                                 type="text"
//                                 placeholder="Update Department"
//                                 aria-label="Update Department"
                                
//                                 onChange={e => setTodo3(e.target.value)}
//                             />

//                         </InputGroup>
//                     </ModalBody>

//                     <ModalFooter>
//                         <Button h="1.5rem" size="sm" onClick={updateTodo}>Update Role</Button>
//                     </ModalFooter>
//                 </ModalContent>
//             </Modal>
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


   