
import React, { useEffect, useState } from "react";
import "./learningJourneys.css"

const LearningJourneys = (props) => {
    var userID = 140001

    const [LJ, setLJ] = useState([])

    const fetchLJ = async () => {
        var userID = "130001"
        const response = await fetch("http://127.0.0.1:8000/learning_journey/get_staff_learning_journey/"+userID)
        const LJ = await response.json()
        const LJList = []
        LJ.map((LJ) => {
            LJList.push([LJ.Learning_Journey_ID, LJ.Staff_ID])
        })
        setLJ(LJList)
    }
    useEffect(() => {
        fetchLJ()
    }, [])


    console.log(LJ)

    console.log(props.id)
    var allLinks = []

    for (var i in LJ) {
        allLinks.push('/ljdetails/' + LJ[i][0])
    }
    var dom_content = [];
    for (var link in allLinks) {
        console.log(LJ)
        dom_content.push(
            (
                
                <div className="indivLJ"><a href={allLinks[link][0]}>Testing</a></div>
            )
        );
    }

    return (
        <div id='overallLJ'>
            {dom_content}
        </div>
    );
};

export default LearningJourneys;