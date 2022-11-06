import React, { useEffect, useState } from "react";
import CourseInfo from "./CourseInfo";
import { Link, BrowserRouter as Router, Routes, Route}
	from 'react-router-dom';import {
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
        const response = await fetch("http://127.0.0.1:8000/courses/get_all_courses")
        const CourseList = await response.json()
        setCourseList(CourseList)
    }
    useEffect(() => {
        fetchCourseList()
    }, [])

    // const CourseRoutes = CourseList.map(
    //   (courses)=>{
    //     <Route path = {`/HR/Courses/${courses.Course_ID}`} element = {CourseInfo(courses)}/>
        
    //   }
    // )



    return (

        <CourseListContext.Provider value={{ CourseList, fetchCourseList }}>

            <h1><b><u>Courses Available</u></b></h1>
            <ol>
                
                {CourseList.map((CourseList) => (
                    <>
                        
                        <li>Course ID: <b>{CourseList.Course_ID}</b> Course Name: <b>{CourseList.Course_Name}</b> Course Description: <b>{CourseList.Course_Desc}</b> Course Status: <b>{CourseList.Course_Status}</b> Course Type: <b>{CourseList.Course_Type}</b> Course Category: <b>{CourseList.Course_Category}</b></li><br></br>
                        {/* <Link to= {`/HR/Courses/${CourseList.Course_ID}`}>Link</Link><br></br> */}
                        
                    </>
                ))}
            </ol>

        </CourseListContext.Provider>
        
    )
}