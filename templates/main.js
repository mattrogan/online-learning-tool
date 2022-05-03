/**
 * Functionality for post pages will go in here
 */

function newPost() {
    // Function to get data for a new post
}

function goBack() {
    // Function for button to go back to previous page
}


function getFormData() {
    /**
     * Function to get data from submission form
     */
    var submission_name = document.getElementById("name").value;
    var submission_title = document.getElementById("qtitle").value;
    var submission_desc = document.getElementById("qdesc").value;

    document.getElementById("name_data").innerHTML = submission_name;
    document.getElementById("title_data").innerHTML = submission_title;
    document.getElementById("desc_data").innerHTML = submission_desc;

}