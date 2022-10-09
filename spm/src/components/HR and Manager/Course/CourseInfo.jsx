
function CourseDetails(props){
    return (
        <div className='expense-item__description'>
                <h2>{props.courses[0].Course_ID}</h2>
                <div className='expense-item__price'>Coourse Name: <br/>{props.courses[0].Course_Name}</div>
                <br/>
                <div className='expense-item__price'>Course Description: {props.courses[0].Course_Desc}</div>
                <br/>
                <div className='expense-item__price'>Course Status: {props.courses[0].Course_Status}</div>
                <br/>
                <div className='expense-item__price'>Course Type: {props.courses[0].Course_Type}</div>
                <br/>
                <div className='expense-item__price'>Course Category: {props.courses[0].Course_Category}</div>
                <br/>
            </div>
    )
}

export default CourseDetails