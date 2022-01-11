const fs = require("fs");
const express = require("express");
const bodyParser = require("body-parser");

// Hold the data from JSON file and file path.
const jsonFilePath = "/../assets/data.json";
let mentorData;

// Loading and configuring Express app.
const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));

// Default route for the GET request.
app.get("/", (req, res) => {

    // Getting query parameters.
    const offset = Number.parseInt(req.query.offset?req.query.offset:0);        // Defaults to 0
    const limit = Number.parseInt(req.query.limit?req.query.limit:10);          // Defaults to 10
    
    // Slicing the JSON data for required data
    try{
        const requestedData = mentorData.slice(offset, Math.min(offset+limit, mentorData.length));
        res.json(requestedData);
    } catch(err){
        res.sendStatus(500)
        console.log("Error in slicing");
    }
})

// Run Express App.
app.listen(5000, () => {
    console.log("Server started on port 5000");
    getMentorData();
    console.log("Loaded Mentor data from the file.");
});

// Helper function to load the JSON file.
getMentorData = () => {
    try {
        mentorData = fs.readFileSync(__dirname + jsonFilePath , "utf-8");
    } catch (err) {
        console.log("Error opening the file");
        console.log(err);
    }
    try {
        mentorData = JSON.parse(mentorData);
    } catch (err) {
        console.log("Error parsing JSON");
        console.log(err);
    }
};